import win32com.client as win32
from datetime import datetime, timedelta

from commands.anexos_state import obter_anexos
from commands.texto_settings import renderizar_email
from commands.visor_settings import mostrar_mensagem
from database.setup_db import Session, Dados, Motorista, Email, EmailRegistro


# =========================================================
# ENVIO DE E-MAIL
# =========================================================
def enviar_email(dados_id):
    anexos = obter_anexos()

    if not anexos or len(anexos) != 2:
        mostrar_mensagem("E-mail não enviado. Anexos obrigatórios não foram selecionados.")
        return None

    sessao = Session()

    try:
        emails_to = sessao.query(Email).filter(Email.opcao_selecionada == 'A').all()
        emails_cc = sessao.query(Email).filter(Email.opcao_selecionada.in_(['B', 'C'])).all()

        to_str = '; '.join(e.email for e in emails_to)
        cc_str = '; '.join(e.email for e in emails_cc)

        dados = sessao.get(Dados, dados_id)
        motorista = sessao.get(Motorista, dados.motorista_id)

        assunto, corpo, _ = renderizar_email(dados, motorista)

        # Registro inicial (SEM dados do Outlook ainda)
        registro = EmailRegistro(
            assunto=assunto,
            destinatario=to_str,
            data_envio=datetime.now(),
            status="aguardando_envio_outlook",
            dados_id=dados_id
        )

        sessao.add(registro)
        sessao.commit()

        outlook = win32.Dispatch("Outlook.Application")
        mail = outlook.CreateItem(0)

        mail.To = to_str
        mail.CC = cc_str
        mail.Subject = assunto

        mail.Display()
        assinatura = mail.HTMLBody
        mail.HTMLBody = corpo + assinatura

        for arquivo in anexos:
            mail.Attachments.Add(arquivo)

        try:
            mail.Send()
        except Exception as e:
            registro.status = "erro"
            sessao.commit()
            mostrar_mensagem(f"Erro ao enviar e-mail: {e}")
            return None

        registro.status = "enviado"
        sessao.commit()

        mostrar_mensagem("E-mail enviado com sucesso.")
        return registro.id

    except Exception as e:
        sessao.rollback()
        mostrar_mensagem(f"Erro geral ao enviar e-mail: {e}")
        return None

    finally:
        sessao.close()


# =========================================================
# SINCRONIZA COM ITENS ENVIADOS (OUTLOOK)
# =========================================================
def sincronizar_email_enviado(registro_id):
    sessao = Session()

    try:
        registro = sessao.get(EmailRegistro, registro_id)
        if not registro:
            return False

        outlook = win32.Dispatch("Outlook.Application")
        namespace = outlook.GetNamespace("MAPI")

        sent_folder = namespace.GetDefaultFolder(5)  # Itens Enviados
        itens = sent_folder.Items
        itens.Sort("[SentOn]", True)

        data_limite = registro.data_envio - timedelta(minutes=10)

        for mail in itens:
            try:
                if mail.Class != 43:
                    continue

                if mail.SentOn < data_limite:
                    break

                if (
                    mail.Subject == registro.assunto and
                    registro.destinatario.lower() in mail.To.lower()
                ):
                    registro.entry_id = mail.EntryID
                    registro.store_id = mail.Parent.StoreID
                    registro.conversation_id = mail.ConversationID
                    registro.remetente = mail.SenderEmailAddress
                    registro.status = "aguardando_resposta"

                    sessao.commit()
                    return True

            except Exception:
                continue

        return False

    except Exception as e:
        sessao.rollback()
        mostrar_mensagem(f"Erro ao sincronizar e-mail: {e}")
        return False

    finally:
        sessao.close()


# =========================================================
# VERIFICA SE O E-MAIL FOI RESPONDIDO
# =========================================================
def email_foi_respondido(conversation_id):
    outlook = win32.Dispatch("Outlook.Application")
    namespace = outlook.GetNamespace("MAPI")

    inbox = namespace.GetDefaultFolder(6)  # Caixa de Entrada
    itens = inbox.Items
    itens.Sort("[ReceivedTime]", True)

    for mail in itens:
        try:
            if mail.Class != 43:
                continue

            if mail.ConversationID == conversation_id:
                return mail

        except Exception:
            continue

    return None


# =========================================================
# BUSCAR RESPOSTA POR ASSUNTO E DESTINATÁRIO
# =========================================================
def buscar_resposta_por_assunto_e_destinatario(registro):
    outlook = win32.Dispatch("Outlook.Application")
    namespace = outlook.GetNamespace("MAPI")
    inbox = namespace.GetDefaultFolder(6)  # Caixa de Entrada

    itens = inbox.Items
    itens.Sort("[ReceivedTime]", True)

    for mail in itens:
        try:
            if mail.Class != 43:
                continue

            if (
                mail.Subject == registro.assunto or
                mail.Subject.endswith(registro.assunto)
            ):
                return mail

        except Exception:
            continue

    return None


# =========================================================
# RESPONDER / ENCERRAR E-MAIL COM BASE NOS DADOS
# =========================================================
def responder_email_por_dados(dados_id):
    sessao = Session()

    try:
        registro = (
            sessao.query(EmailRegistro)
            .filter(
                EmailRegistro.dados_id == dados_id,
                EmailRegistro.status.in_(["aguardando_resposta", "enviado"])
            )
            .order_by(EmailRegistro.data_envio.desc())
            .first()
        )

        if not registro:
            mostrar_mensagem("Nenhum e-mail ativo encontrado para esse envio.")
            return

        # Garante que o Outlook já reconheceu o envio
        if not registro.conversation_id:
            resposta = buscar_resposta_por_assunto_e_destinatario(registro)

            if not resposta:
                mostrar_mensagem("O e-mail ainda não foi respondido.")
                return

            # Agora sim, aprendemos a conversa pela resposta
            registro.conversation_id = resposta.ConversationID
            registro.data_recebimento = resposta.ReceivedTime
            registro.status = "aguardando_resposta"
            sessao.commit()


        resposta = email_foi_respondido(registro.conversation_id)

        if not resposta:
            mostrar_mensagem("O e-mail ainda não foi respondido.")
            return
        
        dados = sessao.get(Dados, dados_id)
        motorista = sessao.get(Motorista, dados.motorista_id)

        _, _, resposta_automatica = renderizar_email(dados, motorista)

        if not resposta_automatica:
            mostrar_mensagem("Nenhuma resposta automática configurada.")
            return

        reply = resposta.ReplyAll()
        reply.HTMLBody = (resposta_automatica + reply.HTMLBody)
        reply.Send()

        registro.status = "encerrado"
        registro.data_recebimento = resposta.ReceivedTime

        sessao.commit()
        mostrar_mensagem("E-mail encerrado com sucesso.")

    except Exception as e:
        sessao.rollback()
        mostrar_mensagem(f"Erro ao encerrar e-mail: {e}")

    finally:
        sessao.close()

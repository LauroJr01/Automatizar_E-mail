import time
import win32com.client as win32
from datetime import datetime

from commands.anexos_state import obter_anexos
from commands.texto_settings import renderizar_email
from commands.visor_settings import mostrar_mensagem
from database.setup_db import Session, Dados, Motorista, Email, EmailRegistro

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
        if not dados:
            mostrar_mensagem("Dados não encontrados para envio.")
            return None

        motorista = sessao.get(Motorista, dados.motorista_id)
        if not motorista:
            mostrar_mensagem("Motorista não encontrado.")
            return None

        assunto, corpo, _ = renderizar_email(dados, motorista)
        if not assunto:
            mostrar_mensagem("Erro ao gerar o e-mail.")
            return None

        outlook = win32.Dispatch("Outlook.Application")
        mail = outlook.CreateItem(0)

        mail.To = to_str
        mail.CC = cc_str
        mail.Subject = assunto

        assinatura = mail.HTMLBody
        mail.HTMLBody = corpo + assinatura

        for arquivo in anexos:
            mail.Attachments.Add(arquivo)

        mail.Save()

        assunto = mail.Subject
        destinatario = mail.To
        remetente = getattr(mail, "SenderEmailAddress", None)

        mail.Send()

        time.sleep(1)  # Outlook precisa respirar

        namespace = outlook.GetNamespace("MAPI")
        sent_folder = namespace.GetDefaultFolder(5)  # 5 = Itens Enviados

        mail_enviado = None
        for item in sent_folder.Items:
            if (
                item.Subject == assunto and
                destinatario in item.To
            ):
                mail_enviado = item
                break

        if not mail_enviado:
            raise Exception("E-mail enviado, mas não localizado nos Itens Enviados.")

        entry_id = mail_enviado.EntryID
        store_id = mail_enviado.Parent.StoreID


        registro = EmailRegistro(
            entry_id=entry_id,
            store_id=store_id,
            assunto=assunto,
            destinatario=destinatario,
            remetente=remetente,
            data_envio=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            status="enviado",
            dados_id=dados_id
        )

        sessao.add(registro)
        sessao.commit()

        mostrar_mensagem("E-mail enviado com sucesso.")
        return registro.id

    except Exception as e:
        sessao.rollback()
        mostrar_mensagem(f"Erro ao enviar e-mail: {e}")
        return None
    finally:
        sessao.close()



def responder_email_por_dados(dados_id):
    sessao = Session()
    try:
        # Busca o último e-mail ENVIADO com esse contexto
        email_base = (
            sessao.query(EmailRegistro)
            .filter(
                EmailRegistro.dados_id == dados_id,
                EmailRegistro.status == "enviado"
            )
            .order_by(EmailRegistro.data_envio.desc())
            .first()
        )

        if not email_base:
            mostrar_mensagem("Nenhum e-mail enviado encontrado para resposta.")
            return

        dados = sessao.get(Dados, dados_id)
        if not dados:
            mostrar_mensagem("Dados não encontrados.")
            return

        motorista = sessao.get(Motorista, dados.motorista_id)
        if not motorista:
            mostrar_mensagem("Motorista não encontrado.")
            return

        assunto, corpo, texto_resposta = renderizar_email(dados, motorista)
        if not corpo and not texto_resposta:
            mostrar_mensagem("Erro ao gerar a resposta.")
            return
        
        texto_resposta = texto_resposta or ''
        corpo = corpo or ''

        outlook = win32.Dispatch("Outlook.Application")
        namespace = outlook.GetNamespace("MAPI")

        mail_item = namespace.GetItemFromID(
            email_base.entry_id,
            email_base.store_id
        )

        resposta = mail_item.ReplyAll()

        assinatura = resposta.HTMLBody
        if texto_resposta:
            resposta.HTMLBody = texto_resposta + assinatura
        else:
            resposta.HTMLBody = corpo + assinatura

        resposta.Save()

        assunto_resp = resposta.Subject
        destinatario_resp = resposta.To
        remetente_resp = resposta.SenderEmailAddress

        entry_id_resp = resposta.EntryID
        store_id_resp = resposta.Parent.StoreID

        resposta.Send()

        registro_resposta = EmailRegistro(
            entry_id=entry_id_resp,
            store_id=store_id_resp,
            assunto=assunto_resp,
            destinatario=destinatario_resp,
            remetente=remetente_resp,
            data_envio=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            status="respondido",
            dados_id=dados_id
        )

        email_base.status = "respondido"

        sessao.add(registro_resposta)
        sessao.add(email_base)
        sessao.commit()

        mostrar_mensagem("Resposta enviada com sucesso.")

    except Exception as e:
        sessao.rollback()
        mostrar_mensagem(f"Erro ao responder e-mail: {e}")
    finally:
        sessao.close()

import time
import win32com.client as win32
from commands.anexos_state import obter_anexos
from commands.texto_settings import renderizar_email
from commands.visor_settings import mostrar_mensagem
from database.setup_db import Session, Dados, Motorista, Email


def enviar_email():
    # 👉 ANEXOS (antes de tudo)
    anexos = obter_anexos()

    if not anexos or len(anexos) != 2:
        mostrar_mensagem("E-mail não enviado. Anexos obrigatórios não foram selecionados.")
        return


    sessao = Session()
    try:
        emails_to = sessao.query(Email).filter(Email.opcao_selecionada == 'A').all()
        emails_cc = sessao.query(Email).filter(Email.opcao_selecionada.in_(['B', 'C'])).all()

        to_str = '; '.join(e.email for e in emails_to)
        cc_str = '; '.join(e.email for e in emails_cc)

        dados = sessao.query(Dados).order_by(Dados.id.desc()).first()
        if not dados:
            mostrar_mensagem("Nenhum dado encontrado para envio.")
            return

        motorista = sessao.get(Motorista, dados.motorista_id)
        if not motorista:
            mostrar_mensagem("Motorista não encontrado.")
            return

    finally:
        sessao.close()

    assunto, corpo = renderizar_email(dados, motorista)
    if not assunto:
        mostrar_mensagem("Erro ao gerar o e-mail.")
        return

    outlook = win32.Dispatch('outlook.application')
    email = outlook.CreateItem(0)

    email.To = to_str
    email.CC = cc_str
    email.Subject = assunto

    # 👉 Abre para o Outlook aplicar a assinatura
    email.Display()
    time.sleep(0.2)

    assinatura = email.HTMLBody
    email.HTMLBody = corpo + assinatura

    # 👉 Anexa os arquivos
    for arquivo in anexos:
        email.Attachments.Add(arquivo)

    email.Send()
    mostrar_mensagem("E-mail enviado com sucesso.")

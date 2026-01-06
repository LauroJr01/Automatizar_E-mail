from database.setup_db import Session, EmailTemplate
from datetime import datetime
from commands.visor_settings import mostrar_mensagem

def obter_template():
    sessao = Session()
    try:
        return sessao.query(EmailTemplate).first()
    finally:
        sessao.close()


def carregar_template(entry_assunto, textbox_corpo):
    sessao = Session()
    try:
        template = sessao.query(EmailTemplate).first()
        if not template:
            return

        entry_assunto.delete(0, "end")
        entry_assunto.insert(0, template.assunto)

        textbox_corpo.delete("1.0", "end")
        textbox_corpo.insert("1.0", template.corpo)

    finally:
        sessao.close()


def salvar_template(entry_assunto, textbox_corpo):
    assunto = entry_assunto.get().strip()
    corpo = textbox_corpo.get("1.0", "end-1c").strip()

    if not assunto or not corpo:
        return False

    sessao = Session()
    try:
        template = sessao.query(EmailTemplate).first()
        if not template:
            template = EmailTemplate(assunto=assunto, corpo=corpo)
            sessao.add(template)
        else:
            template.assunto = assunto
            template.corpo = corpo

        sessao.commit()
        mostrar_mensagem("Template salvo com sucesso!")
        return True
    finally:
        sessao.close()


def renderizar_email(dados, motorista):
    template = obter_template()
    if not template or not dados or not motorista:
        return None, None

    data = datetime.now().strftime('%d/%m/%Y')

    assunto = template.assunto.format(
        data=dados.data,
        carreta=dados.numero_carreta,
        local=dados.local
    )

    valor_frete = dados.valor_frete or 0

    corpo = template.corpo.format(
        valor_frete=f"{valor_frete:.2f}",
        placa=motorista.placa,
        motorista=motorista.nome
    )

    return assunto, corpo



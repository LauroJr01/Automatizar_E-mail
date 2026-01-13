import os
import sys
from tkinter import filedialog
from commands.enviar_email import enviar_email, responder_email_por_dados
from database.setup_db import Session, Email, Dados, Motorista
from commands.visor_settings import mostrar_mensagem
from commands.anexos_state import definir_anexos, obter_anexos

# Icone
def resource_path(rel_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, rel_path)
    return os.path.join(os.path.abspath("."), rel_path)


# Botão selecionar todos os e-mails
def selecionar_todos_emails(estado):
    sessao = Session()
    try:
        if estado == 1:
            lista = sessao.query(Email).filter(Email.opcao_selecionada == None).all()
            for email in lista:
                email.opcao_selecionada = "C"            
            #mostrar_mensagem("Todos os e-mails foram selecionados com sucesso.")            
        else:
            lista = sessao.query(Email).filter(Email.opcao_selecionada == "C").all()
            for email in lista:
                email.opcao_selecionada = None
            #mostrar_mensagem("Todos os e-mails foram desmarcados com sucesso.")
        sessao.commit()
    except Exception as e:
        mostrar_mensagem(f"Erro ao atualizar lista: {e}")
    finally:
        sessao.close()

def estado_checkbox_geral():
    sessao = Session()
    try:
        total = sessao.query(Email).count()
        marcados = sessao.query(Email).filter(Email.opcao_selecionada != None).count()
        
        # Se todos estiverem marcados, retorna 1
        return 1 if total > 0 and total == marcados else 0
    finally:
        sessao.close()


# Botões de seleção de local
def selecionar_filial(filial_btn, outros_btn, entry_outros):
    if filial_btn.get() == 1:
        outros_btn.deselect()
        entry_outros.delete(0, "end")
        entry_outros.grid_forget()  # Começa desabilitado

def selecionar_outros(filial_btn, outros_btn, entry_outros):
    if outros_btn.get() == 1:
        filial_btn.deselect()
        entry_outros.grid(row=1, column=0, sticky='nw', padx=(210,0), pady=5)


# Botão de número da carreta
def aplicar_placeholder_combobox(combo, placeholder="N° ..."):
    # Define o placeholder inicial
    combo.set(placeholder)
    combo.configure(text_color=("gray60", "gray60"))

    def limpar(event):
        # Só limpa se estiver no placeholder
        if combo.get() == placeholder:
            combo.set("")
            combo.configure(text_color=("white", "white"))

    def restaurar(event):
        # Se saiu do foco e está vazio → volta o placeholder
        if combo.get() == "":
            combo.set(placeholder)
            combo.configure(text_color=("gray60", "gray60"))

    # Bind ao clicar (limpa)
    combo.bind("<FocusIn>", limpar)

    # Bind ao perder foco (restaura)
    combo.bind("<FocusOut>", restaurar)


# Salvar local, número da carreta e valor do frete
def salvar_dados(selecionado, filial_btn, entry_outros, numero_combobox, entry_valor_frete):
    sessao = Session()
    try:
        # ----- MOTORISTA -----
        motorista = sessao.get(Motorista, selecionado["motorista_id"])


        if not motorista:
            mostrar_mensagem("Nenhum motorista selecionado.")
            return None
        
        # ----- LOCAL -----
        if filial_btn.get() == 1:
            local = "FILIAL"
        else:
            texto = entry_outros.get().strip().upper()
            local = texto if texto else None

        if local is None:
            mostrar_mensagem("Nenhum local definido.")
            return None

        # ----- NÚMERO DA CARRETA -----
        valor = numero_combobox.get().strip()

        if valor.startswith("N°"):
            valor = valor.replace("N°", "").strip()

        if not valor.isdigit():   # impede crash antes do int()
            mostrar_mensagem("Número da carreta inválido.")
            return None

        numero_int = int(valor)

        if numero_int < 1:
            mostrar_mensagem("Número da carreta inválido.")
            return None
        
        # ----- VALOR DO FRETE -----
        valor_frete_texto = entry_valor_frete.get().strip().replace(",", ".")
        if not valor_frete_texto:
            mostrar_mensagem("Valor do frete não definido.")
            return None
        try:
            frete_valor = float(valor_frete_texto)
        except ValueError:
            mostrar_mensagem("Valor do frete inválido.")
            return None
        

        # ----- CRIA O REGISTRO COMPLETO -----
        novo = Dados(
            motorista=motorista,
            local=local,
            numero_carreta=numero_int,
            valor_frete=frete_valor
        )

        sessao.add(novo)
        sessao.commit()

        mostrar_mensagem(f"Motorista: {motorista.nome} | Placa: {motorista.placa} | Local: {local} | Número carreta: {numero_int} | Frete: R$ {frete_valor}")
        return novo.id

    except Exception as e:
        mostrar_mensagem(f"Erro ao salvar os dados: {e}")
        return None
    finally:
        sessao.close()

# Botão de anexar arquivo
def anexar_arquivos():
    arquivos = filedialog.askopenfilenames(title="Selecione os 02 arquivos obrigatórios", filetypes=[("Todos os arquivos", "*.*")])
    if len(arquivos) != 2:
        mostrar_mensagem("Por favor, selecione exatamente 2 arquivos: 1 PDF e 1 XML.")
        return False
    definir_anexos(list(arquivos))
    mostrar_mensagem("Arquivos anexados com sucesso.")
    return True
    

# Botão de enviar e-mail
def salvar_e_enviar(selecionado, filial, entry_outros, numero, valor):
    dados_id = salvar_dados(selecionado, filial, entry_outros, numero, valor)
    if not dados_id:
        mostrar_mensagem("Dados incompletos. E-mail não enviado.")
        return

    anexos = obter_anexos()    
    if not anexos or len(anexos) != 2:
        mostrar_mensagem("Selecione exatamente 1 PDF e 1 XML antes de enviar o e-mail.")
        return    
    for arquivo in anexos:
        if not os.path.exists(arquivo):
            mostrar_mensagem(f"O arquivo anexado não foi encontrado:\n{arquivo}")
            return

    enviar_email(dados_id)



def obter_dados_por_contexto(selecionado, filial_btn, entry_outros, numero_combobox, entry_valor_frete):
    sessao = Session()
    try:
        motorista_id = selecionado["motorista_id"]

        local = "FILIAL" if filial_btn.get() == 1 else entry_outros.get().strip().upper()
        numero = numero_combobox.get().replace("N°", "").strip()
        valor = entry_valor_frete.get().replace(",", ".")

        if not (motorista_id and local and numero.isdigit() and valor):
            return None

        dados = (
            sessao.query(Dados)
            .filter(
                Dados.motorista_id == motorista_id,
                Dados.local == local,
                Dados.numero_carreta == int(numero),
                Dados.valor_frete == float(valor)
            )
            .order_by(Dados.id.desc())
            .first()
        )

        return dados.id if dados else None

    finally:
        sessao.close()


# Botão de responder e-mail
def salvar_e_responder(selecionado, filial, entry_outros, numero, valor):
    dados_id = obter_dados_por_contexto(
        selecionado,
        filial,
        entry_outros,
        numero,
        valor
    )

    if not dados_id:
        mostrar_mensagem("Nenhum envio anterior encontrado com esses dados.")
        return

    responder_email_por_dados(dados_id)


import customtkinter as ctk
from database.setup_db import Session, Email
from commands.visor_settings import mostrar_mensagem


def cadastrar_email(entry_nome, entry_email, email_lista):
        nome = entry_nome.get().strip().upper()
        email = entry_email.get().strip().lower()
        if not nome or not email:
            mostrar_mensagem('Preencha todos os campos.')
            return
        
        sessao = Session()
        try:
            email_existente = sessao.query(Email).filter_by(nome=nome).first()
            if email_existente:
                mostrar_mensagem('Nome ou E-mail já cadastrado.')
                return
            novo_email = Email(nome=nome, email=email)
            sessao.add(novo_email)
            sessao.commit()
            mostrar_mensagem('E-mail cadastrado com sucesso.')
            atualizar_lista_email(email_lista, entry_nome, entry_email)
        finally:
            sessao.close()

def atualizar_email(entry_nome, entry_email, email_lista):
    nome = entry_nome.get().strip().upper()
    email = entry_email.get().strip().lower()
    if not nome or not email:
        mostrar_mensagem('Preencha todos os campos.')
        return

    sessao = Session()
    try:
        pessoa = sessao.query(Email).filter_by(nome=nome).first()
        if pessoa:
            pessoa.email = email
            sessao.commit()
            mostrar_mensagem('E-mail alterado com sucesso.')
            atualizar_lista_email(email_lista, entry_nome, entry_email)
            return
    finally:
        sessao.close()

def excluir_email(entry_nome, entry_email, email_lista):
    nome = entry_nome.get().strip().upper()
    email = entry_email.get().strip().lower()
    if not nome or not email:
        mostrar_mensagem('Preencha todos os campos.')
        return
    
    sessao = Session()
    try:
        pessoa = sessao.query(Email).filter(Email.nome == nome, Email.email == email).first()
        if not pessoa:
            mostrar_mensagem('Nome ou E-mail incorreto.')
            return
        else:
            sessao.delete(pessoa)
            sessao.commit()
            mostrar_mensagem('E-mail removido com sucesso.')
            atualizar_lista_email(email_lista, entry_nome, entry_email)
            return
    finally:
        sessao.close()
        
def atualizar_lista_email(email_lista, entry_nome, entry_email):
    for widget in email_lista.winfo_children():
        widget.destroy()

    sessao = Session()
    try:
        lista_emails = sessao.query(Email).all()

        def preencher_campos(registro):
            entry_nome.delete(0, "end")
            entry_nome.insert(0, registro.nome)
            entry_email.delete(0, "end")
            entry_email.insert(0, registro.email)

        for registro_email in lista_emails:
            varA = ctk.IntVar(value=0)
            varB = ctk.IntVar(value=0)

            # CARREGA ESTADO GUARDADO NO BANCO
            if registro_email.opcao_selecionada == "A":
                varA.set(1)
            elif registro_email.opcao_selecionada == "B":
                varB.set(1)

            def marcar_A(r=registro_email, vA=varA, vB=varB):
                if vA.get() == 1:
                    vB.set(0)
                    preencher_campos(r)

                    s = Session()
                    obj = s.query(Email).get(r.id)
                    obj.opcao_selecionada = "A"
                    s.commit()
                    s.close()
                else:
                    s = Session()
                    obj = s.query(Email).get(r.id)
                    obj.opcao_selecionada = None
                    s.commit()
                    s.close()
                    # limpando entries ao desmarcar
                    entry_nome.delete(0, "end")
                    entry_email.delete(0, "end")

            def marcar_B(r=registro_email, vA=varA, vB=varB):
                if vB.get() == 1:
                    vA.set(0)
                    preencher_campos(r)

                    s = Session()
                    obj = s.query(Email).get(r.id)
                    obj.opcao_selecionada = "B"
                    s.commit()
                    s.close()
                else:
                    s = Session()
                    obj = s.query(Email).get(r.id)
                    obj.opcao_selecionada = None
                    s.commit()
                    s.close()
                    # limpando entries ao desmarcar
                    entry_nome.delete(0, "end")
                    entry_email.delete(0, "end")

            # FRAME
            frame = ctk.CTkFrame(email_lista)
            frame.pack(fill="x", padx=10, pady=4)

            # CHECKBOX A (laranja)
            chkA = ctk.CTkCheckBox(frame, text="", variable=varA, command=marcar_A, width=1, checkbox_width=25, checkbox_height=25, fg_color="#ff7f00", hover_color="#cc6600", border_color="#ff7f00")
            chkA.pack(side="left", padx=(0, 6))

            # CHECKBOX B (azul)
            chkB = ctk.CTkCheckBox(frame, text="", variable=varB, command=marcar_B, width=1, checkbox_width=25, checkbox_height=25, fg_color="#1f6aa5", hover_color="#144a75", border_color="#1f6aa5")
            chkB.pack(side="left", padx=(0, 6))

            # LABEL
            label = ctk.CTkLabel(frame, text=f"{registro_email.nome} - {registro_email.email}", anchor="w")
            label.pack(side="left", fill="x", expand=True)

    except Exception as e:
        mostrar_mensagem(f"Erro ao atualizar lista: {e}")
    finally:
        sessao.close()

def resetar_all_email(all_email_var, all_email):
    all_email_var.set(0)
    all_email.deselect()

    sessao = Session()
    try:    
        lista = sessao.query(Email).filter(Email.opcao_selecionada == "C").all()
        for email in lista:
            email.opcao_selecionada = None
        sessao.commit()
    except Exception as e:
        mostrar_mensagem(f"Erro ao atualizar lista: {e}")
    finally:
        sessao.close()
import customtkinter as ctk
from database.setup_db import Session, Motorista, Email
from sqlalchemy.exc import IntegrityError
from tkinter import messagebox

def iniciar_programa():
 # ===== BANCO DE DADOS ===== #

    # ++ E-MAIL ++ #
    def cadastrar_email():
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
            atualizar_lista_email()
        finally:
            sessao.close()

    def atualizar_email():
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
                atualizar_lista_email()
                return
        finally:
            sessao.close()

    def excluir_email():
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
                atualizar_lista_email()
                return
        finally:
            sessao.close()

    def atualizar_lista_email():
        """Atualiza a lista de e-mails com checkboxes para seleção múltipla."""
        # Limpa os elementos existentes na lista
        for widget in email_lista.winfo_children():
            widget.destroy()

        sessao = Session()
        try:
            lista_emails = sessao.query(Email).all()
            estados_dos_checkboxes = {}
            emails_selecionados = set()

            def selecionar_email(registro_email):
                """Preenche os campos com os dados do e-mail selecionado."""
                entry_nome.delete(0, "end")
                entry_nome.insert(0, registro_email.nome)
                entry_email.delete(0, "end")
                entry_email.insert(0, registro_email.email)
                mostrar_mensagem(f'E-mail de "{registro_email.nome}" selecionado.')

            def ao_marcar_checkbox(registro_email, estado_checkbox):
                """Adiciona ou remove o e-mail conforme o checkbox é marcado ou desmarcado."""
                if estado_checkbox.get() == 1:
                    emails_selecionados.add(registro_email)
                    selecionar_email(registro_email)
                else:
                    emails_selecionados.discard(registro_email)
                    # Se nenhum estiver marcado, limpa os campos
                    if not emails_selecionados:
                        entry_nome.delete(0, "end")
                        entry_email.delete(0, "end")

            # Cria um checkbox para cada e-mail e já deixa todos marcados
            for registro_email in lista_emails:
                estado_checkbox = ctk.IntVar(value=1)  # Marcado por padrão
                estados_dos_checkboxes[registro_email.id] = estado_checkbox
                checkbox = ctk.CTkCheckBox(email_lista, text=f"{registro_email.nome} - {registro_email.email}", variable=estado_checkbox, command=lambda r=registro_email, e=estado_checkbox: ao_marcar_checkbox(r, e))
                checkbox.pack(anchor="w", padx=10, pady=2)
                # Marca o e-mail como selecionado desde o início
                emails_selecionados.add(registro_email)

            # Preenche o primeiro e-mail na área de edição
            if lista_emails:
                selecionar_email(lista_emails[0])

            mostrar_mensagem("Lista de e-mails atualizada e todos pré-selecionados.")
        except Exception as e:
            mostrar_mensagem(f"Erro ao atualizar lista de e-mails: {e}")
        finally:
            sessao.close()

    # ++ MOTORISTA ++ #
    def cadastrar_motorista():
        nome = entry_motorista.get().strip().upper()
        placa = entry_placa.get().strip().upper()
        if not nome or not placa:
            mostrar_mensagem('Preencha todos os campos.')
            return
        
        sessao = Session()
        try:
            motorista_existente = sessao.query(Motorista).filter_by(nome=nome).first()
            if motorista_existente:
                mostrar_mensagem('Motorista já cadastrado.')
                return
            novo_motorista = Motorista(nome=nome, placa=placa)
            sessao.add(novo_motorista)
            sessao.commit()
            mostrar_mensagem('Motorista cadastrado com sucesso.')
            atualizar_lista_motorista()
        finally:
            sessao.close()

    def atualizar_motorista():
        nome = entry_motorista.get().strip().upper()
        placa = entry_placa.get().strip().upper()
        if not nome or not placa:
            mostrar_mensagem('Preencha todos os campos.')
            return
        
        sessao = Session()
        try:
            motorista = sessao.query(Motorista).filter_by(nome=nome).first()
            if motorista:
                motorista.placa = placa
                sessao.commit()
                mostrar_mensagem('Placa alterada com sucesso.')
                atualizar_lista_motorista()
                return
        finally:
            sessao.close()

    def excluir_motorista():
        nome = entry_motorista.get().strip().upper()
        placa = entry_placa.get().strip().upper()
        if not nome or not placa:
            mostrar_mensagem('Preencha todos os campos.')
            return
        
        sessao = Session()
        try:
            motorista = sessao.query(Motorista).filter(Motorista.nome == nome, Motorista.placa == placa).first()
            if not motorista:
                mostrar_mensagem('Motorista ou Placa incorreto.')
                return
            else:
                sessao.delete(motorista)
                sessao.commit()
                mostrar_mensagem('Motorista removido com sucesso.')
                atualizar_lista_motorista()
                return
        finally:
            sessao.close()

    def mostrar_mensagem(texto):
        visor.configure(state="normal")
        visor.delete("1.0", "end")
        visor.insert("1.0", texto)
        visor.configure(state="disabled")

    def atualizar_lista_motorista():
        """Atualiza a lista de motoristas com checkboxes para seleção única."""
        # Limpa os elementos existentes na lista
        for widget in motorista_lista.winfo_children():
            widget.destroy()

        sessao = Session()
        try:
            lista_motoristas = sessao.query(Motorista).all()
            estados_dos_checkboxes = {}

            def selecionar_motorista_item(registro_motorista):
                """Preenche os campos com os dados do motorista selecionado."""
                entry_motorista.delete(0, "end")
                entry_motorista.insert(0, registro_motorista.nome)

                entry_placa.delete(0, "end")
                entry_placa.insert(0, registro_motorista.placa)

                mostrar_mensagem(f'Motorista "{registro_motorista.nome}" selecionado.')

            def ao_clicar_checkbox(registro_motorista, estado_checkbox):
                """Permite selecionar apenas um motorista por vez e atualiza os campos."""
                for outro_estado in estados_dos_checkboxes.values():
                    if outro_estado != estado_checkbox:
                        outro_estado.set(0)

                if estado_checkbox.get() == 1:
                    selecionar_motorista_item(registro_motorista)
                else:
                    entry_motorista.delete(0, "end")
                    entry_placa.delete(0, "end")

            # Cria um checkbox para cada motorista cadastrado
            for registro_motorista in lista_motoristas:
                estado_checkbox = ctk.IntVar(value=0)
                estados_dos_checkboxes[registro_motorista.id] = estado_checkbox

                checkbox_motorista = ctk.CTkCheckBox(
                    motorista_lista,
                    text=f"{registro_motorista.nome} - {registro_motorista.placa}",
                    variable=estado_checkbox,
                    onvalue=1,
                    offvalue=0,
                    command=lambda m=registro_motorista, e=estado_checkbox: ao_clicar_checkbox(m, e)
                )
                checkbox_motorista.pack(pady=2, padx=5, anchor="w")
        except Exception as e:
            mostrar_mensagem(f"Erro ao atualizar lista de motoristas: {e}")
        finally:
            sessao.close()

    # ++ FORNECEDOR ++ #
    def selecionar(valor):
        # Atualiza a variável principal
        selecionado.set(valor)

        # Força atualização visual manual dos checkboxes
        botao_filial.deselect() if valor != 'Filial' else botao_filial.select()
        botao_outros.deselect() if valor != 'Outros' else botao_outros.select()

    def selecionar_outros():
        if var_outros.get() == 1:
            texto.grid(row=1, column=2, sticky="nsew", padx=15, pady=25)
            var_filial.set(0)
        else:
            texto.grid_remove()

    def selecionar_filial():
        if var_filial.get() == 1:
            texto.grid_remove()
            var_outros.set(0)

    # ---------- CONFIGURAÇÃO INICIAL ----------
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Cadastro de Motoristas e Placas")
    app.geometry("672x900")

    # Configura o grid do app principal
    app.grid_rowconfigure(0, weight=1)  # janela_principal cresce
    app.grid_rowconfigure(1, weight=0)  # visor fica fixo
    app.grid_columnconfigure(0, weight=1)

    # ===== LAYOUT ===== #
    janela_principal = ctk.CTkFrame(app)
    janela_principal.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    # Configura o grid dentro do janela_principal
    janela_principal.grid_rowconfigure(0, weight=1)
    janela_principal.grid_rowconfigure(1, weight=1)
    janela_principal.grid_rowconfigure(2, weight=1)
    janela_principal.grid_rowconfigure(3, weight=1)
    janela_principal.grid_rowconfigure(4, weight=1)
    janela_principal.grid_columnconfigure(0, weight=1)
    janela_principal.grid_columnconfigure(1, weight=1)
    janela_principal.grid_columnconfigure(2, weight=1)
    janela_principal.grid_columnconfigure(3, weight=1)
    janela_principal.grid_columnconfigure(4, weight=1)
    
    # == E-MAIL == #
    janela_email_lista = ctk.CTkFrame(janela_principal)
    janela_email_lista.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    email_lista = ctk.CTkScrollableFrame(janela_email_lista, label_text='E-mails Cadastrados')
    email_lista.pack(fill='both', expand=True, padx=5, pady=5)

    janela_email_formulario = ctk.CTkFrame(janela_principal)
    janela_email_formulario.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    label_nome = ctk.CTkLabel(janela_email_formulario, text="Nome:")
    label_nome.grid(row=0, column=0, sticky="e", padx=5, pady=5)
    entry_nome = ctk.CTkEntry(janela_email_formulario, width=200)
    entry_nome.grid(row=0, column=1, padx=5, pady=5)

    label_email = ctk.CTkLabel(janela_email_formulario, text="E-mail:")
    label_email.grid(row=1, column=0, sticky="e", padx=5, pady=5)
    entry_email = ctk.CTkEntry(janela_email_formulario, width=200)
    entry_email.grid(row=1, column=1, padx=5, pady=5)

    frame_botoes_email = ctk.CTkFrame(janela_email_formulario, fg_color="transparent")
    frame_botoes_email.grid(row=2, column=0, columnspan=2, pady=10)

    botao_cadastrar_email = ctk.CTkButton(frame_botoes_email, text="Cadastrar", width=100, command=cadastrar_email)
    botao_cadastrar_email.grid(row=0, column=0, padx=10)
    botao_atualizar_email = ctk.CTkButton(frame_botoes_email, text="Atualizar", width=100, fg_color="orange", hover_color="#cc8400", command=atualizar_email)
    botao_atualizar_email.grid(row=0, column=1, padx=10)
    botao_excluir_email = ctk.CTkButton(frame_botoes_email, text="Excluir", width=100, fg_color="red", hover_color="#ff0000", command=excluir_email)
    botao_excluir_email.grid(row=0, column=2, padx=10)

    # == MOTORISTA == #
    janela_motorista_lista = ctk.CTkFrame(janela_principal)
    janela_motorista_lista.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    motorista_lista = ctk.CTkScrollableFrame(janela_motorista_lista, label_text='Motoristas Cadastrados')
    motorista_lista.pack(fill='both', expand=True, padx=5, pady=5)

    janela_motorista_formulario = ctk.CTkFrame(janela_principal)
    janela_motorista_formulario.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    label_motorista = ctk.CTkLabel(janela_motorista_formulario, text="Motorista:")
    label_motorista.grid(row=0, column=0, sticky="e", padx=5, pady=5)
    entry_motorista = ctk.CTkEntry(janela_motorista_formulario, width=200)
    entry_motorista.grid(row=0, column=1, padx=5, pady=5)

    label_placa = ctk.CTkLabel(janela_motorista_formulario, text="Placa:")
    label_placa.grid(row=1, column=0, sticky="e", padx=5, pady=5)
    entry_placa = ctk.CTkEntry(janela_motorista_formulario, width=200)
    entry_placa.grid(row=1, column=1, padx=5, pady=5)

    frame_botoes_motorista = ctk.CTkFrame(janela_motorista_formulario, fg_color="transparent")
    frame_botoes_motorista.grid(row=2, column=0, columnspan=2, pady=10)

    botao_cadastrar_motorista = ctk.CTkButton(frame_botoes_motorista, text="Cadastrar", width=100, command=botao_cadastrar_email)
    botao_cadastrar_motorista.grid(row=0, column=0, padx=10)
    botao_atualizar_motorista = ctk.CTkButton(frame_botoes_motorista, text="Atualizar", width=100, fg_color="orange", hover_color="#cc8400", command=atualizar_motorista)
    botao_atualizar_motorista.grid(row=0, column=1, padx=10)
    botao_excluir_motorista = ctk.CTkButton(frame_botoes_motorista, text="Excluir", width=100, fg_color="red", hover_color="#ff0000", command=excluir_motorista)
    botao_excluir_motorista.grid(row=0, column=2, padx=10)

    # == FORNECEDOR == #
    janela_fornecedor = ctk.CTkFrame(janela_principal)
    janela_fornecedor.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    # ---------- VARIÁVEL DE CONTROLE ----------
    selecionado = ctk.StringVar(value="Filial")
    var_filial = ctk.IntVar(value=1)

    valores = [str(i) for i in range(1,100)]
    quantidade = ctk.CTkComboBox(janela_fornecedor, values=valores, width=100, height=30)
    quantidade.grid(row=1, column=0, sticky="nsew", padx=50, pady=30)

    botao_filial = ctk.CTkCheckBox(janela_fornecedor, text='Filial', variable=var_filial, command=lambda: (selecionar('Filial'), selecionar_filial()))
    botao_filial.grid(row=1, column=1, sticky="nsew", padx=50, pady=30)
    var_outros = ctk.IntVar(value=0)
    botao_outros = ctk.CTkCheckBox(janela_fornecedor, text='Outros', variable=var_outros, command=lambda: (selecionar('Outros'), selecionar_outros()))
    botao_outros.grid(row=1, column=2, sticky="nsew", padx=50, pady=30)

    texto = ctk.CTkEntry(janela_fornecedor, placeholder_text='Digite aqui')
    texto.grid(row=1, column=2, sticky="nsew", padx=50, pady=30)
    texto.grid_remove()

    # == QUANTIDADE / ENVIAR == #
    janela_quantidade = ctk.CTkFrame(janela_principal)
    janela_quantidade.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    valores = [str(i) for i in range(1,100)]

    quantidade = ctk.CTkComboBox(janela_quantidade, values=valores, width=100, height=30)
    quantidade.grid(row=1, column=1, sticky="nsew", padx=50, pady=30)
    botao_enviar = ctk.CTkButton(janela_quantidade, text='Enviar')
    botao_enviar.grid(row=1, column=2, sticky="nsew", padx=50, pady=30)

    # == VISOR == #
    visor = ctk.CTkTextbox(app, height=60, width=500)
    visor.grid(row=1, column=0, pady=10, sticky="ew")
    visor.insert("1.0", "Cadastre um motorista para começar...")
    visor.configure(state="disabled")

    # ---------- EXECUÇÃO ----------
    botao_filial.select()
    atualizar_lista_email()
    atualizar_lista_motorista()
    app.mainloop()

import customtkinter as ctk
from functools import partial
from commands.visor_settings import set_visor
from pages.email_page import abrir_janela_email
from pages.motorista_page import abrir_janela_motorista
from pages.texto_page import confirmar_texto
from commands.email_settings import resetar_all_email
from commands.motorista_settings import lista_motorista_dashboard
from commands.dashboard_settings import selecionar_todos_emails, estado_checkbox_geral, selecionar_filial, selecionar_outros, aplicar_placeholder_combobox, salvar_dados, salvar_e_enviar, anexar_arquivos



def iniciar_programa():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("790x450")
    app.title("Automatização de E-mail")
    #app.iconbitmap(resource_path('icone.ico'))

    # Frame de cabeçalho (título visual)
    header = ctk.CTkFrame(app)
    header.pack(fill="x", padx=10, pady=10)
    # Label à esquerda
    titulo_esquerda = ctk.CTkLabel(header, text="Automatização de E-mail", font=("Arial", 14, "bold"))
    titulo_esquerda.pack(side="left", padx=10)
    # Label à direita
    titulo_direita = ctk.CTkLabel(header, text="Desenvolvido por Lauro Júnior", font=("Arial", 10), text_color="gray")
    titulo_direita.pack(side="right", padx=10)

    # Configura o grid do app principal
    app.grid_rowconfigure(0, weight=1)  # janela_principal cresce
    app.grid_rowconfigure(1, weight=0)  # visor fica fixo
    app.grid_columnconfigure(0, weight=1)

    # ===== LAYOUT ===== #
    janela_principal = ctk.CTkFrame(app)
    janela_principal.pack(fill="both", expand=True, padx=20)

    # JANELA QUADRO #
    janela_quadro = ctk.CTkFrame(janela_principal, width=150, height=150, corner_radius=10)
    janela_quadro.grid(row=0, column=0, sticky='nw', padx=20, pady=20)

    botao_email = ctk.CTkButton(janela_quadro, text="E-MAIL", width=125, height=30, fg_color="#7070ff", hover_color="#0000ff", font=('Arial',14,'bold'), corner_radius=5, command=lambda:(resetar_all_email(all_email_var, all_email), abrir_janela_email()))
    botao_email.grid(row=0, column=0, padx=10, pady=10)
    botao_motorista = ctk.CTkButton(janela_quadro, text="MOTORISTA", width=125, height=30, fg_color="#5050ff", hover_color="#0000ff", font=('Arial',14,'bold'), corner_radius=5, command=partial(abrir_janela_motorista, on_close=lambda: lista_motorista_dashboard(janela_motorista_lista, motorista)))
    botao_motorista.grid(row=1, column=0, padx=10, pady=10)
    botao_texto = ctk.CTkButton(janela_quadro, text="TEXTO", width=125, height=30, fg_color="#3030ff", hover_color="#0000ff", font=('Arial',14,'bold'), corner_radius=5, command=lambda: confirmar_texto())
    botao_texto.grid(row=2, column=0, padx=10, pady=10)

    # JANELA MOTORISTA #
    janela_motorista_frame = ctk.CTkFrame(janela_principal, width=150, height=150, corner_radius=10)
    janela_motorista_frame.grid(row=0, column=1, sticky='nw', padx=0, pady=20)

    janela_motorista_lista = ctk.CTkScrollableFrame(janela_motorista_frame, label_text='MOTORISTAS CADASTRADOS', width=150, height=150)
    janela_motorista_lista.pack(padx=5, pady=5)   
    janela_motorista_lista._label.configure(font=('Arial', 10, 'bold'))

    motorista = {"motorista_id": None}
    lista_motorista_dashboard(janela_motorista_lista, motorista)

    # JANELA BOTÕES #
    janela_botoes = ctk.CTkFrame(janela_principal, width=150, height=150, corner_radius=10, fg_color='transparent')
    janela_botoes.grid(row=0, column=2, sticky='nw', padx=20, pady=20)
    
    all_email_var = ctk.IntVar(value=estado_checkbox_geral())
    all_email = ctk.CTkCheckBox(janela_botoes, text='SELECIONAR TODOS OS E-MAILS', font=('Arial',14,'bold'), variable=all_email_var, command=lambda:selecionar_todos_emails(all_email_var.get()))
    all_email.grid(row=0, column=0, sticky='nw', padx=5, pady=7)
    filial = ctk.CTkCheckBox(janela_botoes, text='FILIAL', font=('Arial',14,'bold'), command=lambda:selecionar_filial(filial, outros, entry_outros))
    filial.grid(row=1, column=0, sticky='nw', padx=5, pady=7)
    filial.select()  # Começa selecionado
    outros = ctk.CTkCheckBox(janela_botoes, text='OUTROS', font=('Arial',14,'bold'), command=lambda:selecionar_outros(filial, outros, entry_outros))
    outros.grid(row=1, column=0, sticky='nw', padx=(100,0), pady=7)
    entry_outros = ctk.CTkEntry(janela_botoes, placeholder_text='Digite aqui...')
    entry_outros.grid(row=1, column=0, sticky='nw', padx=(210,0), pady=7)
    entry_outros.grid_forget()  # Começa desabilitado
    
    numero = ctk.CTkComboBox(janela_botoes, values=[str(i) for i in range(1, 11)], width=80)
    numero.grid(row=2, column=0, sticky='nw', padx=5, pady=7)
    aplicar_placeholder_combobox(numero, 'N° ...')
    numero_carreta = ctk.CTkLabel(janela_botoes, text='NÚMERO DA CARRETA', font=('Arial',14,'bold'))
    numero_carreta.grid(row=2, column=0, sticky='nw', padx=(100,0), pady=7)
    valor = ctk.CTkEntry(janela_botoes, placeholder_text='R$ 0,00', width=80)
    valor.grid(row=3, column=0, sticky='nw', padx=5, pady=7)
    valor_frete = ctk.CTkLabel(janela_botoes, text='VALOR DO FRETE', font=('Arial',14,'bold'))
    valor_frete.grid(row=3, column=0, sticky='nw', padx=(100,0), pady=7)

    anexar_arquivo = ctk.CTkButton(janela_principal, text="ANEXAR", width=125, height=30, fg_color="#ff9900", hover_color="#ffaa00", font=('Arial',14,'bold'), corner_radius=5, command=lambda: anexar_arquivos())
    anexar_arquivo.grid(row=0, column=2, padx=(240,30), pady=(150,10))
    encerrar = ctk.CTkButton(janela_principal, text="ENCERRAR", width=125, height=30, fg_color="#cc0000", hover_color="#ff0000", font=('Arial',14,'bold'), corner_radius=5)
    encerrar.grid(row=0, column=0, padx=10, pady=(150,10))
    enviar = ctk.CTkButton(janela_principal, text="ENVIAR E-MAIL", width=125, height=30, fg_color="#00cc00", hover_color="#00ff00", font=('Arial',14,'bold'), corner_radius=5, command=lambda:(salvar_dados(motorista, filial, entry_outros, numero, valor), salvar_e_enviar(motorista, filial, entry_outros, numero, valor)))
    enviar.grid(row=0, column=2, padx=(240,30), pady=(240,10))

    footer = ctk.CTkFrame(app)
    footer.pack(fill="x", padx=10, pady=10)

    # == VISOR == #
    visor = ctk.CTkTextbox(footer, height=60, width=750)
    visor.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
    visor.insert("1.0", "Cadastre um motorista para começar...")
    visor.configure(state="disabled")
    set_visor(visor)

    # # Label à esquerda
    # titulo_esquerda = ctk.CTkLabel(footer, text="Automatização de E-mail", font=("Arial", 14, "bold"))
    # titulo_esquerda.pack(side="left", padx=10)
    # # Label à direita
    # titulo_direita = ctk.CTkLabel(footer, text="Desenvolvido por Lauro Júnior", font=("Arial", 10), text_color="gray")
    # titulo_direita.pack(side="right", padx=10)
    app.mainloop()
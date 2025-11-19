import customtkinter as ctk

def iniciar_programa():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("550x280")
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

    botao_email = ctk.CTkButton(janela_quadro, text="E-MAIL", width=125, height=30, fg_color="#7070ff", hover_color="#0000ff", font=('Arial',14,'bold'), corner_radius=5)
    botao_email.grid(row=0, column=0, padx=10, pady=10)
    botao_motorista = ctk.CTkButton(janela_quadro, text="MOTORISTA", width=125, height=30, fg_color="#5050ff", hover_color="#0000ff", font=('Arial',14,'bold'), corner_radius=5)
    botao_motorista.grid(row=1, column=0, padx=10, pady=10)
    botao_texto = ctk.CTkButton(janela_quadro, text="TEXTO", width=125, height=30, fg_color="#3030ff", hover_color="#0000ff", font=('Arial',14,'bold'), corner_radius=5)
    botao_texto.grid(row=2, column=0, padx=10, pady=10)

    # JANELA MOTORISTA #
    janela_motorista_lista = ctk.CTkFrame(janela_principal, width=150, height=150, corner_radius=10)
    janela_motorista_lista.grid(row=0, column=1, sticky='nw', padx=0, pady=20)
    
    motorista_lista = ctk.CTkScrollableFrame(janela_motorista_lista, label_text='MOTORISTAS CADASTRADOS', width=150, height=150)
    motorista_lista.pack(padx=5, pady=5)   
    motorista_lista._label.configure(font=('Arial', 10, 'bold'))

    

    # JANELA BOTÕES #
    janela_botoes = ctk.CTkFrame(janela_principal, width=150, height=150, corner_radius=10, fg_color='transparent')
    janela_botoes.grid(row=0, column=2, sticky='nw', padx=20, pady=20)

    all_email = ctk.CTkCheckBox(janela_botoes, text='SELECIONAR TODOS OS E-MAILS', font=('Arial',14,'bold'))
    all_email.grid(row=0, column=0, sticky='nw', padx=5, pady=5)
    filial = ctk.CTkCheckBox(janela_botoes, text='FILIAL', font=('Arial',14,'bold'))
    filial.grid(row=1, column=0, sticky='nw', padx=5, pady=5)
    outros = ctk.CTkCheckBox(janela_botoes, text='OUTROS', font=('Arial',14,'bold'))
    outros.grid(row=1, column=0, sticky='nw', padx=(100,0), pady=5)
    digite = ctk.CTkEntry(janela_botoes, placeholder_text='Digite aqui...')
    digite.grid(row=1, column=0, sticky='nw', padx=(210,0), pady=5)
    numero = ctk.CTkComboBox(janela_botoes, values=[str(i) for i in range(1, 11)], width=80)
    numero.grid(row=2, column=0, sticky='nw', padx=5, pady=5)
    numero_carreta = ctk.CTkLabel(janela_botoes, text='NÚMERO DA CARRETA', font=('Arial',14,'bold'))
    numero_carreta.grid(row=2, column=0, sticky='nw', padx=(100,0), pady=5)
    valor = ctk.CTkEntry(janela_botoes, placeholder_text='R$ 0,00', width=80)
    valor.grid(row=3, column=0, sticky='nw', padx=5, pady=5)
    valor_frete = ctk.CTkLabel(janela_botoes, text='VALOR DO FRETE', font=('Arial',14,'bold'))
    valor_frete.grid(row=3, column=0, sticky='nw', padx=(100,0), pady=5)

    anexar_arquivo = ctk.CTkButton(janela_principal, text="ANEXAR", width=125, height=30, fg_color="#ff9900", hover_color="#ffaa00", font=('Arial',14,'bold'), corner_radius=5)
    anexar_arquivo.grid(row=0, column=2, padx=(240,10), pady=(150,10))
    encerrar = ctk.CTkButton(janela_principal, text="ENCERRAR", width=125, height=30, fg_color="#cc0000", hover_color="#ff0000", font=('Arial',14,'bold'), corner_radius=5)
    encerrar.grid(row=0, column=0, padx=10, pady=(150,10))
    enviar = ctk.CTkButton(janela_principal, text="ENVIAR E-MAIL", width=125, height=30, fg_color="#00cc00", hover_color="#00ff00", font=('Arial',14,'bold'), corner_radius=5)
    enviar.grid(row=0, column=2, padx=(240,10), pady=(240,10))

    footer = ctk.CTkFrame(app)
    footer.pack(fill="x", padx=10, pady=10)
    # # Label à esquerda
    # titulo_esquerda = ctk.CTkLabel(footer, text="Automatização de E-mail", font=("Arial", 14, "bold"))
    # titulo_esquerda.pack(side="left", padx=10)
    # # Label à direita
    # titulo_direita = ctk.CTkLabel(footer, text="Desenvolvido por Lauro Júnior", font=("Arial", 10), text_color="gray")
    # titulo_direita.pack(side="right", padx=10)
    
    app.mainloop()
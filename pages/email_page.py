import customtkinter as ctk
from commands.email_settings import cadastrar_email, atualizar_email, excluir_email, atualizar_lista_email
from commands.visor_settings import set_visor


# ++ E-MAIL ++ #
def abrir_janela_email():
    janela_principal = ctk.CTkToplevel()
    janela_principal.geometry("635x365")
    janela_principal.title("Gerenciar E-mails")
    janela_principal.grab_set()
    
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

    botao_cadastrar_email = ctk.CTkButton(frame_botoes_email, text="Cadastrar", width=100, fg_color="green", hover_color="#33cc33", command=lambda: cadastrar_email(entry_nome, entry_email, email_lista))
    botao_cadastrar_email.grid(row=0, column=0, padx=10)
    botao_atualizar_email = ctk.CTkButton(frame_botoes_email, text="Atualizar", width=100, fg_color="orange", hover_color="#cc8400", command=lambda: atualizar_email(entry_nome, entry_email, email_lista))
    botao_atualizar_email.grid(row=0, column=1, padx=10)
    botao_excluir_email = ctk.CTkButton(frame_botoes_email, text="Excluir", width=100, fg_color="red", hover_color="#ff5050", command=lambda: excluir_email(entry_nome, entry_email, email_lista))
    botao_excluir_email.grid(row=0, column=2, padx=10)

    # == VISOR == #
    visor = ctk.CTkTextbox(janela_principal, height=60, width=500)
    visor.grid(row=1, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
    visor.insert("1.0", "Cadastre um motorista para começar...")
    visor.configure(state="disabled")
    set_visor(visor)

    # 🔁 carrega automaticamente ao abrir
    atualizar_lista_email(email_lista, entry_nome, entry_email)


        
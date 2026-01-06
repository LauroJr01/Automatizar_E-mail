import customtkinter as ctk
from commands.motorista_settings import cadastrar_motorista, atualizar_motorista, excluir_motorista, atualizar_lista_motorista
from commands.visor_settings import set_visor

def abrir_janela_motorista(on_close=None):
    janela_principal = ctk.CTkToplevel()
    janela_principal.geometry("635x365")
    janela_principal.title("Gerenciar Motoristas")
    janela_principal.grab_set()

    # 🔔 intercepta o fechamento da janela
    def fechar():
        if on_close:
            on_close()
        janela_principal.destroy()

    janela_principal.protocol("WM_DELETE_WINDOW", fechar)

    janela_motorista_lista = ctk.CTkFrame(janela_principal)
    janela_motorista_lista.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    motorista_lista = ctk.CTkScrollableFrame(janela_motorista_lista, label_text='Motoristas Cadastrados')
    motorista_lista.pack(fill='both', expand=True, padx=5, pady=5)

    janela_motorista_formulario = ctk.CTkFrame(janela_principal)
    janela_motorista_formulario.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

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

    botao_cadastrar_motorista = ctk.CTkButton(frame_botoes_motorista, text="Cadastrar", width=100, fg_color="green", hover_color="#33cc33", command=lambda: cadastrar_motorista(entry_motorista, entry_placa, motorista_lista))
    botao_cadastrar_motorista.grid(row=0, column=0, padx=10)
    botao_atualizar_motorista = ctk.CTkButton(frame_botoes_motorista, text="Atualizar", width=100, fg_color="orange", hover_color="#cc8400", command=lambda: atualizar_motorista(entry_motorista, entry_placa, motorista_lista))
    botao_atualizar_motorista.grid(row=0, column=1, padx=10)
    botao_excluir_motorista = ctk.CTkButton(frame_botoes_motorista, text="Excluir", width=100, fg_color="red", hover_color="#ff5050", command=lambda: excluir_motorista(entry_motorista, entry_placa, motorista_lista))
    botao_excluir_motorista.grid(row=0, column=2, padx=10)

    # == VISOR == #
    visor = ctk.CTkTextbox(janela_principal, height=60, width=500)
    visor.grid(row=1, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
    visor.insert("1.0", "Cadastre um motorista para começar...")
    visor.configure(state="disabled")
    set_visor(visor)

    # 🔁 carrega automaticamente ao abrir
    atualizar_lista_motorista(entry_motorista, entry_placa, motorista_lista)


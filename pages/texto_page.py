import customtkinter as ctk
from commands import visor_settings
from commands.texto_settings import carregar_template, salvar_template
import tkinter.messagebox as msg

def abrir_janela_texto():
    janela_principal = ctk.CTkToplevel()
    janela_principal.geometry("570x620")
    janela_principal.title("Editar Modelo de E-mail")
    janela_principal.grab_set()

    janela_principal.grid_columnconfigure(0, weight=1)

    # == Assunto == 
    assunto_label = ctk.CTkLabel(janela_principal, text="Assunto do E-mail")
    assunto_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

    assunto_entry = ctk.CTkEntry(janela_principal)
    assunto_entry.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")

    # == Corpo ==
    corpo_label = ctk.CTkLabel(janela_principal, text="Corpo do E-mail (HTML)")
    corpo_label.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="nsew")

    corpo_textbox = ctk.CTkTextbox(janela_principal, height=200)
    corpo_textbox.grid(row=3, column=0, padx=10, pady=(0, 10), sticky="nsew")

    # == Resposta ==
    resposta_label = ctk.CTkLabel(janela_principal, text="Texto de Resposta Automática")
    resposta_label.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="nsew")

    resposta_textbox = ctk.CTkTextbox(janela_principal, height=120)
    resposta_textbox.grid(row=5, column=0, padx=10, pady=(0, 10), sticky="nsew")


    # == Botão Salvar ==
    botao_salvar = ctk.CTkButton(janela_principal, text="Salvar", width=120, fg_color="green", hover_color="#33cc33", command=lambda: salvar_template(assunto_entry, corpo_textbox, resposta_textbox))
    botao_salvar.grid(row=6, column=0, pady=(0, 10))

    # == VISOR ==
    visor = ctk.CTkTextbox(janela_principal, height=60)
    visor.grid(row=7, column=0, padx=10, pady=10, sticky="ew")
    visor.insert("1.0", "Edite o modelo do e-mail/resposta e clique em Salvar.")
    visor.configure(state="disabled")
    
    visor_anterior = visor_settings.visor_global
    visor_settings.set_visor(visor)

    def ao_fechar_janela():
        visor_settings.set_visor(visor_anterior)

        # libera o grab corretamente
        janela_principal.grab_release()
        janela_principal.destroy()

    janela_principal.protocol("WM_DELETE_WINDOW", ao_fechar_janela)

    # 🔁 carrega automaticamente ao abrir
    carregar_template(assunto_entry, corpo_textbox, resposta_textbox)

def confirmar_texto():
    if msg.askyesno(title="Confirmação", message="Alterar o texto do e-mail pode impactar envios futuros. \nDeseja continuar?"):
        abrir_janela_texto()
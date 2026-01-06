import customtkinter as ctk
from commands.visor_settings import set_visor
from commands.texto_settings import carregar_template, salvar_template
import tkinter.messagebox as msg

def abrir_janela_texto():
    janela_principal = ctk.CTkToplevel()
    janela_principal.geometry("570x495")
    janela_principal.title("Editar Modelo de E-mail")
    janela_principal.grab_set()

    janela_principal.grid_columnconfigure(0, weight=1)

    assunto_label = ctk.CTkLabel(janela_principal, text="Assunto do E-mail")
    assunto_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

    assunto_entry = ctk.CTkEntry(janela_principal)
    assunto_entry.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")

    corpo_label = ctk.CTkLabel(janela_principal, text="Corpo do E-mail (HTML)")
    corpo_label.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="nsew")

    corpo_textbox = ctk.CTkTextbox(janela_principal, height=250)
    corpo_textbox.grid(row=3, column=0, padx=10, pady=(0, 10), sticky="nsew")

    botao_salvar = ctk.CTkButton(janela_principal, text="Salvar", width=120, fg_color="green", hover_color="#33cc33", command=lambda: salvar_template(assunto_entry, corpo_textbox))
    botao_salvar.grid(row=4, column=0, pady=(0, 10))

    # == VISOR ==
    visor = ctk.CTkTextbox(janela_principal, height=60)
    visor.grid(row=5, column=0, padx=10, pady=10, sticky="ew")
    visor.insert("1.0", "Edite o modelo do e-mail e clique em Salvar.")
    visor.configure(state="disabled")
    set_visor(visor)

    # 🔁 carrega automaticamente ao abrir
    carregar_template(assunto_entry, corpo_textbox)

def confirmar_texto():
    if msg.askyesno(title="Confirmação", message="Alterar o texto do e-mail pode impactar envios futuros. \nDeseja continuar?"):
        abrir_janela_texto()
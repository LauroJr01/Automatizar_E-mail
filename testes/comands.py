import customtkinter as ctk
from database.setup_db import Session, Motorista, Email
from sqlalchemy.exc import IntegrityError
from tkinter import messagebox

# ++ E-MAIL ++ #
def cadastrar_email():
    def salvar_email():
        novo_email = email_entry.get().strip()
        if novo_email:
            session = Session()
            email_obj = Email(endereco=novo_email)
            session.add(email_obj)
            try:
                session.commit()
                messagebox.showinfo("Sucesso", f"E-mail '{novo_email}' cadastrado com sucesso!")
                email_entry.delete(0, ctk.END)
            except IntegrityError:
                session.rollback()
                messagebox.showerror("Erro", f"E-mail '{novo_email}' já está cadastrado.")
            finally:
                session.close()
        else:
            messagebox.showwarning("Atenção", "Por favor, insira um e-mail válido.")

    janela_email = ctk.CTkToplevel()
    janela_email.geometry("400x200")
    janela_email.title("Cadastrar E-mail")

    label = ctk.CTkLabel(janela_email, text="Insira o novo e-mail:", font=("Arial", 12))
    label.pack(pady=10)

    email_entry = ctk.CTkEntry(janela_email, width=300)
    email_entry.pack(pady=10)

    salvar_button = ctk.CTkButton(janela_email, text="Salvar", command=salvar_email)
    salvar_button.pack(pady=10)
        
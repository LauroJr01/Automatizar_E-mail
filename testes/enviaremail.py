import win32com.client as win32
import customtkinter as ctk
import sqlite3

def enviar_email():
    # Criar a integração com o outlook
    outlook = win32.Dispatch('outlook.application')

    # Criar um email
    email = outlook.CreateItem(0)

    # Configurar as informações do seu e-mail
    email.To = 'jr.reis1@hotmail.com'
    email.CC = 'jr.reis1@hotmail.com'
    email.Subject = 'Assunto (Teste)'


    # email.Body = 'Corpo do E-mail'
    email.HTMLBody = '''
    <p>Olá Lauro, aqui é o código Python</p>

    <p>O faturamento da loja foi de R$1.500</p>
    <p>Vendemos 10 produtos</p>
    <p>O ticket Médio foi de R$150</p>

    <p>Abs,</p>
    <p>Lauro</p>
    '''
    email.Display()  # Para abrir o e-mail antes de enviar
    #email.Send()
    print('E-mail enviado')

       

enviar_email()
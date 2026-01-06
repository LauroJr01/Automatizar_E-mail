# # import customtkinter as ctk

# # ctk.set_appearance_mode("dark")
# # ctk.set_default_color_theme("blue")

# # app = ctk.CTk()
# # app.title("Cadastro de Motoristas e Placas")
# # app.geometry("600x400")

# # motoristas = {}  # {nome: placa}
# # selecionado = ctk.StringVar()  # variável controladora dos radio buttons

# # # --- FUNÇÕES --- #
# # def cadastrar_motorista():
# #     nome = entry_motorista.get().strip()
# #     placa = entry_placa.get().strip()

# #     if not nome or not placa:
# #         mostrar_mensagem("Preencha nome e placa antes de cadastrar.")
# #         return

# #     if nome in motoristas:
# #         mostrar_mensagem(f"{nome} já está cadastrado. Use 'Atualizar' para editar.")
# #         return

# #     motoristas[nome] = placa
# #     atualizar_lista()
# #     mostrar_mensagem(f"{nome} cadastrado com sucesso!")

# #     limpar_campos()

# # def atualizar_motorista():
# #     nome = entry_motorista.get().strip()
# #     placa = entry_placa.get().strip()

# #     if not nome or not placa:
# #         mostrar_mensagem("Preencha nome e placa antes de atualizar.")
# #         return

# #     if nome not in motoristas:
# #         mostrar_mensagem("Motorista não encontrado para atualização.")
# #         return

# #     motoristas[nome] = placa
# #     atualizar_lista()
# #     mostrar_mensagem(f"{nome} atualizado com sucesso!")

# # def atualizar_lista():
# #     for widget in frame_lista.winfo_children():
# #         widget.destroy()

# #     for nome in motoristas:
# #         rb = ctk.CTkRadioButton(
# #             frame_lista,
# #             text=nome,
# #             variable=selecionado,
# #             value=nome,
# #             command=lambda n=nome: preencher_campos(n),
# #         )
# #         rb.pack(anchor="w", pady=2)

# # def preencher_campos(nome):
# #     entry_motorista.delete(0, "end")
# #     entry_motorista.insert(0, nome)
# #     entry_placa.delete(0, "end")
# #     entry_placa.insert(0, motoristas[nome])

# # def limpar_campos():
# #     entry_motorista.delete(0, "end")
# #     entry_placa.delete(0, "end")

# # def mostrar_mensagem(texto):
# #     visor.configure(state="normal")
# #     visor.delete("1.0", "end")
# #     visor.insert("1.0", texto)
# #     visor.configure(state="disabled")

# # # --- LAYOUT --- #

# # frame_main = ctk.CTkFrame(app)
# # frame_main.pack(fill="both", expand=True, padx=20, pady=20)

# # # Lista de motoristas (lado esquerdo)
# # frame_lista = ctk.CTkFrame(frame_main, width=200)
# # frame_lista.grid(row=0, column=0, padx=10, pady=10, sticky="nswe")

# # # Formulário (lado direito)
# # frame_form = ctk.CTkFrame(frame_main)
# # frame_form.grid(row=0, column=1, padx=10, pady=10, sticky="nswe")

# # label_motorista = ctk.CTkLabel(frame_form, text="Motorista:")
# # label_motorista.grid(row=0, column=0, sticky="e", padx=5, pady=5)
# # entry_motorista = ctk.CTkEntry(frame_form, width=200)
# # entry_motorista.grid(row=0, column=1, padx=5, pady=5)

# # label_placa = ctk.CTkLabel(frame_form, text="Placa:")
# # label_placa.grid(row=1, column=0, sticky="e", padx=5, pady=5)
# # entry_placa = ctk.CTkEntry(frame_form, width=200)
# # entry_placa.grid(row=1, column=1, padx=5, pady=5)

# # # Botões lado a lado
# # frame_botoes = ctk.CTkFrame(frame_form, fg_color="transparent")
# # frame_botoes.grid(row=2, column=0, columnspan=2, pady=10)

# # botao_cadastrar = ctk.CTkButton(frame_botoes, text="Cadastrar", width=100, command=cadastrar_motorista)
# # botao_cadastrar.grid(row=0, column=0, padx=10)

# # botao_atualizar = ctk.CTkButton(frame_botoes, text="Atualizar", width=100, fg_color="orange", hover_color="#cc8400", command=atualizar_motorista)
# # botao_atualizar.grid(row=0, column=1, padx=10)

# # # Visor
# # visor = ctk.CTkTextbox(app, height=60, width=500)
# # visor.pack(pady=10)
# # visor.insert("1.0", "Cadastre um motorista para começar...")
# # visor.configure(state="disabled")

# # app.mainloop()






# # import customtkinter as ctk
# # import sqlite3

# # # ---------- CONFIGURAÇÃO INICIAL ----------
# # ctk.set_appearance_mode("dark")
# # ctk.set_default_color_theme("blue")

# # app = ctk.CTk()
# # app.title("Cadastro de Motoristas e Placas")
# # app.geometry("600x420")

# # # ---------- BANCO DE DADOS ----------
# # def inicializar_banco():
# #     conexao = sqlite3.connect("motoristas.db")
# #     cursor = conexao.cursor()
# #     cursor.execute("""
# #         CREATE TABLE IF NOT EXISTS motoristas (
# #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# #             nome TEXT UNIQUE NOT NULL,
# #             placa TEXT NOT NULL
# #         )
# #     """)
# #     conexao.commit()
# #     conexao.close()

# # def inserir_motorista(nome, placa):
# #     conexao = sqlite3.connect("motoristas.db")
# #     cursor = conexao.cursor()
# #     try:
# #         cursor.execute("INSERT INTO motoristas (nome, placa) VALUES (?, ?)", (nome, placa))
# #         conexao.commit()
# #     except sqlite3.IntegrityError:
# #         mostrar_mensagem(f"Motorista '{nome}' já cadastrado.")
# #     conexao.close()

# # def atualizar_motorista_db(nome, placa):
# #     conexao = sqlite3.connect("motoristas.db")
# #     cursor = conexao.cursor()
# #     cursor.execute("UPDATE motoristas SET placa = ? WHERE nome = ?", (placa, nome))
# #     conexao.commit()
# #     conexao.close()

# # def excluir_motorista():
# #     nome = selecionado.get()
# #     if not nome:
# #         mostrar_mensagem("Selecione um motorista para excluir.")
# #         return

# #     conexao = sqlite3.connect("motoristas.db")
# #     cursor = conexao.cursor()
# #     cursor.execute("DELETE FROM motoristas WHERE nome = ?", (nome,))
# #     conexao.commit()
# #     conexao.close()

# #     # Atualiza a lista de motoristas e limpa campos
# #     carregar_motoristas()
# #     limpar_campos()
# #     mostrar_mensagem(f"Motorista '{nome}' excluído com sucesso!")


# # def buscar_todos_motoristas():
# #     conexao = sqlite3.connect("motoristas.db")
# #     cursor = conexao.cursor()
# #     cursor.execute("SELECT nome, placa FROM motoristas")
# #     dados = cursor.fetchall()
# #     conexao.close()
# #     return {nome: placa for nome, placa in dados}

# # # ---------- INTERFACE ----------
# # motoristas = {}
# # selecionado = ctk.StringVar()

# # def cadastrar_motorista():
# #     nome = entry_motorista.get().strip()
# #     placa = entry_placa.get().strip()

# #     if not nome or not placa:
# #         mostrar_mensagem("Preencha nome e placa antes de cadastrar.")
# #         return

# #     inserir_motorista(nome, placa)
# #     carregar_motoristas()
# #     mostrar_mensagem(f"{nome} cadastrado com sucesso!")
# #     limpar_campos()

# # def atualizar_motorista():
# #     nome = entry_motorista.get().strip()
# #     placa = entry_placa.get().strip()

# #     if not nome or not placa:
# #         mostrar_mensagem("Preencha nome e placa antes de atualizar.")
# #         return

# #     if nome not in motoristas:
# #         mostrar_mensagem("Motorista não encontrado.")
# #         return

# #     atualizar_motorista_db(nome, placa)
# #     carregar_motoristas()
# #     mostrar_mensagem(f"{nome} atualizado com sucesso!")

# # def carregar_motoristas():
# #     global motoristas
# #     motoristas = buscar_todos_motoristas()

# #     for widget in frame_lista.winfo_children():
# #         widget.destroy()

# #     for nome in motoristas:
# #         rb = ctk.CTkRadioButton(
# #             frame_lista,
# #             text=nome,
# #             variable=selecionado,
# #             value=nome,
# #             command=lambda n=nome: preencher_campos(n),
# #         )
# #         rb.pack(anchor="w", pady=2)

# # def preencher_campos(nome):
# #     entry_motorista.delete(0, "end")
# #     entry_motorista.insert(0, nome)
# #     entry_placa.delete(0, "end")
# #     entry_placa.insert(0, motoristas[nome])

# # def limpar_campos():
# #     entry_motorista.delete(0, "end")
# #     entry_placa.delete(0, "end")

# # def mostrar_mensagem(texto):
# #     visor.configure(state="normal")
# #     visor.delete("1.0", "end")
# #     visor.insert("1.0", texto)
# #     visor.configure(state="disabled")

# # # ---------- LAYOUT ----------
# # frame_main = ctk.CTkFrame(app)
# # frame_main.pack(fill="both", expand=True, padx=20, pady=20)

# # frame_lista = ctk.CTkFrame(frame_main, width=200)
# # frame_lista.grid(row=0, column=0, padx=10, pady=10, sticky="nswe")

# # frame_form = ctk.CTkFrame(frame_main)
# # frame_form.grid(row=0, column=1, padx=10, pady=10, sticky="nswe")

# # label_motorista = ctk.CTkLabel(frame_form, text="Motorista:")
# # label_motorista.grid(row=0, column=0, sticky="e", padx=5, pady=5)
# # entry_motorista = ctk.CTkEntry(frame_form, width=200)
# # entry_motorista.grid(row=0, column=1, padx=5, pady=5)

# # label_placa = ctk.CTkLabel(frame_form, text="Placa:")
# # label_placa.grid(row=1, column=0, sticky="e", padx=5, pady=5)
# # entry_placa = ctk.CTkEntry(frame_form, width=200)
# # entry_placa.grid(row=1, column=1, padx=5, pady=5)

# # frame_botoes = ctk.CTkFrame(frame_form, fg_color="transparent")
# # frame_botoes.grid(row=2, column=0, columnspan=2, pady=10)

# # botao_cadastrar = ctk.CTkButton(frame_botoes, text="Cadastrar", width=100, command=cadastrar_motorista)
# # botao_cadastrar.grid(row=0, column=0, padx=10)

# # botao_atualizar = ctk.CTkButton(frame_botoes, text="Atualizar", width=100, fg_color="orange", hover_color="#cc8400", command=atualizar_motorista)
# # botao_atualizar.grid(row=0, column=1, padx=10)

# # botao_atualizar = ctk.CTkButton(frame_botoes, text="Excluir", width=100, fg_color="red", hover_color="#ff0000", command=excluir_motorista)
# # botao_atualizar.grid(row=0, column=2, padx=10)

# # visor = ctk.CTkTextbox(app, height=60, width=500)
# # visor.pack(pady=10)
# # visor.insert("1.0", "Cadastre um motorista para começar...")
# # visor.configure(state="disabled")

# # # ---------- EXECUÇÃO ----------
# # inicializar_banco()
# # carregar_motoristas()
# # app.mainloop()


# # import customtkinter as ctk
# # import sqlite3

# # # === CONFIGURAÇÕES INICIAIS ===
# # ctk.set_appearance_mode("dark")
# # ctk.set_default_color_theme("blue")

# # # === BANCO DE DADOS ===
# # def criar_tabela():
# #     conn = sqlite3.connect("dados.db")
# #     c = conn.cursor()
# #     c.execute("""
# #         CREATE TABLE IF NOT EXISTS motoristas (
# #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# #             nome TEXT NOT NULL,
# #             placa TEXT NOT NULL
# #         )
# #     """)
# #     conn.commit()
# #     conn.close()

# # def inserir_motorista(nome, placa):
# #     conn = sqlite3.connect("dados.db")
# #     c = conn.cursor()
# #     c.execute("INSERT INTO motoristas (nome, placa) VALUES (?, ?)", (nome, placa))
# #     conn.commit()
# #     conn.close()

# # def listar_motoristas():
# #     conn = sqlite3.connect("dados.db")
# #     c = conn.cursor()
# #     c.execute("SELECT id, nome, placa FROM motoristas")
# #     dados = c.fetchall()
# #     conn.close()
# #     return dados

# # def atualizar_motorista(id_motorista, nome, placa):
# #     conn = sqlite3.connect("dados.db")
# #     c = conn.cursor()
# #     c.execute("UPDATE motoristas SET nome=?, placa=? WHERE id=?", (nome, placa, id_motorista))
# #     conn.commit()
# #     conn.close()

# # def excluir_motorista(id_motorista):
# #     conn = sqlite3.connect("dados.db")
# #     c = conn.cursor()
# #     c.execute("DELETE FROM motoristas WHERE id=?", (id_motorista,))
# #     conn.commit()
# #     conn.close()

# # # === INTERFACE ===
# # class App(ctk.CTk):
# #     def __init__(self):
# #         super().__init__()
# #         self.title("Cadastro de Motoristas")
# #         self.geometry("700x500")
# #         self.resizable(False, False)

# #         criar_tabela()

# #         # Campos de entrada
# #         self.nome_entry = ctk.CTkEntry(self, placeholder_text="Nome do Motorista")
# #         self.nome_entry.grid(row=0, column=0, padx=10, pady=10)

# #         self.placa_entry = ctk.CTkEntry(self, placeholder_text="Placa do Veículo")
# #         self.placa_entry.grid(row=0, column=1, padx=10, pady=10)

# #         self.cadastrar_btn = ctk.CTkButton(self, text="Cadastrar", command=self.cadastrar_motorista)
# #         self.cadastrar_btn.grid(row=0, column=2, padx=10, pady=10)

# #         self.atualizar_btn = ctk.CTkButton(self, text="Atualizar", command=self.atualizar_lista)
# #         self.atualizar_btn.grid(row=0, column=3, padx=10, pady=10)

# #         # Frame dos checkboxes
# #         self.frame_lista = ctk.CTkScrollableFrame(self, width=650, height=300, label_text="Motoristas Cadastrados")
# #         self.frame_lista.grid(row=1, column=0, columnspan=4, padx=20, pady=20)

# #         # Campos de edição (após seleção)
# #         self.edit_nome = ctk.CTkEntry(self, placeholder_text="Editar nome")
# #         self.edit_nome.grid(row=2, column=0, padx=10, pady=5)

# #         self.edit_placa = ctk.CTkEntry(self, placeholder_text="Editar placa")
# #         self.edit_placa.grid(row=2, column=1, padx=10, pady=5)

# #         self.salvar_btn = ctk.CTkButton(self, text="Salvar Alterações", command=self.salvar_edicao)
# #         self.salvar_btn.grid(row=2, column=2, padx=10, pady=5)

# #         self.excluir_btn = ctk.CTkButton(self, text="Excluir", command=self.excluir_selecionado)
# #         self.excluir_btn.grid(row=2, column=3, padx=10, pady=5)

# #         self.motoristas_vars = []
# #         self.motoristas_ids = []
# #         self.motorista_selecionado = None

# #         self.atualizar_lista()

# #     def cadastrar_motorista(self):
# #         nome = self.nome_entry.get().strip()
# #         placa = self.placa_entry.get().strip()
# #         if nome and placa:
# #             inserir_motorista(nome, placa)
# #             self.nome_entry.delete(0, "end")
# #             self.placa_entry.delete(0, "end")
# #             self.atualizar_lista()

# #     def atualizar_lista(self):
# #         for widget in self.frame_lista.winfo_children():
# #             widget.destroy()

# #         self.motoristas_vars.clear()
# #         self.motoristas_ids.clear()

# #         motoristas = listar_motoristas()

# #         for i, (id_motorista, nome, placa) in enumerate(motoristas):
# #             var = ctk.StringVar(value="")
# #             rb = ctk.CTkRadioButton(
# #                 self.frame_lista,
# #                 text=f"{nome} — {placa}",
# #                 variable=var,
# #                 value="selected",
# #                 command=lambda i=id_motorista, n=nome, p=placa: self.selecionar_motorista(i, n, p)
# #             )
# #             rb.pack(anchor="w", padx=10, pady=5)
# #             self.motoristas_vars.append(var)
# #             self.motoristas_ids.append(id_motorista)

# #     def selecionar_motorista(self, id_motorista, nome, placa):
# #         self.motorista_selecionado = id_motorista
# #         self.edit_nome.delete(0, "end")
# #         self.edit_nome.insert(0, nome)
# #         self.edit_placa.delete(0, "end")
# #         self.edit_placa.insert(0, placa)

# #     def salvar_edicao(self):
# #         if self.motorista_selecionado:
# #             novo_nome = self.edit_nome.get().strip()
# #             nova_placa = self.edit_placa.get().strip()
# #             if novo_nome and nova_placa:
# #                 atualizar_motorista(self.motorista_selecionado, novo_nome, nova_placa)
# #                 self.atualizar_lista()

# #     def excluir_selecionado(self):
# #         if self.motorista_selecionado:
# #             excluir_motorista(self.motorista_selecionado)
# #             self.motorista_selecionado = None
# #             self.edit_nome.delete(0, "end")
# #             self.edit_placa.delete(0, "end")
# #             self.atualizar_lista()

# # if __name__ == "__main__":
# #     app = App()
# #     app.mainloop()


# import customtkinter as ctk
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import declarative_base, sessionmaker
# from sqlalchemy.exc import IntegrityError

# # ---------- CONFIGURAÇÃO INICIAL ----------
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("blue")

# app = ctk.CTk()
# app.title("Cadastro de Motoristas e Placas")
# app.geometry("640x420")

# # ---------- BANCO DE DADOS ----------
# Base = declarative_base()

# class Motorista(Base):
#     __tablename__ = "motoristas"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     nome = Column(String, unique=True, nullable=False)
#     placa = Column(String, nullable=False)

# # Criação do engine e da sessão
# engine = create_engine("sqlite:///motoristas.db", echo=False)
# Session = sessionmaker(bind=engine)
# session = Session()

# def inicializar_banco():
#     Base.metadata.create_all(engine)

# def inserir_motorista(nome, placa):
#     novo = Motorista(nome=nome, placa=placa)
#     try:
#         session.add(novo)
#         session.commit()
#     except IntegrityError:
#         session.rollback()
#         mostrar_mensagem(f"Motorista '{nome}' já cadastrado.")

# def atualizar_motorista_db(nome, placa):
#     motorista = session.query(Motorista).filter_by(nome=nome).first()
#     if motorista:
#         motorista.placa = placa
#         session.commit()

# def excluir_motorista():
#     nome = selecionado.get()
#     if not nome:
#         mostrar_mensagem("Selecione um motorista para excluir.")
#         return

#     motorista = session.query(Motorista).filter_by(nome=nome).first()
#     if motorista:
#         session.delete(motorista)
#         session.commit()
#         carregar_motoristas()
#         limpar_campos()
#         mostrar_mensagem(f"Motorista '{nome}' excluído com sucesso!")
#     else:
#         mostrar_mensagem("Motorista não encontrado.")

# def buscar_todos_motoristas():
#     motoristas_db = session.query(Motorista).all()
#     return {m.nome: m.placa for m in motoristas_db}

# # ---------- INTERFACE ----------
# motoristas = {}
# selecionado = ctk.StringVar()

# def cadastrar_motorista():
#     nome = entry_motorista.get().strip()
#     placa = entry_placa.get().strip()

#     if not nome or not placa:
#         mostrar_mensagem("Preencha nome e placa antes de cadastrar.")
#         return

#     inserir_motorista(nome, placa)
#     carregar_motoristas()
#     mostrar_mensagem(f"{nome} cadastrado com sucesso!")
#     limpar_campos()

# def atualizar_motorista():
#     nome = entry_motorista.get().strip()
#     placa = entry_placa.get().strip()

#     if not nome or not placa:
#         mostrar_mensagem("Preencha nome e placa antes de atualizar.")
#         return

#     if nome not in motoristas:
#         mostrar_mensagem("Motorista não encontrado.")
#         return

#     atualizar_motorista_db(nome, placa)
#     carregar_motoristas()
#     mostrar_mensagem(f"{nome} atualizado com sucesso!")

# def carregar_motoristas():
#     global motoristas
#     motoristas = buscar_todos_motoristas()

#     for widget in frame_lista.winfo_children():
#         widget.destroy()

#     for nome in motoristas:
#         rb = ctk.CTkRadioButton(
#             frame_lista,
#             text=nome,
#             variable=selecionado,
#             value=nome,
#             command=lambda n=nome: preencher_campos(n),
#         )
#         rb.pack(anchor="w", pady=2)

# def preencher_campos(nome):
#     entry_motorista.delete(0, "end")
#     entry_motorista.insert(0, nome)
#     entry_placa.delete(0, "end")
#     entry_placa.insert(0, motoristas[nome])

# def limpar_campos():
#     entry_motorista.delete(0, "end")
#     entry_placa.delete(0, "end")

# def mostrar_mensagem(texto):
#     visor.configure(state="normal")
#     visor.delete("1.0", "end")
#     visor.insert("1.0", texto)
#     visor.configure(state="disabled")

# # ---------- LAYOUT ----------
# frame_main = ctk.CTkFrame(app)
# frame_main.pack(fill="both", expand=True, padx=20, pady=20)

# frame_lista = ctk.CTkFrame(frame_main, width=200)
# frame_lista.grid(row=0, column=0, padx=10, pady=10, sticky="nswe")

# frame_form = ctk.CTkFrame(frame_main)
# frame_form.grid(row=0, column=1, padx=10, pady=10, sticky="nswe")

# label_motorista = ctk.CTkLabel(frame_form, text="Motorista:")
# label_motorista.grid(row=0, column=0, sticky="e", padx=5, pady=5)
# entry_motorista = ctk.CTkEntry(frame_form, width=200)
# entry_motorista.grid(row=0, column=1, padx=5, pady=5)

# label_placa = ctk.CTkLabel(frame_form, text="Placa:")
# label_placa.grid(row=1, column=0, sticky="e", padx=5, pady=5)
# entry_placa = ctk.CTkEntry(frame_form, width=200)
# entry_placa.grid(row=1, column=1, padx=5, pady=5)

# frame_botoes = ctk.CTkFrame(frame_form, fg_color="transparent")
# frame_botoes.grid(row=2, column=0, columnspan=2, pady=10)

# botao_cadastrar = ctk.CTkButton(frame_botoes, text="Cadastrar", width=100, command=cadastrar_motorista)
# botao_cadastrar.grid(row=0, column=0, padx=10)

# botao_atualizar = ctk.CTkButton(frame_botoes, text="Atualizar", width=100, fg_color="orange", hover_color="#cc8400", command=atualizar_motorista)
# botao_atualizar.grid(row=0, column=1, padx=10)

# botao_excluir = ctk.CTkButton(frame_botoes, text="Excluir", width=100, fg_color="red", hover_color="#ff0000", command=excluir_motorista)
# botao_excluir.grid(row=0, column=2, padx=10)

# visor = ctk.CTkTextbox(app, height=60, width=500)
# visor.pack(pady=10)
# visor.insert("1.0", "Cadastre um motorista para começar...")
# visor.configure(state="disabled")

# # ---------- EXECUÇÃO ----------
# inicializar_banco()
# carregar_motoristas()
# app.mainloop()

# import customtkinter as ctk

# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("blue")

# app = ctk.CTk()
# app.title("Pinguinho Toggle")
# app.geometry("300x200")

# ativo = False

# def toggle_pingo():
#     global ativo
#     ativo = not ativo
#     pingo.configure(fg_color="#00FF7F" if ativo else "#555555")  # verde ou cinza

# # Cria o "pinguinho"
# pingo = ctk.CTkButton(
#     app,
#     text="",           # sem texto
#     width=15,          # pequenino
#     height=15,
#     corner_radius=50,  # bem redondo
#     fg_color="#555555",  # cor inicial (desligado)
#     hover_color="#777777",
#     command=toggle_pingo
# )
# pingo.pack(pady=60)

# app.mainloop()

# import customtkinter as ctk

# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("blue")

# # --- Função base pra criar janelas ---
# def criar_janela(titulo, conteudo_func):
#     janela = ctk.CTk()
#     janela.title(titulo)
#     janela.geometry("300x200")
#     conteudo_func(janela)
#     janela.mainloop()

# # --- 1. CTkButton ---
# def janela_ctkbutton(master):
#     def acao():
#         label.configure(text="Botão clicado!")
#     label = ctk.CTkLabel(master, text="Clique no botão")
#     label.pack(pady=10)
#     botao = ctk.CTkButton(master, text="Clique aqui", command=acao)
#     botao.pack(pady=10)

# # --- 2. CTkSwitch ---
# def janela_ctkswitch(master):
#     def alternar():
#         estado = "Ligado" if switch.get() else "Desligado"
#         label.configure(text=f"Estado: {estado}")
#     switch = ctk.CTkSwitch(master, text="Ativar modo turbo", command=alternar)
#     switch.pack(pady=10)
#     label = ctk.CTkLabel(master, text="Estado: Desligado")
#     label.pack(pady=10)

# # --- 3. CTkCheckBox ---
# def janela_ctkcheckbox(master):
#     def verificar():
#         label.configure(text=f"Marcado: {checkbox.get()}")
#     checkbox = ctk.CTkCheckBox(master, text="Aceito os termos", command=verificar)
#     checkbox.pack(pady=10)
#     label = ctk.CTkLabel(master, text="Marcado: 0")
#     label.pack(pady=10)

# # --- 4. CTkRadioButton ---
# def janela_ctkradiobutton(master):
#     var = ctk.StringVar(value="A")
#     def mostrar():
#         label.configure(text=f"Selecionado: {var.get()}")
#     radio1 = ctk.CTkRadioButton(master, text="Opção A", variable=var, value="A", command=mostrar)
#     radio2 = ctk.CTkRadioButton(master, text="Opção B", variable=var, value="B", command=mostrar)
#     radio1.pack(pady=5)
#     radio2.pack(pady=5)
#     label = ctk.CTkLabel(master, text="Selecionado: A")
#     label.pack(pady=10)

# # --- 5. CTkSegmentedButton ---
# def janela_ctksegmented(master):
#     def selecionar(valor):
#         label.configure(text=f"Selecionado: {valor}")
#     seg = ctk.CTkSegmentedButton(master, values=["Dia", "Semana", "Mês"], command=selecionar)
#     seg.pack(pady=10)
#     label = ctk.CTkLabel(master, text="Selecionado: Nenhum")
#     label.pack(pady=10)

# # --- 6. CTkOptionMenu ---
# def janela_ctkoptionmenu(master):
#     def escolher(valor):
#         label.configure(text=f"Escolhido: {valor}")
#     menu = ctk.CTkOptionMenu(master, values=["Pequeno", "Médio", "Grande"], command=escolher)
#     menu.pack(pady=10)
#     label = ctk.CTkLabel(master, text="Escolhido: Nenhum")
#     label.pack(pady=10)

# # --- 7. CTkButton minimalista (bolinha) ---
# def janela_botao_bolinha(master):
#     def toggle():
#         estado[0] = not estado[0]
#         cor = "#00FF00" if estado[0] else "#FF0000"
#         botao.configure(fg_color=cor)
#     estado = [False]
#     botao = ctk.CTkButton(
#         master,
#         text="",
#         width=40,
#         height=40,
#         fg_color="#FF0000",
#         hover_color="#880000",
#         corner_radius=20,
#         command=toggle
#     )
#     botao.pack(pady=50)

# # --- Chamadas individuais ---
# # Escolha qual janela quer abrir trocando a função abaixo 👇

# criar_janela("CTkButton", janela_ctkbutton)
# criar_janela("CTkSwitch", janela_ctkswitch)
# criar_janela("CTkCheckBox", janela_ctkcheckbox)
# criar_janela("CTkRadioButton", janela_ctkradiobutton)
# criar_janela("CTkSegmentedButton", janela_ctksegmented)
# criar_janela("CTkOptionMenu", janela_ctkoptionmenu)
# criar_janela("Botão Bolinha", janela_botao_bolinha)


# import customtkinter as ctk
# from PIL import Image

# # ---------- CONFIGURAÇÃO INICIAL ----------
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("blue")

# app = ctk.CTk()
# app.title("Galeria de Botões - CustomTkinter")
# app.geometry("600x500")

# # ---------- ABAS ----------
# abas = ctk.CTkTabview(app)
# abas.pack(fill="both", expand=True, padx=20, pady=20)

# abas.add("Básicos")
# abas.add("Alternáveis")
# abas.add("Estilosos")
# abas.add("Extras")

# # ----------------------------------------------------------
# # 🧩 ABA 1: BOTÕES BÁSICOS
# # ----------------------------------------------------------

# def acao_padrao():
#     label1.configure(text="Botão clicado!")

# label1 = ctk.CTkLabel(abas.tab("Básicos"), text="CTkButton simples")
# label1.pack(pady=10)
# botao_padrao = ctk.CTkButton(abas.tab("Básicos"), text="Clique aqui", command=acao_padrao)
# botao_padrao.pack(pady=10)

# # Botão com ícone
# try:
#     img = Image.open("icone.png")  # Coloque um ícone na pasta
#     icone = ctk.CTkImage(light_image=img, dark_image=img, size=(20, 20))
# except:
#     icone = None

# botao_icon = ctk.CTkButton(
#     abas.tab("Básicos"),
#     text="Salvar",
#     image=icone,
#     compound="left",
#     fg_color="#1E90FF",
#     hover_color="#4682B4",
#     corner_radius=10,
# )
# botao_icon.pack(pady=10)

# # ----------------------------------------------------------
# # ⚙️ ABA 2: BOTÕES ALTERNÁVEIS (Switch, Checkbox, Radio, Toggle)
# # ----------------------------------------------------------

# # CTkSwitch
# def alternar():
#     estado = "Ligado" if switch.get() else "Desligado"
#     label2.configure(text=f"Switch: {estado}")

# switch = ctk.CTkSwitch(abas.tab("Alternáveis"), text="Modo turbo", command=alternar)
# switch.pack(pady=10)
# label2 = ctk.CTkLabel(abas.tab("Alternáveis"), text="Switch: Desligado")
# label2.pack(pady=5)

# # Checkbox
# def verificar():
#     label3.configure(text=f"Checkbox: {checkbox.get()}")

# checkbox = ctk.CTkCheckBox(abas.tab("Alternáveis"), text="Aceito os termos", command=verificar)
# checkbox.pack(pady=10)
# label3 = ctk.CTkLabel(abas.tab("Alternáveis"), text="Checkbox: 0")
# label3.pack(pady=5)

# # RadioButton
# var = ctk.StringVar(value="A")
# def mostrar():
#     label4.configure(text=f"Selecionado: {var.get()}")

# radio1 = ctk.CTkRadioButton(abas.tab("Alternáveis"), text="Opção A", variable=var, value="A", command=mostrar)
# radio2 = ctk.CTkRadioButton(abas.tab("Alternáveis"), text="Opção B", variable=var, value="B", command=mostrar)
# radio1.pack(pady=5)
# radio2.pack(pady=5)
# label4 = ctk.CTkLabel(abas.tab("Alternáveis"), text="Selecionado: A")
# label4.pack(pady=5)

# # Toggle (muda cor ao clicar)
# estado_toggle = [False]
# def toggle():
#     estado_toggle[0] = not estado_toggle[0]
#     cor = "#00C851" if estado_toggle[0] else "#D32F2F"
#     texto = "Ativo" if estado_toggle[0] else "Desativado"
#     botao_toggle.configure(text=texto, fg_color=cor)

# botao_toggle = ctk.CTkButton(
#     abas.tab("Alternáveis"),
#     text="Desativado",
#     fg_color="#D32F2F",
#     hover_color="#B71C1C",
#     width=120,
#     command=toggle
# )
# botao_toggle.pack(pady=10)

# # ----------------------------------------------------------
# # 💎 ABA 3: BOTÕES ESTILOSOS
# # ----------------------------------------------------------

# # Transparente
# botao_transp = ctk.CTkButton(
#     abas.tab("Estilosos"),
#     text="Transparente",
#     fg_color="transparent",
#     border_width=1,
#     border_color="#5A5A5A",
#     hover_color="#2A2A2A"
# )
# botao_transp.pack(pady=10)

# # Fantasma
# botao_fantasma = ctk.CTkButton(
#     abas.tab("Estilosos"),
#     text="Cancelar",
#     fg_color="transparent",
#     border_width=2,
#     border_color="#FF5555",
#     text_color="#FF5555",
#     hover_color="#661111"
# )
# botao_fantasma.pack(pady=10)

# # Circular (ícone)
# try:
#     img2 = Image.open("editar.png")
#     icone2 = ctk.CTkImage(light_image=img2, dark_image=img2, size=(25, 25))
# except:
#     icone2 = None

# botao_circular = ctk.CTkButton(
#     abas.tab("Estilosos"),
#     text="",
#     image=icone2,
#     width=50,
#     height=50,
#     corner_radius=25,
#     fg_color="#FF9500",
#     hover_color="#FFB84D"
# )
# botao_circular.pack(pady=10)

# # Gradiente simulado
# def grad_hover(e=None):
#     botao_grad.configure(fg_color="#6A5ACD")
# def grad_leave(e=None):
#     botao_grad.configure(fg_color="#9370DB")

# botao_grad = ctk.CTkButton(
#     abas.tab("Estilosos"),
#     text="Gradiente",
#     fg_color="#9370DB",
#     text_color="white",
#     width=120,
#     height=40,
#     corner_radius=15
# )
# botao_grad.bind("<Enter>", grad_hover)
# botao_grad.bind("<Leave>", grad_leave)
# botao_grad.pack(pady=10)

# # ----------------------------------------------------------
# # 🧭 ABA 4: EXTRAS (Segmented, OptionMenu, Feedback, Tooltip)
# # ----------------------------------------------------------

# # SegmentedButton
# def selecionar(valor):
#     label_seg.configure(text=f"Selecionado: {valor}")

# seg = ctk.CTkSegmentedButton(abas.tab("Extras"), values=["Dia", "Semana", "Mês"], command=selecionar)
# seg.pack(pady=10)
# label_seg = ctk.CTkLabel(abas.tab("Extras"), text="Selecionado: Nenhum")
# label_seg.pack(pady=5)

# # OptionMenu
# def escolher(valor):
#     label_menu.configure(text=f"Escolhido: {valor}")

# menu = ctk.CTkOptionMenu(abas.tab("Extras"), values=["Pequeno", "Médio", "Grande"], command=escolher)
# menu.pack(pady=10)
# label_menu = ctk.CTkLabel(abas.tab("Extras"), text="Escolhido: Nenhum")
# label_menu.pack(pady=5)

# # Feedback visual
# def animar():
#     botao_feedback.configure(fg_color="#00FF7F")
#     abas.tab("Extras").after(150, lambda: botao_feedback.configure(fg_color="#00C851"))

# botao_feedback = ctk.CTkButton(
#     abas.tab("Extras"),
#     text="Enviar",
#     fg_color="#00C851",
#     hover_color="#009E4F",
#     command=animar
# )
# botao_feedback.pack(pady=10)

# # Tooltip simples
# tooltip = ctk.CTkLabel(abas.tab("Extras"), text="Clique para enviar dados", fg_color="#222", text_color="white")
# tooltip.place_forget()

# def mostrar_tooltip(event):
#     tooltip.place(x=event.x_root - app.winfo_x() - 80, y=event.y_root - app.winfo_y() - 100)

# def esconder_tooltip(event):
#     tooltip.place_forget()

# botao_tooltip = ctk.CTkButton(abas.tab("Extras"), text="Botão com Tooltip")
# botao_tooltip.bind("<Enter>", mostrar_tooltip)
# botao_tooltip.bind("<Leave>", esconder_tooltip)
# botao_tooltip.pack(pady=10)

# # ----------------------------------------------------------
# app.mainloop()

# import customtkinter as ctk

# # ---------- CONFIGURAÇÃO ----------
# ctk.set_appearance_mode("dark")
# ctk.set_default_color_theme("blue")

# app = ctk.CTk()
# app.title("RadioButton Personalizado")
# app.geometry("400x300")

# # ---------- VARIÁVEL DE CONTROLE ----------
# modo = ctk.StringVar(value="Nenhum")

# # ---------- FUNÇÃO DE SELEÇÃO ----------
# def selecionar(valor):
#     label_resultado.configure(text=f"Selecionado: {valor}")

#     for botao in botoes:
#         if botao.cget("value") == valor:
#             botao.configure(
#                 fg_color="#007BFF",  # azul destaque
#                 hover_color="#339CFF",
#                 text_color="white",
#                 border_width_checked=5
#             )
#         else:
#             botao.configure(
#                 fg_color="#2A2A2A",
#                 hover_color="#3A3A3A",
#                 text_color="#BFBFBF"
#             )

# # ---------- CONTAINER ----------
# frame = ctk.CTkFrame(app, corner_radius=15)
# frame.pack(padx=20, pady=30, fill="x")

# titulo = ctk.CTkLabel(frame, text="Escolha o modo:", font=("Segoe UI", 16, "bold"))
# titulo.pack(pady=10)

# # ---------- BOTÕES PERSONALIZADOS ----------
# botoes = []

# radio1 = ctk.CTkRadioButton(
#     frame,
#     text="Modo Padrão",
#     variable=modo,
#     value="Padrão",
#     border_width_checked=6,
#     border_width_unchecked=2,
#     fg_color="#2A2A2A",
#     hover_color="#3A3A3A",
#     text_color="#BFBFBF",
#     font=("Segoe UI", 13, "bold"),
#     command=lambda: selecionar("Padrão")
# )
# radio1.pack(pady=6, anchor="w", padx=40)
# botoes.append(radio1)

# radio2 = ctk.CTkRadioButton(
#     frame,
#     text="Modo Escuro",
#     variable=modo,
#     value="Escuro",
#     border_width_checked=6,
#     border_width_unchecked=2,
#     fg_color="#2A2A2A",
#     hover_color="#3A3A3A",
#     text_color="#BFBFBF",
#     font=("Segoe UI", 13, "bold"),
#     command=lambda: selecionar("Escuro")
# )
# radio2.pack(pady=6, anchor="w", padx=40)
# botoes.append(radio2)

# radio3 = ctk.CTkRadioButton(
#     frame,
#     text="Modo Claro",
#     variable=modo,
#     value="Claro",
#     border_width_checked=6,
#     border_width_unchecked=2,
#     fg_color="#2A2A2A",
#     hover_color="#3A3A3A",
#     text_color="#BFBFBF",
#     font=("Segoe UI", 13, "bold"),
#     command=lambda: selecionar("Claro")
# )
# radio3.pack(pady=6, anchor="w", padx=40)
# botoes.append(radio3)

# # ---------- LABEL DE RESULTADO ----------
# label_resultado = ctk.CTkLabel(app, text="Selecionado: Nenhum", font=("Segoe UI", 14))
# label_resultado.pack(pady=20)

# app.mainloop()

# import customtkinter as ctk

# # Janela principal
# ctk.set_appearance_mode("dark")
# janela = ctk.CTk()
# janela.title("Exemplo RadioButton")
# janela.geometry("300x200")

# # Variável compartilhada entre os RadioButtons
# opcao = ctk.StringVar(value="opcao1")  # <- define o padrão (a opção selecionada)

# # Criação dos RadioButtons
# radio1 = ctk.CTkRadioButton(
#     janela, text="Opção 1", variable=opcao, value="opcao1"
# )
# radio1.pack(pady=10)

# radio2 = ctk.CTkRadioButton(
#     janela, text="Opção 2", variable=opcao, value="opcao2"
# )
# radio2.pack(pady=10)

# # Função para mostrar a opção selecionada
# def mostrar_opcao():
#     print("Selecionado:", opcao.get())

# botao = ctk.CTkButton(janela, text="Ver seleção", command=mostrar_opcao)
# botao.pack(pady=20)

# janela.mainloop()

# import customtkinter as ctk

# ctk.set_appearance_mode("dark")
# janela = ctk.CTk()
# janela.geometry("300x200")

# opcao = ctk.StringVar(value="")

# def selecionar(valor):
#     opcao.set(valor)
#     print("Selecionado:", valor)

# check1 = ctk.CTkCheckBox(
#     janela,
#     text="Opção 1",
#     variable=opcao,
#     onvalue="opcao1",
#     offvalue="",
#     command=lambda: selecionar("opcao1"),
#     checkbox_width=25,
#     checkbox_height=25,
#     corner_radius=50  # 50 deixa redondo como radio button
# )
# check1.pack(pady=10)

# check2 = ctk.CTkCheckBox(
#     janela,
#     text="Opção 2",
#     variable=opcao,
#     onvalue="opcao2",
#     offvalue="",
#     command=lambda: selecionar("opcao2"),
#     checkbox_width=25,
#     checkbox_height=25,
#     corner_radius=50
# )
# check2.pack(pady=10)

# janela.mainloop()

# import customtkinter as ctk

# ctk.set_appearance_mode("dark")
# app = ctk.CTk()
# app.geometry("300x200")

# # Variável compartilhada entre todos os checkboxes
# opcao = ctk.StringVar(value="A")

# def mostrar_opcao():
#     print("Selecionado:", opcao.get())

# check1 = ctk.CTkCheckBox(
#     app,
#     text="Opção A",
#     variable=opcao,
#     onvalue="A",
#     offvalue="",
#     command=mostrar_opcao,
#     checkbox_width=25,
#     checkbox_height=25,
#     corner_radius=50  # deixa redondinho, estilo radio
# )
# check1.pack(pady=5)

# check2 = ctk.CTkCheckBox(
#     app,
#     text="Opção B",
#     variable=opcao,
#     onvalue="B",
#     offvalue="",
#     command=mostrar_opcao,
#     checkbox_width=25,
#     checkbox_height=25,
#     corner_radius=50
# )
# check2.pack(pady=5)

# check3 = ctk.CTkCheckBox(
#     app,
#     text="Opção C",
#     variable=opcao,
#     onvalue="C",
#     offvalue="",
#     command=mostrar_opcao,
#     checkbox_width=25,
#     checkbox_height=25,
#     corner_radius=50
# )
# check3.pack(pady=5)

# app.mainloop()

# import customtkinter as ctk

# ctk.set_appearance_mode("dark")
# app = ctk.CTk()
# app.geometry("300x200")

# # Criamos uma variável que guarda o nome da opção selecionada
# selecionado = ctk.StringVar(value="")

# def selecionar(valor):
#     # Atualiza a variável principal
#     selecionado.set(valor)

#     # Força atualização visual manual dos checkboxes
#     check_a.deselect() if valor != "A" else check_a.select()
#     check_b.deselect() if valor != "B" else check_b.select()
#     check_c.deselect() if valor != "C" else check_c.select()

#     print("Selecionado:", selecionado.get())

# check_a = ctk.CTkCheckBox(app, text="Opção A", command=lambda: selecionar("A"))
# check_a.pack(pady=5)
# check_b = ctk.CTkCheckBox(app, text="Opção B", command=lambda: selecionar("B"))
# check_b.pack(pady=5)
# check_c = ctk.CTkCheckBox(app, text="Opção C", command=lambda: selecionar("C"))
# check_c.pack(pady=5)

# # Define a opção inicial
# selecionar("A")

# app.mainloop()


# import customtkinter as ctk

# ctk.set_appearance_mode("dark")

# def selecionar_outros():
#     if var_outros.get() == 1:
#         texto.grid(row=1, column=2, sticky="nsew", padx=50, pady=30)
#     else:
#         texto.grid_remove()  # Esconde o campo se desmarcar

# janela_fornecedor = ctk.CTk()
# janela_fornecedor.geometry("500x200")

# # Variável que guarda o estado do checkbox
# var_outros = ctk.IntVar(value=0)

# # CheckBox "Outros"
# botao_outros = ctk.CTkCheckBox(
#     janela_fornecedor,
#     text='Outros',
#     variable=var_outros,
#     command=selecionar_outros
# )
# botao_outros.grid(row=1, column=1, sticky="nsew", padx=50, pady=30)

# # Campo de texto (começa oculto)
# texto = ctk.CTkEntry(janela_fornecedor)
# texto.grid(row=1, column=2, sticky="nsew", padx=50, pady=30)
# texto.grid_remove()

# janela_fornecedor.mainloop()


# import customtkinter as ctk

# app = ctk.CTk()
# app.geometry("300x200")

# valores = ["10", "20", "30", "40"]

# combo = ctk.CTkComboBox(app, values=valores)
# combo.set("Selecione ou digite")
# combo.pack(pady=20)

# app.mainloop()

# import customtkinter as ctk

# app = ctk.CTk()
# app.geometry("300x250")

# valores = [str(i) for i in range(1, 100)]

# # Campo principal
# entrada = ctk.CTkEntry(app, width=120)
# entrada.pack(pady=(30, 0))

# # Frame rolável que simula o dropdown
# frame_dropdown = ctk.CTkScrollableFrame(app, width=120, height=100)  # altura = quantos itens quer ver
# frame_dropdown.pack_forget()  # começa escondido

# # Adiciona botões com os valores
# for v in valores:
#     botao = ctk.CTkButton(frame_dropdown, text=v, width=100, command=lambda val=v: (
#         entrada.delete(0, 'end'),
#         entrada.insert(0, val),
#         frame_dropdown.pack_forget()
#     ))
#     botao.pack(pady=1)

# # Abre/fecha o dropdown ao clicar na entrada
# def toggle_dropdown(event):
#     if frame_dropdown.winfo_ismapped():
#         frame_dropdown.pack_forget()
#     else:
#         frame_dropdown.pack(pady=5)

# entrada.bind("<Button-1>", toggle_dropdown)

# app.mainloop()

# import customtkinter
# class MyScrollableCheckboxFrame(customtkinter.CTkScrollableFrame):
#     def __init__(self, master, title, values):
#         super().__init__(master, label_text=title)
#         self.grid_columnconfigure(0, weight=1)
#         self.values = values
#         self.checkboxes = []

#         for i, value in enumerate(self.values):
#             checkbox = customtkinter.CTkCheckBox(self, text=value)
#             checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
#             self.checkboxes.append(checkbox)

#     def get(self):
#         checked_checkboxes = []
#         for checkbox in self.checkboxes:
#             if checkbox.get() == 1:
#                 checked_checkboxes.append(checkbox.cget("text"))
#         return checked_checkboxes
# class App(customtkinter.CTk):
#     def __init__(self):
#         super().__init__()

#         self.title("my app")
#         self.geometry("400x220")
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_rowconfigure(0, weight=1)

#         values = ["value 1", "value 2", "value 3", "value 4", "value 5", "value 6"]
#         self.scrollable_checkbox_frame = MyScrollableCheckboxFrame(self, title="Values", values=values)
#         self.scrollable_checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

#         self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
#         self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

#     def button_callback(self):
#         print("checkbox_frame:", self.checkbox_frame.get())
#         print("radiobutton_frame:", self.radiobutton_frame.get())

# app = App()
# app.mainloop()

import customtkinter as ctk

# janela = ctk.CTk()
# janela.geometry("300x300")

# for i in range(5):
#     item_frame = ctk.CTkFrame(janela)
#     item_frame.pack(fill="x", padx=10, pady=5)

#     label = ctk.CTkLabel(item_frame, text=f"Item {i+1}")
#     label.pack(side="left", padx=5)

#     checkbox1 = ctk.CTkCheckBox(item_frame, text="")
#     checkbox1.pack(side="right", padx=5)

#     checkbox2 = ctk.CTkCheckBox(item_frame, text="")
#     checkbox2.pack(side="right", padx=5)

# janela.mainloop()


import win32com.client as win32

def enviar_email(destinatario, assunto, corpo):
    outlook = win32.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)

    mail.To = destinatario
    mail.CC = "jr.reis1@hotmail.com"
    mail.Subject = assunto
    mail.Body = corpo

    mail.Display()

enviar_email(
    "jr.reis1@hotmail.com",
    "Teste win32com",
    "Email enviado via Outlook Desktop usando win32com"
)

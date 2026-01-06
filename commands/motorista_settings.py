import customtkinter as ctk
from database.setup_db import Session, Motorista
from commands.visor_settings import mostrar_mensagem

def cadastrar_motorista(entry_motorista, entry_placa, motorista_lista):
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
            atualizar_lista_motorista(entry_motorista, entry_placa, motorista_lista)
        finally:
            sessao.close()

def atualizar_motorista(entry_motorista, entry_placa, motorista_lista):
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
            atualizar_lista_motorista(entry_motorista, entry_placa, motorista_lista)
            return
    finally:
        sessao.close()

def excluir_motorista(entry_motorista, entry_placa, motorista_lista):
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
            atualizar_lista_motorista(entry_motorista, entry_placa, motorista_lista)
            return
    finally:
        sessao.close()

def atualizar_lista_motorista(entry_motorista, entry_placa, motorista_lista):
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

def lista_motorista_dashboard(motorista_lista, selecionado):
    """Atualiza a lista de motoristas no dashboard com seleção única."""

    for widget in motorista_lista.winfo_children():
        widget.destroy()

    sessao = Session()
    try:
        lista_motoristas = sessao.query(Motorista).all()
        estados_dos_checkboxes = {}

        def ao_clicar_checkbox(registro_motorista, estado_checkbox):
            for outro_estado in estados_dos_checkboxes.values():
                if outro_estado != estado_checkbox:
                    outro_estado.set(0)

            if estado_checkbox.get() == 1:
                selecionado["motorista_id"] = registro_motorista.id
            else:
                selecionado["motorista_id"] = None

            mostrar_mensagem(f"Selecionado agora: {registro_motorista.nome} | {registro_motorista.placa}")

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
    return {"motorista_id": None}


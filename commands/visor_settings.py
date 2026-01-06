visor_global = None

def set_visor(visor):
    global visor_global
    visor_global = visor

def mostrar_mensagem(texto):
    if visor_global is None:
        print("Visor ainda não conectado!")
        return

    visor_global.configure(state="normal")
    visor_global.delete("1.0", "end")
    visor_global.insert("1.0", texto)
    visor_global.configure(state="disabled")

# def mostrar_mensagem(texto):
#         visor.configure(state="normal")
#         visor.delete("1.0", "end")
#         visor.insert("1.0", texto)
#         visor.configure(state="disabled")
import tkinter as tk
from tkinter import ttk

class InterfazConversor(tk.Tk):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.title("Conversor de Monedas")
        self.geometry("300x250")

        # Entrada de cantidad
        self.label_cantidad = tk.Label(self, text="Cantidad:")
        self.label_cantidad.pack()
        self.entry_cantidad = tk.Entry(self)
        self.entry_cantidad.pack()

        # Selección de moneda origen
        self.label_origen = tk.Label(self, text="De:")
        self.label_origen.pack()
        self.combo_origen = ttk.Combobox(self, values=[])
        self.combo_origen.pack()

        # Selección de moneda destino
        self.label_destino = tk.Label(self, text="A:")
        self.label_destino.pack()
        self.combo_destino = ttk.Combobox(self, values=[])
        self.combo_destino.pack()

        # Botón de conversión
        self.boton_convertir = tk.Button(self, text="Convertir", command=self.controlador.convertir)
        self.boton_convertir.pack()

        # Resultado
        self.label_resultado = tk.Label(self, text="Resultado: ")
        self.label_resultado.pack()

    def actualizar_monedas(self, monedas):
        #Llena los Combobox con las monedas disponibles.
        self.combo_origen["values"] = monedas
        self.combo_destino["values"] = monedas

    def mostrar_resultado(self, resultado):
        #Muestra el resultado en la interfaz.
        self.label_resultado.config(text=f"Resultado: {resultado}")

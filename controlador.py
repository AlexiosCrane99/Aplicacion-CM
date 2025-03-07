# controlador.py

"""
Este módulo actúa como puente entre la capa de negocio y la capa de presentación.
"""

from negocio.conversor import ConversorMonedas
from presentacion.interfaz import InterfazConversor
from datos.tasas_cambio import tasas

class ControladorConversor:
    def __init__(self):
        self.modelo = ConversorMonedas()
        self.vista = InterfazConversor(self)
        
        # Cargar monedas en la interfaz
        self.vista.actualizar_monedas(list(tasas.keys()))

    def convertir(self):
        """Obtiene datos de la vista, realiza la conversión y actualiza el resultado."""
        try:
            cantidad = float(self.vista.entry_cantidad.get())
            moneda_origen = self.vista.combo_origen.get()
            moneda_destino = self.vista.combo_destino.get()
            resultado = self.modelo.convertir(cantidad, moneda_origen, moneda_destino)
            self.vista.mostrar_resultado(resultado)
        except ValueError:
            self.vista.mostrar_resultado("Error: Ingrese un número válido")

    def ejecutar(self):
        """Inicia la interfaz gráfica."""
        self.vista.mainloop()

if __name__ == "__main__":
    app = ControladorConversor()
    app.ejecutar()

from datos.tasas_cambio import tasas

class ConversorMonedas:
    @staticmethod
    def convertir(cantidad, moneda_origen, moneda_destino):
     
        if moneda_origen not in tasas or moneda_destino not in tasas:
            return "Error: Moneda no válida"
        
        return round(cantidad * (tasas[moneda_destino] / tasas[moneda_origen]), 2)

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

from model import logica_Credito 
 
class CreditoApp(App):
 
    def build(self):
        contenedor = GridLayout(cols=2, padding=20, spacing=20)
 
        contenedor.add_widget(Label(text="Monto del crédito educativo"))
        self.monto = TextInput(font_size=30)
        contenedor.add_widget(self.monto)
 
        contenedor.add_widget(Label(text="Tasa de interés (%)"))
        self.tasa = TextInput(font_size=30)
        contenedor.add_widget(self.tasa)
 
        contenedor.add_widget(Label(text="Número de cuotas"))
        self.plazo = TextInput(font_size=30)
        contenedor.add_widget(self.plazo)
 
        self.resultado = Label(text="")
        contenedor.add_widget(self.resultado)
 
        calcular = Button(text="Calcular cuota", font_size=40)
        contenedor.add_widget(calcular)
 
        calcular.bind(on_press=self.calcular_cuota)
 
        return contenedor
 
    def calcular_cuota(self, value):
        try:
            monto = float(self.monto.text)
            tasa = float(self.tasa.text) / 100
            plazo = int(self.plazo.text)
 
            cuota = round(logica_Credito.calcular_cuota(monto, tasa, plazo), 2)
            self.resultado.text = f"Cuota mensual: {cuota}"
 
        except ValueError:
            self.resultado.text = "Ingrese valores numéricos válidos"
        except Exception as err:
            self.mostrar_error(err)
 
    def mostrar_error(self, err):
        contenido = GridLayout(cols=1)
        contenido.add_widget(Label(text=str(err)))
 
        cerrar = Button(text="Cerrar")
        contenido.add_widget(cerrar)
 
        popup = Popup(title="Error", content=contenido)
        cerrar.bind(on_press=popup.dismiss)
        popup.open()
 
 
if __name__ == "__main__":
    CreditoApp().run()
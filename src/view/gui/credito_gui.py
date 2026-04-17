import sys
sys.path.append("src")

from model.logica_Credito import calcular_cuota, calcular_total_abonos, calcular_total_intereses 
from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class CreditoEducativoGUI(App):
    def build(self): 
        layout = GridLayouy(cols=2)
        self.monto_input= TextInput(hint_text='Monto de la compra')
        self.intereses_input = TextInput(hint_text='Tasa de interés')
        self.plazo_input = TextInput(hint_text='Número de pagos')

        boton_calcular = Button(text= 'Calcular cuota mensual')
        boton_calcular.bind(on_press= self.calcular_cuouta)

        self.resultado_label = Label(text='Calcular cuota')

        layout.add_widget(Label(text='Valor de compra'))
        layout.add_widget(self.monto_input)
        
        layout.add_widget(Label(text="Tasa de interés"))
        layout.add_widget(self.intereses_input)

        layout.add_widget(Label(text="Cuota a pagar"))
        layout.add_widget(self.plazo_input)

if __name__ == "__main__":
    CreditoEducativoGUI().run()

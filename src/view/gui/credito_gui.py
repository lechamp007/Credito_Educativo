import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.graphics import Color, RoundedRectangle, Rectangle
from kivy.core.window import Window
from kivy.metrics import dp
 
# Tamaño de ventana fijo y centrado
Window.size = (520, 620)
Window.clearcolor = (0.96, 0.97, 0.99, 1)  # Fondo gris azulado suave
 
 
# ── Paleta de colores ──────────────────────────────────────────────────────────
AZUL_OSCURO  = (0.10, 0.22, 0.44, 1)   # Encabezado / acentos fuertes
AZUL_MEDIO   = (0.18, 0.40, 0.75, 1)   # Botón principal
AZUL_CLARO   = (0.86, 0.92, 1.00, 1)   # Fondo de tarjeta
VERDE        = (0.13, 0.65, 0.45, 1)   # Resultado exitoso
ROJO         = (0.80, 0.18, 0.18, 1)   # Error
BLANCO       = (1, 1, 1, 1)
GRIS_TEXTO   = (0.35, 0.38, 0.45, 1)
GRIS_BORDE   = (0.78, 0.83, 0.92, 1)
 
 
class CardLayout(BoxLayout):
    """BoxLayout con fondo blanco redondeado (efecto tarjeta)."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(pos=self._redraw, size=self._redraw)
 
    def _redraw(self, *_):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*BLANCO)
            RoundedRectangle(pos=self.pos, size=self.size, radius=[dp(16)])
            Color(*GRIS_BORDE)
            RoundedRectangle(pos=(self.x - 1, self.y - 1),
                             size=(self.width + 2, self.height + 2),
                             radius=[dp(16)])
            Color(*BLANCO)
            RoundedRectangle(pos=self.pos, size=self.size, radius=[dp(16)])
 
 
class HeaderWidget(BoxLayout):
    """Encabezado azul con título y subtítulo."""
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=[dp(24), dp(20)],
                         size_hint_y=None, height=dp(110), **kwargs)
        self.bind(pos=self._redraw, size=self._redraw)
 
        titulo = Label(
            text="Crédito Educativo",
            font_size=dp(26),
            bold=True,
            color=BLANCO,
            size_hint_y=None,
            height=dp(40),
        )
        
        
        self.add_widget(titulo)
        
 
    def _redraw(self, *_):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*AZUL_OSCURO)
            RoundedRectangle(pos=self.pos, size=self.size,
                             radius=[dp(16), dp(16), 0, 0])
 
 
def make_label(text):
    return Label(
        text=text,
        font_size=dp(14),
        color=GRIS_TEXTO,
        halign='left',
        size_hint_y=None,
        height=dp(22),
        text_size=(None, None),
    )
 
 
def make_input(hint):
    ti = TextInput(
        hint_text=hint,
        font_size=dp(18),
        foreground_color=(0.10, 0.15, 0.30, 1),
        background_color=BLANCO,
        cursor_color=AZUL_MEDIO,
        hint_text_color=(0.65, 0.70, 0.80, 1),
        padding=[dp(12), dp(10)],
        size_hint_y=None,
        height=dp(46),
        multiline=False,
        write_tab=False,
    )
    return ti
 
 
class CreditoApp(App):
 
    def build(self):
        self.title = "Crédito Educativo"
 
        # Contenedor raíz
        root = BoxLayout(orientation='vertical', spacing=0)
 
        # ── Encabezado ──────────────────────────────────────────────────────
        root.add_widget(HeaderWidget())
 
        # ── Cuerpo con padding ───────────────────────────────────────────────
        body = BoxLayout(orientation='vertical', padding=[dp(20), dp(16)],
                         spacing=dp(14))
 
        # Tarjeta de formulario
        card = CardLayout(orientation='vertical',
                          padding=[dp(20), dp(18)],
                          spacing=dp(10),
                          size_hint_y=None,
                          height=dp(310))
 
        # Campo: Monto
        card.add_widget(make_label("Valor del crédito "))
        self.monto = make_input("Ej: 5000000")
        card.add_widget(self.monto)
 
        # Campo: Tasa
        card.add_widget(make_label("Tasa de interés mensual"))
        self.tasa = make_input("Ej: 0.015    máximo 4%")
        card.add_widget(self.tasa)
 
        # Campo: Plazo
        card.add_widget(make_label("Número de cuotas  (1 – 36)"))
        self.plazo = make_input("Ej: 24")
        card.add_widget(self.plazo)
 
        body.add_widget(card)
 
        # ── Botón calcular ───────────────────────────────────────────────────
        self.btn = Button(
            text="Calcular cuota",
            font_size=dp(17),
            bold=True,
            background_normal='',
            background_color=AZUL_MEDIO,
            color=BLANCO,
            size_hint_y=None,
            height=dp(52),
        )
        self.btn.bind(on_press=self.calcular_cuota)
        body.add_widget(self.btn)
 
        # ── Tarjeta de resultado ─────────────────────────────────────────────
        self.resultado_card = CardLayout(
            orientation='vertical',
            padding=[dp(16), dp(14)],
            spacing=dp(4),
            size_hint_y=None,
            height=dp(90),
            opacity=0,           # oculta al inicio
        )
 
        lbl_titulo_res = Label(
            text="Cuota mensual a pagar",
            font_size=dp(13),
            color=GRIS_TEXTO,
            size_hint_y=None,
            height=dp(20),
        )
        self.resultado_valor = Label(
            text="",
            font_size=dp(30),
            bold=True,
            color=VERDE,
            size_hint_y=None,
            height=dp(44),
        )
        self.resultado_card.add_widget(lbl_titulo_res)
        self.resultado_card.add_widget(self.resultado_valor)
        body.add_widget(self.resultado_card)
 
        # Espacio flexible al fondo
        body.add_widget(Widget())
 
        # Pie de página
        
 
        root.add_widget(body)
        return root
 
    # ── Lógica ────────────────────────────────────────────────────────────────
 
    def calcular_cuota(self, *_):
        from model import logica_Credito
 
        # Resetear estado visual
        self.resultado_card.opacity = 0
        self.resultado_valor.color = VERDE
 
        try:
            monto = float(self.monto.text.replace(',', '.').strip())
            tasa  = float(self.tasa.text.replace(',', '.').strip()) / 100
            plazo = int(self.plazo.text.strip())
 
            cuota = round(logica_Credito.calcular_cuota(monto, tasa, plazo), 2)
 
            # Formatear con separadores de miles
            cuota_fmt = f"$ {cuota:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
            self.resultado_valor.text = cuota_fmt
            self.resultado_card.opacity = 1
 
        except ValueError:
            self.mostrar_error(
                "⚠  Valor inválido",
                "Por favor ingrese solo números en todos los campos.\n"
                "Ejemplo de tasa: 1.5  (sin el signo %)"
            )
        except Exception as err:
            self.mostrar_error("⚠  No se pudo calcular", str(err))
 
    def mostrar_error(self, titulo, mensaje):
        contenido = BoxLayout(orientation='vertical',
                              padding=[dp(20), dp(16)],
                              spacing=dp(12))
 
        contenido.add_widget(Label(
            text=mensaje,
            font_size=dp(14),
            color=(0.20, 0.20, 0.25, 1),
            halign='center',
            text_size=(dp(320), None),
        ))
 
        cerrar = Button(
            text="Entendido",
            font_size=dp(15),
            bold=True,
            background_normal='',
            background_color=ROJO,
            color=BLANCO,
            size_hint_y=None,
            height=dp(44),
        )
 
        contenido.add_widget(cerrar)
 
        popup = Popup(
            title=titulo,
            title_color=(0.15, 0.15, 0.20, 1),
            title_size=dp(16),
            content=contenido,
            size_hint=(None, None),
            size=(dp(360), dp(200)),
            separator_color=ROJO,
        )
        cerrar.bind(on_press=popup.dismiss)
        popup.open()
 
 
if __name__ == "__main__":
    CreditoApp().run()
 
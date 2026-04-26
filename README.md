Crédito Educativo - GUI

Este proyecto consiste en el desarrollo de una interfaz gráfica (GUI) para la gestión y simulación de un crédito educativo. Permite calcular cuotas, intereses y llevar un control de los pagos realizados de manera visual e intuitiva.


Integrantes del equipo
Jerónimo Roldán Cardona
Francisco Gómez
Características
Cálculo de cuota mensual
Cálculo del total de intereses
Registro de abonos realizados
Visualización de resultados en una interfaz gráfica amigable
Implementación basada en Kivy
Tecnologías utilizadas
Python
Kivy (para la interfaz gráfica)
Arquitectura modular (separación entre lógica y vista)
 Estructura del proyecto
Credito_Educativo/
│
├── src/
│   ├── model/
│   │   └── logica_Credito.py
│   ├── view/
│   │   └── gui/
│   │       └── credito_gui.py
│
├── main.py
└── README.md
Instrucciones para ejecutar la GUI

Clonar o descargar el repositorio

git clone <URL_DEL_REPOSITORIO>

Ubicarse en la carpeta del proyecto

cd Credito_Educativo

Instalar dependencias
Asegúrate de tener Python instalado y luego ejecuta:

pip install kivy

Ejecutar la aplicación

python main.py
Requisitos
Python 3.x
Librería Kivy instalada correctamente
Notas adicionales
Asegúrate de que la estructura de carpetas se mantenga intacta para evitar errores en las importaciones.
Si se presentan errores con Kivy, verifica la instalación o dependencias del sistema.

Simulador de Crédito Educativo
Integrantes

Juan Felipe Santiago

Jhairo Esteban Muñeton

Descripción del Proyecto

Este proyecto consiste en el desarrollo de un simulador de crédito educativo en Python.
El sistema permite calcular el valor de la cuota mensual, el total pagado al finalizar el crédito y el total de intereses generados, a partir de un monto solicitado, una tasa de interés mensual y un plazo en meses.

Además, el programa valida los datos ingresados y maneja errores mediante excepciones personalizadas, garantizando que los valores ingresados sean correctos antes de realizar los cálculos.

También incluye pruebas unitarias para verificar que los resultados sean correctos en diferentes escenarios, tanto normales como extraordinarios y casos de error.

Datos de Entrada

El programa recibe tres datos principales:

Valor de la compra: monto total del crédito solicitado.

Tasa de interés mensual: porcentaje mensual que se cobra por el crédito.

Plazo: número de meses en los que se pagará el crédito.

Datos de Salida

Con base en los datos ingresados, el sistema calcula:

Cuota mensual: valor que se debe pagar cada mes.

Total de abonos: suma total pagada al finalizar el crédito.

Total de intereses: dinero adicional pagado por concepto de intereses.

Casos Evaluados

Se probaron diferentes escenarios:

Casos normales:

Créditos con tasas entre 1% y 1.5%.

Plazos entre 48 y 72 meses.

Montos entre 15 y 35 millones de pesos.

Casos extraordinarios:

Tasas más bajas (0.8% y 0.9%).

Plazos más largos (hasta 96 meses).

Casos de error:

Valor de crédito negativo.

Tasa superior al máximo permitido.

Plazo mayor al permitido.

Plazo negativo o cero.

Datos incompletos.

En todos estos casos el sistema responde correctamente, ya sea calculando los valores esperados o generando el error correspondiente.

from joblib import load
import pandas as pd
import os
import gradio as gr

from demo.utils.predicciones import predecir
from demo.metadata.columnas import Options

# if __name__ == '__main__':
# result = predecir(50, 100000, 'Femenino', 'Credit Card', 'Emaar Square Mall')
# print(result)


def main():
    age = gr.Number(label="Age")
    price = gr.Number(label="Price")
    gender = gr.Radio(choices=["Male", "Female"], label="Gender")
    payment_method = gr.Radio(
        choices=Options.categorias_payment_method, label="Payment Method"
    )
    shopping_mall = gr.Dropdown(
        choices=Options.categorias_shopping_mall, label="Shopping Mall"
    )
    descripcion = """
        Este demo te permite explorar y comparar múltiples modelos 
        de clasificación para predecir la categoría de las ventas en función de 
        distintas características relacionadas con los productos, el entorno de
        venta y otros factores relevantes.
    """
    iface = gr.Interface(
        fn=predecir,
        inputs=[age, price, gender, payment_method, shopping_mall],
        outputs=gr.Textbox(label='Prediction'),
        title='Clasificación de categorías de ventas',
        description=descripcion,
        theme='dark'
    )

    iface.launch()


if __name__ == '__main__':
    main()

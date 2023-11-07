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
    price = gr.Number(label="Price", placeholder="Enter price here...")
    gender = gr.Radio(choices=["Male", "Female"], label="Gender")
    payment_method = gr.Radio(
        choices=Options.categorias_payment_method, label="Payment Method"
    )
    shopping_mall = gr.Dropdown(
        choices=Options.categorias_shopping_mall, label="Shopping Mall"
    )

    css = """
    .gradio_container {
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }
    .gradio_label {
        color: #333333;
        font-weight: bold;
    }
    .gradio_number input, .gradio_radio, .gradio_dropdown {
        border: 2px solid #eeeeee;
        border-radius: 5px;
    }
    .gradio_number input:hover, .gradio_radio:hover, .gradio_dropdown:hover {
        border-color: #3498db;
    }
    .gradio_number input:focus, .gradio_radio:focus, .gradio_dropdown:focus {
        border-color: #9b59b6;
        outline: none;
    }
    .gradio_output {
        color: #2ecc71;
        font-weight: bold;
    }
    """

    iface = gr.Interface(
        fn=predecir,
        inputs=[age, price, gender, payment_method, shopping_mall],
        outputs=gr.Textbox(label="Prediction"),
        title="Shopping Classifier",
        description="Enter the details for classification.",
        theme="huggingface",  # Usa uno de los temas disponibles, por ejemplo, 'huggingface'
        css=css,  # Usa el CSS personalizado
    )

    iface.launch()


if __name__ == '__main__':
    main()

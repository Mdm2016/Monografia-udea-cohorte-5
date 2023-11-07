from joblib import load
import pandas as pd
import os

from sklearn.preprocessing import MinMaxScaler

from demo.metadata.path import Path
from demo.metadata.columnas import Columns
from demo.metadata.columnas import Options


def predecir(
    edad: int, precio: int, genero: str, medio_pago: str, lugar: str
) -> str:
    """Realiza predicciones utilizando varios modelos de aprendizaje automático y
     devuelve una cadena con los resultados.

    Args:
        edad (int): Edad del cliente.
        precio (int): Precio del producto comprado.
        genero (str): Género del cliente ('Male' o 'Female').
        medio_pago (str): Método de pago utilizado por el cliente.
        lugar (str): Centro comercial donde se realizó la compra.

    Returns:
        str: Cadena con las predicciones realizadas por varios modelos de aprendizaje
         automático.

    """
    bernulli = load(Path.bernulli)
    # decision_tree = load(Path.decision_tree)
    gaussian = load(Path.gaussian)
    multinomial = load(Path.multinomial)
    # neural_network = load(Path.neural_network)
    # random_forest_classifier = load(Path.random_forest_classifier)

    datos = pd.Series(0, index=Columns.columnas_modelo)

    datos['age'] = edad
    datos['price'] = precio
    datos['gender_Male'] = 1 if genero == 'Male' else 0

    if medio_pago in ['Credit Card', 'Debit Card']:
        datos[f'payment_method_{medio_pago}'] = 1

    datos[f'shopping_mall_{lugar}'] = 1

    datos_df = datos.to_frame().transpose()

    min_max = MinMaxScaler()
    x_scale = min_max.fit_transform(datos_df.values)
    x_scale = pd.DataFrame(x_scale, columns=datos_df.columns)

    prediccion_bernulli = bernulli.predict(datos_df)[0]
    # prediccion_decision_tree = decision_tree.predict(datos_df)[0]
    prediccion_gaussian = gaussian.predict(datos_df)[0]
    prediccion_multinomial = multinomial.predict(datos_df)[0]
    # prediccion_neural_network = neural_network.predict(datos_df)
    # prediccion_random_forest = random_forest_classifier.predict(datos_df)[0]

    prediccion = f'Predicción Bernulli: {prediccion_bernulli}\n'
    prediccion += f'Predicción Gaussian: {prediccion_gaussian}\n'
    prediccion += f'Predicción Multinomial: {prediccion_multinomial}\n'
    # prediccion += f'Predicción Random Forest: {prediccion_random_forest}\n'

    return prediccion

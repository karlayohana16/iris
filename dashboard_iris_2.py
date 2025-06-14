# -*- coding: utf-8 -*-
"""dashboard_iris_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OxUxp6DagN1cFZ1VGSwGMA7dfQ_-DdpX
"""

import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import os
import plotly.io as pio

# Figura de ejemplo (puedes usar la tuya)
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

# Inicializar la app Dash
app = dash.Dash(__name__)

# Layout con el botón y el mensaje
app.layout = html.Div([
    dcc.Graph(figure=fig),
    html.Button("Exportar Reporte PDF", id="exportar-btn", n_clicks=0),
    html.Div(id="mensaje-exportacion")
])

# Funciones para exportar
def guardar_graficas(figuras, carpeta="graficas_exportadas"):
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    rutas = []
    for i, fig in enumerate(figuras):
        ruta = os.path.join(carpeta, f"grafica_{i+1}.png")
        try:
            fig.write_image(ruta, format="png", engine="kaleido")
            rutas.append(ruta)
        except Exception as e:
            print(f"Error al guardar {ruta}: {e}")
    return rutas

# Ejecutar el servidor
if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=8050)
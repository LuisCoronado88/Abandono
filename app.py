from dash import Dash
from dash import dcc
from dash import html

import dash_bootstrap_components as dbc

from tabs import contextoproblema
from tabs import metodologia
from tabs import eda
from tabs import metricasmodelo
from tabs import prediccionmodelo

app = Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.FLATLY
    ]
)

app.title = "Employee Attrition"

app.layout = dbc.Container([

    html.Br(),

    html.H1(
        "Employee Attrition Dashboard",
        className="text-center"
    ),

    html.Hr(),

    dcc.Tabs([

        dcc.Tab(
            label="Contexto",
            children=contextoproblema.layout()
        ),

        dcc.Tab(
            label="Metodología",
            children=metodologia.layout()
        ),

        dcc.Tab(
            label="EDA",
            children=eda.layout()
        ),

        dcc.Tab(
            label="Métricas",
            children=metricasmodelo.layout()
        ),

        dcc.Tab(
            label="Predicción",
            children=prediccionmodelo.layout()
        )

    ])

], fluid=True)

if __name__ == "__main__":
    app.run(debug=True)
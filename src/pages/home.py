import dash
from dash import html, dcc

dash.register_page(__name__, path='/')

layout = html.Div(children=[
    html.Br(),
    html.H1(children='Which Dog is right for you?'),

    html.Div(children='''
        This is our Home page content.
    ''')

])
import dash
from dash import html, dash_table
import pandas as pd

dash.register_page(__name__)

description = pd.read_csv("../data/trait_description.csv").rename(columns={"Trait_1": "Low (1)", "Trait_5": "High (5)"})

layout = html.Div(children=[
    html.Br(),
    html.H1(children='What do the traits mean?', style = {"text-align":"center"}),

    html.Div(children=dash_table.DataTable(description.to_dict('records'), 
                                           style_cell={'textAlign': 'left'}, 
                                           style_data={'whiteSpace': 'normal','height': 'auto',"padding":"5px"}, 
                                           style_table={"padding":"10px"},
                                           style_as_list_view=True))
])
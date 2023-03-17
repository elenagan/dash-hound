import dash
from dash import html, dcc, Input, Output, callback, dash_table
import pandas as pd
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/')

traits = pd.read_csv("../data/breed_traits.csv").drop(["Coat Type", "Coat Length"], axis = 1).drop(166)
trait_choices = sorted(traits.columns.to_list())
trait_choices.remove("Breed")

def top_dogs(choices, order):
    sorted = traits.sort_values(choices, ascending = order)
    cut = sorted.loc[:][["Breed"]+choices][0:10]
    cut.index = range(1,11)
    return cut

layout = html.Div(children=[
    html.Br(),
    html.H1(children='Which Dog is right for you?', style = {"text-align":"center"}),

    html.Div(dbc.Row(
        [dbc.Col([html.H5("Please select the three most important traits in your perfect dog:"),
                  dcc.Dropdown(trait_choices, placeholder = "First Priority", id='first', className = "form-select"),
                  dcc.RadioItems({"True": "Low Level ", "False" : "High Level "}, value = "False", inline = True, id = "level-1"),
                  dcc.Dropdown(trait_choices, placeholder = "Second Priority", id='second', className = "form-select"),
                  dcc.RadioItems({"True": "Low Level ", "False" : "High Level "}, value = "False", inline = True, id = "level-2"),
                  dcc.Dropdown(trait_choices, placeholder = "Third Priority", id='third', className = "form-select"),
                  dcc.RadioItems({"True": "Low Level ", "False" : "High Level "}, value = "False", inline = True, id = "level-3")]), 
                    
         dbc.Col([dash_table.DataTable(id="table")])]
    ))

])

@callback(
    Output(component_id='table', component_property='data'),
    Input(component_id='first', component_property='value'),
    Input(component_id='second', component_property='value'),
    Input(component_id='third', component_property='value'),
    Input(component_id='level-1', component_property='value'),
    Input(component_id='level-2', component_property='value'),
    Input(component_id='level-3', component_property='value'))
def update_output(first, second, third, level1, level2, level3):
    choices = [first, second, third]
    levels = []
    for i in [level1, level2, level3]:
        if i == "True":
            levels.append(True)
        else:
            levels.append(False)
    return top_dogs(choices, levels).to_dict("records")
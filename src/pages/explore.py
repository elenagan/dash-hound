import dash
from dash import html, dcc, Input, Output, callback
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__)

rank = pd.read_csv("../data/breed_rank.csv")
traits = pd.read_csv("../data/breed_traits.csv").T
traits.columns = traits.iloc[0]
traits["Traits"] = traits.index
traits = traits.reset_index().drop(index=[0,7,8])

def plot_trait(df=traits, dog ="Dachshunds"):
    df = df.sort_values(by=dog)
    fig = px.bar(df, y='Traits', x=dog, orientation='h', labels = {dog:"Level"}, title=dog)
    fig.update_layout(yaxis={'categoryorder':'array', 'categoryarray':list(df['Traits'])})
    return fig

def display_img(dog = "Dachshunds"):
    img = rank[rank["Breed"]==dog]["Image"]
    return img

def info_link(dog = "Dachshunds"):
    link = rank[rank["Breed"]==dog]["links"]
    return link

#List of unique dog breeds in dataset
breeds = sorted(rank["Breed"].to_list())
breeds.remove("Plott Hounds")

layout = html.Div(children=[
    html.Br(),
    html.H1(children='Explore the dog breeds', style = {"text-align":"center"}),
    html.Br(),
    dbc.Row(dbc.Col(dcc.Dropdown(breeds, value = "Dachshunds", placeholder = "Select a breed", id='breed'), width=4)),
    dbc.Row([dbc.Col(html.Div(dcc.Graph(id="plot"))),
             dbc.Col([html.A("Learn More about the breed", id="link", target = "_blank"),
                      html.Div(html.Img(id="img"))])
                      ])  
])

@callback(
    Output(component_id='plot', component_property='figure'),
    Input(component_id='breed', component_property='value'))
def update_output(value):
    return plot_trait(dog = value)

@callback(
    Output(component_id='img', component_property='src'),
    Input(component_id='breed', component_property='value'))
def update_output(value):
    return display_img(dog = value)

@callback(
    Output(component_id='link', component_property='href'),
    Input(component_id='breed', component_property='value'))
def update_output(value):
    return info_link(dog = value)


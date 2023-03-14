import dash
from dash import html, dcc
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
layout = html.Div(children=[
    html.Br(),
    html.H1(children='Explore the dog breeds'),
    dbc.Row([dbc.Col(html.Div(dcc.Graph(figure=plot_trait()))),
             dbc.Col([html.A("Learn More about the breed", href=info_link(), target = "_blank"),
                      html.Div(html.Img(src=display_img()))])
                      ])  
])
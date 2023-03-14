import dash
from dash import html, dcc
import pandas as pd
import altair as alt

dash.register_page(__name__)

rank = pd.read_csv("../data/breed_rank.csv")
traits = pd.read_csv("../data/breed_traits.csv")

# chart = alt.Chart(rank).mark_bar().encode(
#     x="Breed",
#     y="2020_rank"
# )

layout = html.Div(children=[
    html.Br(),
    html.H1(children='Explore the dog breeds'),

    #html.Div(dcc.Graph(chart))

])
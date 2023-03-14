import dash
from dash import html, dash_table, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import altair as alt

rank = pd.read_csv("../data/breed_rank.csv")
traits = pd.read_csv("../data/breed_traits.csv")

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED], use_pages=True)
server = app.server

#navbar adapted from documentation
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href=dash.page_registry['pages.home']['path'])),
        dbc.NavItem(dbc.NavLink("Explore the breeds", href=dash.page_registry['pages.explore']['path'])),
        dbc.NavItem(dbc.NavLink("Trait Description", href=dash.page_registry['pages.traits']['path']))
    ],
    brand="DashHound",
    brand_href=dash.page_registry['pages.home']['path'],
    color="primary",
    dark=True,
)

#Footer for all pages
footer = html.Div([
    html.Hr(),
    dbc.Stack([
        html.Div("Copyright © 2023 Elena Ganacheva"),
        html.Div([html.A("This software", href="https://github.com/elenagan/dash-hound/tree/main/src"), " is free and open source, licensed under the MIT license."])], 
        className="text-muted")
    ])

#Main layout
app.layout = html.Div([
    #navbar
    dbc.Row([
    html.Div(navbar)
    ]),
    #Main Panel
    html.Div(dash.page_container, style = {"padding":"10px"}),
    #Footer
    dbc.Row([footer], style = {"padding":"10px"})
])

app.run_server()

if __name__ == '__main__':
    app.run_server(debug=True)
from dash import dash, html

app = dash.Dash()
server = app.server

app.layout = html.Div('I am alive!!')
app.run_server()
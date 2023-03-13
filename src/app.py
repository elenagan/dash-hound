from dash import dash, html

app = dash.Dash()
app.layout = html.Div('I am alive!!')
app.run_server()
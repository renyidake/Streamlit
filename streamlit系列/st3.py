import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([ html.H1('My Dashboard'), dcc.Graph(id='my-chart', figure={ 'data': [1, 2, 3, 4, 5], 'xlabel': 'Categories', 'ylabel': 'Values' }) ])
return app
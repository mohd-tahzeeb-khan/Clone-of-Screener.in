from dash import Dash, html
from components.navbar import navbar
app=Dash(__name__)
app.layout=html.Div([
    navbar
])
if __name__=='__main__':
    app.run(debug=True)
from dash import Dash, html
from components.navbar import navbar
from components.footer import footer
app=Dash(__name__)
app.layout=html.Div([
    navbar,
    footer
])
if __name__=='__main__':
    app.run(debug=True)
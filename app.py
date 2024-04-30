from dash import Dash, html
from components.navbar import navbar
from components.footer import footer
from components.landingpage import landing
app=Dash(__name__, title='Stock Screener and fundamental analysis tool for Indian Stock')

app.layout=html.Div([
    navbar,
    landing,
    footer
])
if __name__=='__main__':
    app.run(debug=True)
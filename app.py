from dash import Dash, html
from landingpage import landingpage
app=Dash(__name__, title='Stock Screener and fundamental analysis tool for Indian Stock')

app.layout=html.Div([])
if __name__=='__main__':
    app.run(debug=True)
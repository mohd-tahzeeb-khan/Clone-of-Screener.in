from dash import Dash, html
from landingpage import landingpage
from components.industry_info import section_1
external_stylesheets = ['assets/info.css']

app=Dash(__name__, external_stylesheets=external_stylesheets,title='Stock Screener and fundamental analysis tool for Indian Stock')

app.layout=html.Div([section_1])
if __name__=='__main__':
    app.run(debug=True)
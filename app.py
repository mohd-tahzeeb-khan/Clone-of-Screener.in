from dash import Dash, html
from landingpage import landingpage
from components.industry_info import section_1, Pros_Cons, peer_table, Profit_Loss, Quarterly_Results
from components.footer import footer
external_stylesheets = ['assets/info.css']

app=Dash(__name__, external_stylesheets=external_stylesheets,title='Stock Screener and fundamental analysis tool for Indian Stock')

app.layout=html.Div([section_1, Pros_Cons, peer_table, Quarterly_Results, Profit_Loss, footer])
if __name__=='__main__':
    app.run(debug=True)
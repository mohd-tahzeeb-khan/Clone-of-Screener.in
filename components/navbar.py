from dash import Dash, html

navbar=html.Div([
    html.Ul([
        html.Li(id='HOME', className='HOME', children=['HOME']),
        html.Li(id='SCREENS', className='SCREENS', children=['SCREENS'])
    ]
    )
], className="navbar")
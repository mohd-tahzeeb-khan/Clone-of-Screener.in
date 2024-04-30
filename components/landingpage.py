from dash import Dash, html, dcc
landing=html.Div(id='main-landing', className='main-landing', children=[
    html.Div(id='div-logo', className='div-logo', children=[
        html.Img(id='main-logo', className='main-logo', children=[],
        src='assets\screener logo.svg', alt='logo'),
    ]), 
    html.Div(id='div-slogan', className='div-slogan', children=[
        html.H3(id='slogan', className='slogan', children='Stock analysis and screening tool for investors in India.')
    ]), 
    html.Div(id='div-search-bar', className='div-search-bar', children=[
        html.Span(id='search-bar-img-span', className='search-bar-img-span', children=[html.Img(id='search-bar-img', className='search-bar-img', children=[],
            src='assets\search icon.png', alt='search')]),
        dcc.Input(id='input-search-bar', className='input-search-bar',
            type='text',
            placeholder='Search for a Company',
            value=''
        )
    ]),
    html.Div(id='div-suggestions', className='div-suggestions', children=[
        html.H3(id='analyse', className='analyse', children='Or analyse:')
        
    ])

        
])
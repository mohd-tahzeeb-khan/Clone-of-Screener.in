from dash import Dash, html, dcc
suggestions = [
    "Suggestion 1",
    "Suggestion 2",
    "Suggestion 3",
    "Suggestion 4",
    "Suggestion 5",
    "Suggestion 6",
    "Suggestion 7",
    "Suggestion 8",
    "Suggestion 9",
    "Suggestion 10",
    "Suggestion 11",
    "Suggestion 12"
]
buttons = [html.Button(suggestion, className='suggestion-button') for suggestion in enumerate(suggestions)]
landing=html.Div(id='main-landing', className='main-landing', children=[
    html.Div(id='div-logo', className='div-logo', children=[
        html.Img(id='main-logo', className='main-logo', children=[],
        src='assets\screener logo.svg', alt='logo'),
    ]), 
    html.Div(id='div-slogan', className='div-slogan', children=[
        html.H3(id='slogan', className='slogan', children='Stock analysis and screening tool for investors in India.')
    ]), 
    html.Div(id='div-search-bar', className='div-search-bar', children=[
        html.Span(id='search-bar-img-span', className='search-bar-img-span', children=[html.Img(id='search-bar-img', className='search-bar-img common-search', children=[],
            src='assets\search icon.png', alt='search')]),
        dcc.Input(id='input-search-bar', className='input-search-bar common-search',
            type='text',
            placeholder='Search for a Company',

        )
    ]),
    html.Div(id='div-suggestions', className='div-suggestions', children=[
        
        html.Div(id='', className='', children=[html.H3(id='analyse', className='analyse', children='Or analyse:'), html.A(id='', className='suggestion-links', children=['Sandur Manganese'],
            href=''), 
             html.A(id='', className='suggestion-links', children=['Shilchar Tech'],
                href=''),html.A(id='', className='suggestion-links', children=['Sandur Manganese'],
            href=''), html.Br(id='', className='', children=[]),html.Br(id='', className='', children=[]),html.Br(id='', className='', children=[]),
             html.A(id='', className='suggestion-links', children=['Shilchar Tech'],
                href=''), 
                html.A(id='', className='suggestion-links', children=['Sandur Manganese'],
            href=''), 
             html.A(id='', className='suggestion-links', children=['Shilchar Tech'],
                href=''),html.A(id='', className='suggestion-links', children=['Sandur Manganese'],
            href=''), html.Br(id='', className='', children=[]),html.Br(id='', className='', children=[]),html.Br(id='', className='', children=[]),
             html.A(id='', className='suggestion-links', children=['Shilchar Tech'],
                href=''),html.A(id='', className='suggestion-links', children=['Shilchar Tech'],
                href=''),html.A(id='', className='suggestion-links', children=['Shilchar Tech'],
                href='')  ])
        
    ]),
    

        
])
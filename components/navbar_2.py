from dash import Dash, html, dcc

navbar = html.Nav(id='navbar', className='navbar', children=[
    html.Ul(id='navul', className='navul', children=[
        html.Div(id='leftside', className='leftside', children=[html.Li(id='home_li', className='nav-item', children=[
            html.A(id='home_link', className='nav-link', children='HOME', href='www.tahzeeb.dev'),
        ]),
        html.Li(id='title_li', className='nav-item', children=[
            html.A(id='title_link', className='nav-link', children='SCREENS', href='www.kkp.com'),
        ]),
        dcc.Dropdown([
            {
            "label": html.Span(className='spantool',
                children=[
                    html.Img(className="toollogo",src="assets\createstock.svg", height=20),
                    html.Span(className='heading-span',children="Create a stock screen", style={'font-size': 15, 'padding-left': 10}),
                    html.H6(id='', className='', children='Run queries on 10 Years of financial data')
                ], style={'align-items': 'center', 'justify-content': 'center', 'margin-top':'10px'}
            ),
            "value": "Python",
        },
        {
            "label": html.Span(className='spantool',
                children=[
                    html.Img(className="toollogo",src="assets\Commondityprices.svg", height=20),
                    html.Span(className='heading-span',children="Commondity Prices", style={'font-size': 15, 'padding-left': 10}),
                    html.H6(id='', className='', children='See prices and trends of over 10,000 commodtities')
                ], style={'align-items': 'center', 'justify-content': 'center'}
            ),
            "value": "Python",
        },
        {
            "label": html.Span(className='spantool',
                children=[
                    html.Img(className="toollogo",src="assets\searchshareholder.svg", height=20),
                    html.Span(className='heading-span',children="Search shareholders", style={'font-size': 15, 'padding-left': 10}),
                    html.H6(id='', className='', children='See companies where a person holds over 1% of the shares')
                ], style={'align-items': 'center', 'justify-content': 'center'},
            ),
            "value": "Python",
        },
        {
            "label": html.Span(className='spantool',
                children=[
                    html.Img(className="toollogo",src="assets\Latestannouncements.svg", height=20),
                    html.Span(className='heading-span', children="Latest Announcements", style={'font-size': 15, 'padding-left': 10}),
                    html.H6(id='', className='', children='Browse, filter and set alerts for announcements')
                ], style={'align-items': 'center', 'justify-content': 'center'}
            ),
            "value": "Python",
        },
            
            
        ], placeholder='TOOLS', className='dropdownmenu', optionHeight=100, maxHeight=500,searchable=False,clearable=False,style={'backgroundColor': 'transparent', 'border':'none', 'color':'#000'}),
            
        ]),
        html.Div(id='rightside', className='rightside', children=[
            
            html.Div(id='divlogin', className='divlogin', children=[html.Img(id='userimg', className='userimg', children=[], src='assets/user.png', alt='User'),html.A(id='btnlogin', className='btnlogin', children=['Login'], href='https://www.screener.in/login/?'),
        ]),
        html.Div(id='divgetfreeaccount', className='divgetfreeaccount', children=[html.A(id='btngetfreeaccount', className='btngetfreeaccount', children=['Get Free Account'],
            href='https://www.screener.in/register/?')
            
        ])
        
            
        ])
    ]),
])

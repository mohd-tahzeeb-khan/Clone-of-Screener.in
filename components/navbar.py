from dash import Dash, html, dcc

navbar = html.Nav(id='navbar', className='navbar', children=[
    html.Ul(id='navul', className='navul', children=[
        html.Div(id='leftside', className='leftside', children=[html.Li(id='home_li', className='nav-item', children=[
            html.A(id='home_link', className='nav-link', children='HOME', href='www.tahzeeb.dev'),
        ]),
        html.Li(id='title_li', className='nav-item', children=[
            html.A(id='title_link', className='nav-link', children='SCREENS', href='www.kkp.com'),
        ]),
        dcc.Dropdown(['tahzeeb', 'saniya', 'dudh wali'], placeholder='TOOLS', className='dropdownmenu', optionHeight=30, maxHeight=250, searchable=False,clearable=False,style={'backgroundColor': 'transparent', 'border':'none', 'color':'#000'}),
            
        ]),
        html.Div(id='rightside', className='rightside', children=[
            
            html.Div(id='divlogin', className='divlogin', children=[html.Img(id='userimg', className='userimg', children=[], src='assets/user.png', alt='User'),html.A(id='btnlogin', className='btnlogin', children=['Login'], href='www.tahzeeb.k'),
        ]),
        html.Div(id='divgetfreeaccount', className='divgetfreeaccount', children=[html.A(id='btngetfreeaccount', className='btngetfreeaccount', children=['Get Free Account'],
            href='www.tahzeeb.k')
            
        ])
        
            
        ])
    ]),
])

from dash import Dash, html, dcc

navbar = html.Nav(id='navbar', className='navbar', children=[
    html.Ul(id='navul', className='navul', children=[
        html.Li(id='home_li', className='nav-item', children=[
            html.A(id='home_link', className='nav-link', children='HOME', href='www.tahzeeb.dev'),
        ]),
        html.Li(id='title_li', className='nav-item', children=[
            html.A(id='title_link', className='nav-link', children='SCREENS', href='www.kkp.com'),
        ]),
        dcc.Dropdown(['tahzeeb', 'saniya', 'dudh wali'], placeholder='TOOLS')
    ]),
])

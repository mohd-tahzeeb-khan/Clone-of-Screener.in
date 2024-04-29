from dash import Dash, html, dcc
footer=html.Div(id='Footer', className='Footer', children=[
    html.Div(id='leftfooter', className='leftfooter', children=[
        html.Img(id='footerlogo', className='footerlogo', children=[],
            src='assets\screener logo.svg', alt='lgo'), 
            html.H2(id='footer-company-title', className='footer-company-title ', children='Stock analysis and screening tool'),
            html.H4(id='company-title', className='company-title footer-left-common-class', children='Mittal Analytics Private Ltd © 2009-2024'),
            html.H5(id='country-flagship', className='country-flagship footer-left-common-class', children='Made with  in India.'),
            html.H5(id='data-provider', className='data-provider footer-left-common-class', children='Data provided by C-MOTS Internet Technologies Pvt Ltd'),
            html.A(id='', className='footer-left-common-class', children=["Teams &  Condition"],
                href='')
        
    ]),
    html.Div(id='rightfooter', className='rightfooter', children=[
        html.Div(id='Product', className='Product', children=[
            html.H5(id='Product-title', className='Product-title', children='Product'),
            html.A(id='', className='Footer-links footer-right-common-class', children=['Premium'],href=''),
            html.A(id='', className='Footer-links footer-right-common-class', children=["What's New ?"],href=''),
            html.A(id='', className='Footer-links footer-right-common-class', children=['Learn'],href=''),
            html.Button(id='installbtn', className='installbtn', children=['Install'])
            ]),
        html.Div(id='Team', className='Team', children=[
            html.H5(id='Team-title', className='Team-title', children='Team'),
            html.A(id='', className='Footer-links footer-right-common-class', children=['About us'],href=''),
            html.A(id='', className='Footer-links footer-right-common-class', children=["Support"],href=''),
        ]),
        html.Div(id='Theme', className='Theme', children=[
            html.H5(id='Theme-title', className='Theme-title', children='Theme'),
            html.A(id='', className='Footer-links footer-right-common-class', children=['Light'],href=''),
            html.A(id='', className='Footer-links footer-right-common-class', children=["Dark"],href=''),
            html.A(id='', className='Footer-links footer-right-common-class', children=['Auto'],href=''),
        ])
        
    ])
    
])
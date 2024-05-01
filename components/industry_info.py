from dash import  Dash, html
section_1=html.Div(id='section_1', className='section_1', children=[
    html.Div(id='company-title', className='company-title', children=[
        html.H1(id='title', className='title', children='Tata Consultancy Services Ltd')
    ]),
    html.Div(id='button-parent', className='button-parent', children=[
        html.A(id='download-button', className='download-button', children=["Export to Excel"], href=''),
        html.A(id='Follow-button', className='Follow-button', children=['Follow'], href='')
    ]),
    html.Div(id='company-symbol', className='company-symbol', children=[
        html.A(id='', className='anchor-link', children=[html.Img( className='box-arrow-icon', children=[],
            src='assets/icons/link-icon.svg', alt=''),html.H5(id='website', className='website text-anchor-common', children='tcs.com'),],
            href=''),
        html.A(id='anchor-link', className='anchor-link', children=[
        html.Span(id='', className='NEC-tag text-anchor-common', children=['NCE: ']),
        html.H5(id='NEC', className='NEC text-anchor-common', children='532540')],
            href=''),
        html.A(id='', className='anchor-link', children=[
        html.Span(id='', className='BSE-tag text-anchor-common', children=['BSE: ']),
        html.H5(id='BSE', className='BSE text-anchor-common', children='TCS'),],
            href=''),
    ]),
    html.Div(id='stock-detials', className='stock-detials', children=[
        
    ])
    
    
])
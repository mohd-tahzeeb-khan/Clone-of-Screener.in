from dash import  Dash, html,dcc
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
    html.Div(id='', className='', children=[
        
    ]),
    html.Div(id='stock-detials', className='stock-detials', children=[
        html.Table(id='detail-table', className='detail-table', children=[
            html.Tr(id='', className='row', children=[
                html.Td(id='', className='table-title', children=['Market Cap']),
                html.Td(id='', className='rupee-common Cr-logo', children=['1382345']),
                html.Td(id='', className='table-title', children=['Current Price']),
                html.Td(id='', className='rupee-common', children=['3821']),
                html.Td(id='', className='table-title', children=['High/Low']),
                html.Td(id='', className='rupee-common', children=['4255',
                                                                    html.Span(id='', className='slash-before', children=['/']),
                                                                    html.Span(id='', className='', children=[
                                                                    html.Td(id='', className='', children=['3156'])])
                                                                   ]),
                
            ]),
            html.Tr(id='', className='row center-row', children=[
                html.Td(id='', className='table-title', children=['Stock P/E']),
                html.Td(id='#alternative-border', className='stockpe', children=['29.7']),
                html.Td(id='', className='table-title', children=['Book Value']),
                html.Td(id='#alternative-border', className='rupee-common', children=['250']),
                html.Td(id='', className='table-title', children=['Dividend Yield']),
                html.Td(id='#alternative-border', className='percent-common', children=['1.26']),
            ]),
            html.Tr(id='', className='row', children=[
                html.Td(id='', className='table-title', children=['ROCE']),
                html.Td(id='', className='percent-common', children=['64.3']),
                html.Td(id='', className='table-title', children=['ROE']),
                html.Td(id='', className='percent-common', children=['51.5']),
                html.Td(id='', className='table-title', children=['Face Value']),
                html.Td(id='', className='rupee-common', children=['1.00']),
            ])
            
        ]),
        html.Div(id='bottom-details', className='bottom-details', children=[
            html.Div(id='input-bottom', className='input-bottom', children=[
                html.H4(id='', className='ratio-to-table-title', children='Add ratio to table'),
            dcc.Input(className='input-box',placeholder="eg. Promoter holding"),
            ]),
            html.A(id='', className='Edit-button', children=[html.H3(id='', className='Edit-Ratio', children='Edit Ratio')],href='') 
        ])
        
        
    ])
    
    
])
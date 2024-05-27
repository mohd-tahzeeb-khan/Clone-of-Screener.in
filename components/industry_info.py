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
            html.Tr(id='', className='', children=[
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
            html.Tr(id='', className=' center-row', children=[
                html.Td(id='', className='table-title', children=['Stock P/E']),
                html.Td(id='', className='stockpe', children=['29.7']),
                html.Td(id='', className='table-title', children=['Book Value']),
                html.Td(id='', className='rupee-common', children=['250']),
                html.Td(id='', className='table-title', children=['Dividend Yield']),
                html.Td(id='', className='percent-common', children=['1.26']),
            ]),
            html.Tr(id='', className='', children=[
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
        
        
    ]),
    html.Div(id='', className='bottom-right-corner', children=[
        html.Div(id='', className='', children=[
            html.H4(id='', className='', children='About'),
            html.P("Tata Consultancy Services is the flagship company and a part of Tata group. It is an IT services, consulting and business solutions organization that")
            
        ]),
        html.Div(id='', className='', children=[
            html.H3(id='', className='', children='Key Points'),
            html.H4(id='', className='', children='Revenue Breakup Q2FY24'),
            html.H4(id='', className='', children=['BFSI: ',html.Span(id='', className='', children=[html.H4(id='', className='', children='32.6'),])]),
            
            html.A(id='', className='', children=["Read More"], href='')
        ])
    ]),

    
    
])

# -------------------------------------------------Pros - Cons-------------------------------------------------

Pros_Cons=html.Div(id='ProsCons', className='ProsCons', children=[
    html.Div(id='', className='row', children=[
        html.Div(id='Pro_left', className='Pro_left', children=[
        html.H1(id='Pros-title', className='Pros-title', children='Pros'),
        html.Ul(id='', className='', children=[
            html.Li(id='', className='', children=[
                i
            ]) for i in ['Company is almost debt free.',
                          'Company has a good return on equity (ROE) track record: 3 Years ROE 47.4%', 
                          'Company has been maintaining a healthy dividend payout of 66.2%']
            
        ])
    ]),
    html.Div(id='Cons_right', className='Cons_right', children=[
        html.H1(id='Cons-title', className='Cons-title', children='Cons'),
        html.Ul(id='', className='', children=[
            html.Li(id='', className='', children=[
                i
            ]) for i in ['Stock is trading at 15.4 times its book value', 'Promoter holding has decreased over last quarter: -0.64%', 'The company has delivered a poor sales growth of 10.5% over past five years.']
            
        ])
    ]),
    ]),
    html.Div(id='', className='row', children=[
        html.Span(id='', className='bottom-text', children=['The pros and cons are machine generated.',])
    
    ])
    
])
peer_table=html.Div(id='main-peer-table', className='main-peer-table', children=[
    html.Div(id='main-peer-title', className='main-peer-title', children=[
        html.H2(id='', className='peer-title', children='Peer comparison')
    ]),
    html.Div(id='peer-table-row-2', className='peer-table-row-2', children=[
        html.Div(id='peer-left', className='peer-left', children=[
            html.Div(id='', className='', children=[
                html.H4(id='', className='', children='Sector:'),
                html.Span(id='', className='', children=["IT-Sector"])
                
            ]),
            html.Div(id='', className='', children=[
                html.H4(id='', className='', children='Industry:'),
                html.Span(id='', className='', children=["unknown"])
                
            ])
            
        ]),
        html.Div(id='peer-edit-button-right', className='peer-edit-button-right', children=[
            html.A(id='peer-edit-button', className='peer-edit-button', children=["Edit Button"], href='')
        ])
        
    ]),
    html.Div(id='peer-table-row-3', className='3', children=[
        html.Table(id='', className='', children=[
            html.Thead(id='', className='', children=[
                html.Th(id='srno', className='table-heading', children='Srno'),
                html.Th(id='name', className='table-heading', children='Name'),
                html.Th(id='CMP', className='table-heading', children='CMP Rs.'),
                html.Th(id='PE', className='table-heading', children='P/E'),
                html.Th(id='MARCAP', className='table-heading', children='Mar Cap Rs.Cr.'),
                html.Th(id='DIV', className='table-heading', children='Div Yld%'),
                html.Th(id='NP', className='table-heading', children='NP Qtr Rs.Cr'),
                html.Th(id='QTR', className='table-heading', children='Qtr Profit Var %'),
                html.Th(id='SALESCR', className='table-heading', children='Sales Qtr Rs.Cr.'),
                html.Th(id='SALESVAR', className='table-heading', children='Qtr Sales Var %'),
            ]),
        ])
        
    ]),
    html.Div(id='peer-table-row-4', className='peer-table-row-4', children=[
        
    ])
    
])
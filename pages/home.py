from dash import dcc, html
import dash_bootstrap_components as dbc

layout = dbc.Container([
    html.Div([
        dbc.Row([
            dbc.Col(html.H2("AI-Generated Content Detector"),
                    className="header_title"
            ),
        ]),
        dbc.Row([
            dbc.Col(html.P(
                children="""AI-Generated Content Detector analyzes text and gives a score indicating how much of it is AI-generated or human-written, helping users assess content authenticity.""",
            ),
            className="header_description"),
        ]),
    ], className='header'),
    html.Div([
        dbc.Row([
            dbc.Col(dbc.Textarea(
                id='text',
                placeholder="Enter Text Here",
                className="custom-textarea", 
                style={'width': '100%', 'height': 450, 'font-size': '18px'},  
            ), width={"size": 8, "offset": 2}),  
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Upload(id='upload_file', children=[
                    'Upload File ',
                    html.A('(.txt, .docx, .pdf)'),
                ], multiple=False,
                    className='upload-style')
            ], width={"size": 8, "offset": 2}),  # Increased width
        ],
        ),
        dbc.Row([
            dbc.Col(html.H5('Human'), width=4, style={'text-align': 'right', 'color': 'green'}),
            dbc.Col(dcc.Loading(id='loading', children=html.Div(''),
                                type="default"),
                    width=4),
            dbc.Col(html.H5('AI Generated', className="text-danger"), width=4, style={'text-align': 'left'}),
        ], style={'margin-top': '20px'}),
        dbc.Row([
            dbc.Col(dbc.Progress(
                [
                    dbc.Progress(id="real_prog", value=50, color="success", bar=True),
                    dbc.Progress(id="fake_prog", value=50, color="danger", bar=True),
                ], style={'height': '25px', 'font-size': '16px'}
            ), width={"size": 8, "offset": 2}),  # Increased width
        ]),
    ], className='card'),
    html.Div([
        dbc.Row([
            dbc.Col(html.P(
                children="""Disclaimer: This tool provides an estimated AI-generated content score based on linguistic patterns and statistical analysis. While it strives for accuracy, it may not always be 100% precise. Results should be interpreted with caution and not used as definitive proof of authorship.""",
                className="disclaimer-text"
            ), width={"size": 8, "offset": 2}),
        ], style={'margin-top': '20px', 'text-align': 'center'})
    ])
])

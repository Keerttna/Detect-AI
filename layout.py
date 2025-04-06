from dash import dcc, html
import dash_bootstrap_components as dbc


class AppLayout:
    def __init__(self):
        self.content =  self.generateContentLayout()
        self.sidebar =  self.generateSidebarLayout()
    

    def generateSidebarLayout(self):
        sidebar = html.Div(
            className='sidebar',
            children=[
                    dbc.Nav([
                            dbc.NavLink("Home", href="/", id="page-1-link", active="exact", style={'text-align' : 'center'}),
                        ], vertical=True, pills=True
                    ),
            ],
            style={'display': 'none'}
        )
        return sidebar
    
    def generateContentLayout(self):
        content = html.Div(id="page-content", className='content')
        return content
    
    
    def getAppLayout(self):
        layout = html.Div(children=[dcc.Location(id="url", refresh=False), self.sidebar, self.content])
        return layout

    
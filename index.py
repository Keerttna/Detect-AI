# python-3.10.9

import dash_bootstrap_components as dbc
from dash import Dash
from layout import AppLayout
from app_callback import AppCallback

styles = [dbc.themes.BOOTSTRAP]
app = Dash(name = __name__, external_stylesheets=styles)
app.title = "AI Content Detector"
app.config["suppress_callback_exceptions"] = True
server = app.server

layout = AppLayout()
app.layout = layout.getAppLayout()
AppCallback(app)


if __name__ == "__main__":
    app.run_server(debug=False)
from dash import dcc
from dash import html
import dash
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(children = [
    # Navbar
    html.Div(children = [
        html.H1(children='CrisprHelper', style={'flex-grow': '4', 'margin-line-start': '20px'}),

        html.Nav(className = "nav nav-pills", children=[
            html.A('Home', className="nav-item nav-link btn", href='/apps/Home'),
            html.A('Contact', className="nav-item nav-link active btn", href='/apps/Contact'),
            html.A('About', className="nav-item nav-link active btn", href='/apps/About')  
        ], style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'flex-end', 'gap': '30px', 'margin-inline-end':'20px'})
    ], style={'display': 'flex', 'align-items': 'center'}),

    # Divider Line
    html.Hr(),

    html.Div(children = [
        # Description
        html.P(children='Insert a cool description of the tool here'),

        # TODO: Add inputs/dropdowns here!

        # Submit Button
        html.Button('Submit', id='submit-val', n_clicks=0)
    ], style={'display': 'flex', 'flex-flow': 'column', 'justify-content': 'center', 'align-items': 'center'})
]
)

@app.callback(
    Output("out-all-types", "children"),
    [Input("input_sequence", "value")],
)
def cb_render(*vals):
    return " | ".join((str(val) for val in vals if val))


if __name__ == "__main__":
    app.run_server(debug=True)

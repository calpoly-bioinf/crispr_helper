from dash import dcc
from dash import html
import dash
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(
    [
        dcc.Input(
            id="input_sequence",
            type="text",
            placeholder="input type text",
        )
    ]
    + [html.Div(id="out-all-types")]
)


@app.callback(
    Output("out-all-types", "children"),
    [Input("input_sequence", "value")],
)
def cb_render(*vals):
    return " | ".join((str(val) for val in vals if val))


if __name__ == "__main__":
    app.run_server(debug=True)

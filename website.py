import base64
import datetime
import io

from dash import dcc, html, dash_table
import dash
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select FASTA Files')
        ]),
        style={
            'width': '70%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-data-upload'),
])

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')
    print(f'name:{type(filename)}\n{filename}\n')
    print(f'type:{type(content_type)}\n{content_type}\n')
    print(f'string:{type(content_string)}\n{content_string}\n')
    decoded = decode_file_content(content_string)
    print(f'decoded:{decoded}\n')
    #seq1 = SeqIO.parse(decoded, "fasta")
    #print(f'seq parsed {seq1}')
    seq_str = str(decoded)
    print(f'seq_str: {seq_str}')
    #split into lines for output as P's
    seq_arr = seq_str.split('\n')
    #replace \n
    seq_arr = [x.replace("\n", " ") for x in seq_arr]
    print('seq_arr')
    for line in seq_arr:
        print(line)
    '''
    try:
        
        seq = SeqIO.read(decoded, "fasta")
        print(f'\n\nseq:{seq}')
    except Exception as e:
        print(e)
        return html.Div([
            'Error processing file upload'
        ])
    '''
    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        html.Div([
            html.P(line)
            for line in seq_arr
        ]),
        html.Hr(),

        #debugging content
        html.Div('Raw Content'),
        html.Pre(contents[0:100] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })

        ])


def decode_file_content(file: str) -> str:
	"""
	Decode file content from base64 to ascii
	Parameters
	----------
	file: str, required
		A base64 encoded str

	Returns
	-------
	result:
		A decoded str
	"""
	return base64.b64decode(file.split(',')[-1].encode('ascii')).decode()


# @app.callback(
#     Output("out-all-types", "children"),
#     [Input("input_sequence", "value")],
# )
# def cb_render(*vals):
#     return " | ".join((str(val) for val in vals if val))

@app.callback(Output('output-data-upload', 'children'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
    State('upload-data', 'last_modified'))

def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children


if __name__ == "__main__":
    app.run_server(debug=True)

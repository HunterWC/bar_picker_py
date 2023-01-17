
import dash
from dash import dcc
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Bar Picker"),
        html.P(
            children='''
            Filter for best bar in Knoxville 
            and give option to randomly select one
            ''',
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)



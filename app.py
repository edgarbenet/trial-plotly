# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

#fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


#from utils import get_data

data_raw = [{'name': 'Nicole', 'drink': 'Coke Zero'}, {'name': 'Drew',
                                                   'drink': 'Mountain Dew'}, {'name': 'Nicole', 'drink': 'Mountain Dew'}]

# for i, rel in enumerate(data):
#     pass


names = ['Nicole', 'Drew']
drinks = ['Coke Zero', 'Mountain Dew']
print(names+drinks)


node = dict(pad=30,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=names+drinks,
            customdata=["Ms. Nicole", "Mr. Drew",
                        "Coke Zero (with has those properties)", "Mountain Dew (with those properties)"],
            hovertemplate='The person: %{customdata} likes %{value}<extra></extra>',
            color="blue"
            )
print(node)
link = dict(
    # indices correspond to labels, eg A1, A2, A1, B1, ...
    source=[1, 0, 0],  # len(data)
    target=[3, 2, 3],
    value=[2, 4, 8],
    customdata=["A LITTLE ", "QUITE A LOT", "A LOT"],
    hovertemplate='Link from %{source.customdata}, who likes the product %{target.customdata} that much: %{value}' +
    '<br />which means that he likes it %{customdata}<extra></extra>',)

data = go.Sankey(node=node, link=link)

fig = go.Figure(data=data)
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

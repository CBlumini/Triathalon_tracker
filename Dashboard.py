import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from dash import dash_table
import pandas as pd
import sqlite3
from sqlalchemy import create_engine

#import plotly.graph_objs as go
engine = create_engine('sqlite:///data.db', echo=False)
sql_df = pd.read_sql('data.db', con=engine, index_col='ID')

#df = df[['country', 'description', 'rating', 'price','province','title','variety','winery','color']]
print(sql_df.head(1))

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])
server = app.server
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Graph(figure=fig)])

#set the app.layout
# app.layout = html.Div([
#     dcc.Tabs(id="tabs", value='tab-1', children=[
#         dcc.Tab(label='Tab one', value='tab-1'),
#         dcc.Tab(label='Tab two', value='tab-2'),
#     ]),
#     html.Div(id='tabs-content')
# ])

print("hello")
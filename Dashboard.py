import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from dash import dash_table
import pandas as pd
from sqlalchemy import create_engine
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_excel('santa_cruz_data.xlsx', header = 0, index_col=None)
print(data.head())

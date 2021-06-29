import plotly.graph_objects as go
import urllib.request
import json

from utils import get_data


data = get_data()

# override gray link colors with 'source' colors
opacity = 0.4
# change 'magenta' to its 'rgba' value to add opacity
data['data'][0]['node']['color'] = [
    'rgba(255,0,255, 0.8)' if color == "magenta" else color for color in data['data'][0]['node']['color']]
data['data'][0]['link']['color'] = [data['data'][0]['node']['color'][src].replace("0.8", str(opacity))
                                    for src in data['data'][0]['link']['source']]




data = [go.Sankey(
    valueformat=".0f",
    valuesuffix="TWh",
    # Define nodes
    node=dict(
        pad=15,
        thickness=15,
        line=dict(color="black", width=0.5),
        label=data['data'][0]['node']['label'],
        color=data['data'][0]['node']['color']
    ),
    # Add links
    link=dict(
        source=data['data'][0]['link']['source'],
        target=data['data'][0]['link']['target'],
        value=data['data'][0]['link']['value'],
        label=data['data'][0]['link']['label'],
        color=data['data'][0]['link']['color']
    ))]
    
fig = go.Figure(data=data)

fig.update_layout(title_text="Energy forecast for 2050<br>Source: Department of Energy & Climate Change, Tom Counsell via <a href='https://bost.ocks.org/mike/sankey/'>Mike Bostock</a>",
                  font_size=10)
fig.show()


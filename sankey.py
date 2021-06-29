import plotly.graph_objects as go


#from utils import get_data

node = dict(pad=30,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=["0","1", "2", "3", "4", "5"],
            customdata=["Long name 0", "Long name 1", "Long name 2", "Long name 3",
                        "Long name 4", "Long name 5"],
            hovertemplate='Node %{customdata} has total value %{value}<extra></extra>',
            color="blue"
            )
print(node)
link = dict(
    # indices correspond to labels, eg A1, A2, A1, B1, ...
    source=[0, 1, 0, 2, 3, 3],
    target=[2, 3, 3, 4, 4, 5],
    value = [8, 4, 2, 8, 4, 2],
    customdata=["q", "r", "s", "t", "u", "v"],
    hovertemplate='Link from node %{source.customdata}<br />' +
    'to node%{target.customdata}<br />has value %{value}' +
    '<br />and data %{customdata}<extra></extra>',)
    
data = go.Sankey(node=node, link=link)

fig = go.Figure(data=data)

fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
fig.show()

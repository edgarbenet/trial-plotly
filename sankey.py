import plotly.graph_objects as go


#from utils import get_data

node = dict(pad=30,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=["0","1", "2", "3", "4", "5"],
            color="blue"
            )
print(node)
link = dict(
    # indices correspond to labels, eg A1, A2, A1, B1, ...
    source=[0, 1, 0, 2, 3, 3],
    target=[2, 3, 3, 4, 4, 5],
    value = [8, 4, 2, 8, 4, 2])
    
data = go.Sankey(node=node, link=link)

fig = go.Figure(data=data)

fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
fig.show()

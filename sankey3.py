import plotly.graph_objects as go


#from utils import get_data

data = [{'name': 'Nicole', 'drink': 'Coke Zero'}, {'name': 'Drew','drink': 'Mountain Dew'}, {'name': 'Nicole', 'drink': 'Mountain Dew'}]

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
    source=[1, 0, 0], #len(data)
    target=[3, 2, 3],
    value=[2, 4, 8],
    customdata=["A LITTLE ", "QUITE A LOT", "A LOT"],
    hovertemplate='Link from %{source.customdata}, who likes the product %{target.customdata} that much: %{value}' +
    '<br />which means that he likes it %{customdata}<extra></extra>',)

data = go.Sankey(node=node, link=link)

fig = go.Figure(data=data)

fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
fig.show()

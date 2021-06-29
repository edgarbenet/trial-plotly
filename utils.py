import json
import urllib.request


def get_data():
    url = 'https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json'
    response = urllib.request.urlopen(url)
    
    data = json.loads(response.read())

    return data
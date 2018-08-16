from flask import Flask, render_template
from .data import gather
import json
import plotly
import pandas as pd

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    data = gather()
    entries_df = pd.DataFrame(data=data['entries'])
    entries_df = entries_df.drop(columns=['place', 'fullname', 'birthday', 'number'])
    entries_df = entries_df[entries_df['region'] != 'undefined']
    entries_df['bin'] = pd.cut(entries_df['age'], [15, 20, 25, 30, 35, 40],
                               labels=['15-20', '20-25', '25-30', '30-35', '35-40'])
    age_bins = entries_df['bin'].value_counts()
    region_counts = entries_df['region'].value_counts()
    anchors = region_counts.index

    graphs = [
        dict(
            data=[
                dict(
                    y=region_counts,
                    x=anchors,
                    text=list(region_counts),
                    name='Регионы',
                    type='bar'
                )
            ]
        ),
        dict(
            data=[
                dict(
                    y=age_bins,
                    x=age_bins.index,
                    text=list(age_bins),
                    name='Возраст',
                    type='bar'
                )
            ]
        )
    ]

    # Add "ids" to each of the graphs to pass up to the client
    # for templating
    ids = [d['data'][0]['name'] for i, d in enumerate(graphs)]

    # Convert the figures to JSON
    # PlotlyJSONEncoder appropriately converts pandas, datetime, etc
    # objects to their JSON equivalents
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('layouts/index.html',
                           ids=ids,
                           graphJSON=graphJSON)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)

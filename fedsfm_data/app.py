from flask import Flask, render_template

import json
import plotly
import pandas as pd
import numpy as np

app = Flask(__name__)
app.debug = True

from .data import gather


@app.route('/')
def index():
    data = gather()
    entries_df = pd.DataFrame(data=data["entries"])
    entries_df = entries_df.drop(columns=["place", "fullname", "birthday", "number"])
    entries_df = entries_df.groupby(['region']).sum()
    graphs = [
        dict(
            data=[
                dict(
                    x=entries_df.index,  # Can use the pandas data structures directly
                    y=entries_df,
                    type="bar"
                )
            ]
        )
    ]

    # Add "ids" to each of the graphs to pass up to the client
    # for templating
    ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]

    # Convert the figures to JSON
    # PlotlyJSONEncoder appropriately converts pandas, datetime, etc
    # objects to their JSON equivalents
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('layouts/index.html',
                           ids=ids,
                           graphJSON=graphJSON)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)

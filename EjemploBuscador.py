# https://plotly.com/python/parallel-coordinates-plot/
# https://plotly.com/python/colorscales/
# https://plotly.com/python/figure-labels/

import plotly.graph_objects as go


def ejemplohtml():
    fig = go.Figure(data=
    go.Parcoords(
        line_color='blue',
        dimensions=list([
            dict(range=[1, 5],
                 constraintrange=[1, 2],  # change this range by dragging the pink line
                 label='A', values=[1, 4]),
            dict(range=[1.5, 5],
                 tickvals=[1.5, 3, 4.5],
                 label='B', values=[3, 1.5]),
            dict(range=[1, 5],
                 tickvals=[1, 2, 4, 5],
                 label='C', values=[2, 4],
                 ticktext=['text 1', 'text 2', 'text 3', 'text 4']),
            dict(range=[1, 5],
                 label='D', values=[4, 2])
        ])
    )
    )

    fig.update_layout(
        title={
            'text': "Plot Title",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})

    fig.show()

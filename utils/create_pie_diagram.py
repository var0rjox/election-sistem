import plotly.graph_objs as go
from models.result_report import ResultReport


def create_pie_diagram(results):
    result_report = ResultReport()
    data = result_report.getDataForPieDiagram(results)
    labels = data["labels"]
    values = data["values"]

    diagram = go.Pie(labels=labels, values=values)
    layout = go.Layout(
        title="",
        margin=dict(l=0, r=0, t=30, b=0),
    )
    figure = go.Figure(data=[diagram], layout=layout)

    json_diagram = figure.to_json()

    return json_diagram

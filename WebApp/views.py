import json
import tempfile
from io import StringIO

import numpy as np
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView


def demo(request):
    return render(request, 'demo.html', {})


import os

import plotly.graph_objects as go

openposeOutputDirectory = "D:\DystoniaCoalition\OpenPose100\\"
openposeOutputsMain = os.listdir(openposeOutputDirectory)[1]  # single folder


class Graph(TemplateView):
    template_name = 'demo.html'

    def get_context_data(self, **kwargs):
        context = super(Graph, self).get_context_data(**kwargs)

        x = [-2, 0, 4, 6, 7]
        y = [q ** 2 - q + 3 for q in x]
        trace1 = go.Scatter(x=x, y=y, marker={'color': 'red', 'symbol': 104, 'size': 10},
                            mode="lines", name='1st Trace')

        layout = go.Layout(title="Meine Daten", xaxis={'title': 'x1'}, yaxis={'title': 'x2'})
        figure = go.Figure(data=[trace1], layout=layout)

        context['graph'] = PlotSingleMP4Json(openposeOutputsMain)

        return context


import os


# @cache_page(60 * 60 * 15)
def MP4toJson(mp4JsonFolder):
    mp4foldername = os.path.join(openposeOutputDirectory, mp4JsonFolder)
    openposeOutputs = os.listdir(mp4foldername)

    mp4toJSON = []

    for idx, filex in enumerate(openposeOutputs):
        frameNumber = int(filex.split('_')[2])
        data = json.load(open(os.path.join(mp4foldername, filex)))
        peoples_frame = []
        for people in data['people']:
            peopleCoordinate = []
            for i in range(0, 75, 3):
                if not [people['pose_keypoints_2d'][i], people['pose_keypoints_2d'][i + 1]] == [0, 0]:
                    peopleCoordinate.append(
                        [people['pose_keypoints_2d'][i], people['pose_keypoints_2d'][i + 1], np.floor((i + 1) / 3)])
            peoples_frame.append(peopleCoordinate)
        # if (len(data['people'])!=1):
        #     print(len(data['people']))
        mp4toJSON.append([frameNumber, peoples_frame])

    # for i in bones:
    #     bone_each.append(i) if all(x in [d['i'] for d in poses[0][0]] for x in i) else None
    # mp4toJSON
    return len(openposeOutputs), mp4toJSON


import plotly.express as px


# @cache_page(60 * 60 * 15)
def PlotSingleMP4Json(mp4JsonFolderName):
    import plotly.graph_objects as go
    import plotly.tools as tls

    # for idv, eachFrame in enumerate(mp4toJSON[0:5]): #change
    # for p in eachFrame:
    # fig, ax = plt.subplots()
    # ax.set_ylim(ax.get_ylim()[::-1])
    # ax.scatter([e[0]  for e in p], [e[1] for e in p] )

    TotalFrames, JsonDict = MP4toJson(mp4JsonFolderName)

    #
    # for idx, eachFrame in enumerate(JsonDict):
    #     for p in eachFrame[1]:
    #         for e in p:
    #             s = e[0]
    #             pass

    fig = px.scatter(x=[e[0] for idx, eachFrame in enumerate(JsonDict) for p in eachFrame[1] for e in p],
                     y=[e[1] for idx, eachFrame in enumerate(JsonDict) for p in eachFrame[1] for e in p],
                     range_x=[0, 640], range_y=[480, 0],
                     animation_frame=[idx for idx, eachFrame in enumerate(JsonDict) for p in eachFrame[1] for e
                                      in p],
                     animation_group=[pidx for idx, eachFrame in enumerate(JsonDict) for p in eachFrame[1] for
                                      pidx in
                                      enumerate(p)],
                     width=640, height=480)

    post_script = '''
                gd = document.getElementById('{plot_id}');
                TotalFrames = ''' + str(TotalFrames) + ''';
                console.log("hi");
            '''

    # fig.show()
    with StringIO() as path:
        # with os.fdopen(figureVar, 'w') as f:
        #     # f.write('TEST\n')
        fig.write_html(file=path, post_script=post_script, full_html=False, include_plotlyjs='cdn', )
        path.seek(0)
        return path.read()


def list(request):
    # D:\DystoniaCoalition\scripts\videoProfile.ipynb
    df = pd.read_csv("D:\\DystoniaCoalition\\processed\\videoProfile.csv")
    table_html = df.to_html(escape=False)
    return render(request, 'list.html', {"table": table_html[:7] + 'id="%s" ' % "example" + table_html[7:]})


def Profiling(request):
    return HttpResponse(open("D:/DystoniaCoalition/processed/pandasProfiling.html").read())

from collections import Counter
from functools import lru_cache
from io import StringIO
from math import ceil, floor

import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView
from numpy import nan
from tinydb import TinyDB

from WebApp.models import VideoAnnotations
from WebApp.utils import MP4toJson


def demo(request):
    return render(request, 'demo.html', {})


import os

videoProfile = None


def getvideoProfile():
    global videoProfile
    if videoProfile is None:
        videoProfile = pd.read_csv("D:\\DystoniaCoalition\\processed\\videoProfile.csv")
    return videoProfile


openposeOutputDirectory = "D:\DystoniaCoalition\OpenPose100\\"
openposeOutputsMain = os.listdir(openposeOutputDirectory)[1]  # single folder


class Graph(TemplateView):
    template_name = 'demo.html'

    def get_context_data(self, **kwargs):
        context = super(Graph, self).get_context_data(**kwargs)
        context['graph'], JSONDict = PlotSingleMP4Json(openposeOutputsMain)
        return context


tinyDB = TinyDB("D:/DystoniaCoalition/DystViz/NeckMovement_db.json")
NeckMovement = tinyDB.table('NeckMovement')


def SingleGraph(request, projectID):
    if request.method == 'POST':
        # // parse next and previous
        if (request.POST.get('startV')).isdigit() and (request.POST.get('endV').isdigit()):

            obj, created = VideoAnnotations.objects.get_or_create(pid=projectID, type="NeckMovement")

            obj.start = int(request.POST.get('startV'))
            obj.end = int(request.POST.get('endV'))
            obj.save()
            # NeckMovement.upsert(Document({"pid": projectID,
            #                               'startV': int(request.POST.get('startV')),
            #                               'endV': int(request.POST.get('endV'))},
            #                              # //condition
            #                              doc_id=projectID))
            print("saved: ", obj)

            return HttpResponse("Success")
        else:
            return HttpResponse("Please select both start and end time", status=500)

    context = {}
    df = getvideoProfile()
    singleF = df[df['PID'] == projectID]
    # TODO: get next element and send to context
    fileName = singleF['NAME'].values[0]
    context['PID'] = projectID
    context['nextPID'] = int(df.loc[[(int(singleF.index.values) + 1) % len(df)]]['PID'].values)
    context['prevPID'] = int(df.loc[[(int(singleF.index.values) - 1) % len(df)]]['PID'].values)
    context['graph'], JSONDict = PlotSingleMP4Json(fileName)

    ListOfScatterPlots = [{"data": CoordinateToChange(JSONDict), "name": "Cnt", "mode": "markers", },
                          {"data": EstimateCLasses(JSONDict), "name": "SmthCnt", "mode": "markers", },
                          # {"data": IfFeaturePoll(JSONDict), "name": "IfNeck", "mode": "markers", },
                          {"data": HeadAngle(JSONDict), "name": "HeadAngle", "mode": "markers", },
                          ]

    context['MultipleScatterPlots'] = MultipleScatterPlots(ListOfScatterPlots)
    context['fileName'] = fileName

    context['singleF'] = singleF.T.to_html(escape=False, border=0)

    NeckMovementData = VideoAnnotations.objects.filter(pid=projectID, type="NeckMovement")
    if (NeckMovementData):
        context['startV'] = NeckMovementData[0].start
        context['endV'] = NeckMovementData[0].end
    return render(request, 'demo.html', context)


# @cache_page(60 * 60 * 15)


import plotly.express as px


# @cache_page(60 * 60 * 15)
@lru_cache(maxsize=500)
def PlotSingleMP4Json(mp4JsonFolderName):
    # for idv, eachFrame in enumerate(mp4toJSON[0:5]): #change
    # for p in eachFrame:
    # fig, ax = plt.subplots()
    # ax.set_ylim(ax.get_ylim()[::-1])
    # ax.scatter([e[0]  for e in p], [e[1] for e in p] )

    TotalFrames, JsonDict = MP4toJson(mp4JsonFolderName, openposeOutputDirectory)

    #
    # for idx, eachFrame in enumerate(JsonDict):
    #     for p in eachFrame[1]:
    #         for e in p:
    #             s = e[0]
    #             pass

    data = {'x': [e[0] for idx, eachFrame in enumerate(JsonDict) for p in eachFrame[1] for e in p],
            'y': [e[1] for idx, eachFrame in enumerate(JsonDict) for p in eachFrame[1] for e in p],
            'animation_frame': [idx for idx, eachFrame in enumerate(JsonDict) for p in eachFrame[1] for e in p],
            "animation_group": [pidx for idx, eachFrame in enumerate(JsonDict) for p in eachFrame[1] for pidx in
                                enumerate(p)],
            "point": [e[2] for idx, eachFrame in enumerate(JsonDict) for p in eachFrame[1] for e in p]
            }

    df = pd.DataFrame(data)
    # df.columns = ['x', 'y', 'animation_frame', "animation_group"]
    fig = px.scatter(df, x="x", y="y", animation_frame="animation_frame", animation_group="animation_group",
                     range_x=[0, 640], range_y=[480, 0],
                     width=640, height=480, hover_data=['point'])

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
        return path.read(), JsonDict


def listView(request):
    # D:\DystoniaCoalition\scripts\videoProfile.ipynb
    df = getvideoProfile()
    df = df.drop(['NAME', ], axis=1)
    df['NeckData'] = df['PID'].apply(lambda x:
                                     str(VideoAnnotations.objects.filter(pid=x,
                                                                         type="NeckMovement").first().start) + "-" + str(
                                         VideoAnnotations.objects.filter(pid=x,
                                                                         type="NeckMovement").first().end) + " :ANNTD"
                                     if VideoAnnotations.objects.filter(
                                         pid=x, type="NeckMovement") else None
                                     )
    df['PID'] = df['PID'].apply(lambda x: '<a href="/SingleGraph/' + str(x) + '">' + str(x) + '</a>')

    table_html = df.to_html(escape=False)
    return render(request, 'list.html', {"table": table_html[:7] + 'id="%s" ' % "example" + table_html[7:]})


def Profiling(request):
    return HttpResponse(open("D:/DystoniaCoalition/processed/videoProfiling.html").read())


import plotly.graph_objects as go


def MultipleScatterPlots(DataList):
    with StringIO() as path:
        fig = go.Figure()
        for data in DataList:
            fig.add_trace(go.Scatter(y=data["data"], mode=data["mode"], name=data["name"]))
        fig.write_html(file=path, full_html=False, include_plotlyjs='cdn')
        path.seek(0)
        return path.read()


def CoordinateToChange(Coordinates):
    for idx, eachFrame in enumerate(Coordinates):
        data = (eachFrame[1][0], len(eachFrame[1]))
    x = [i[0] for i in Coordinates]
    y = [len(i[1][0]) for i in Coordinates]
    # most_common = Counter(y).most_common(5)

    return y


from numpy.lib.stride_tricks import sliding_window_view

wlen = 30


def EstimateCLasses(Coordinates):
    arr = [len(i[1][0]) for i in Coordinates]
    left = [nan] * ceil(wlen / 2)
    left.extend(arr)
    right = [nan] * floor(wlen / 2)
    left.extend(right)
    new = [Counter(e[e != 0]).most_common(1)[0][0] if len(e[e != 0]) else 0
           for e in sliding_window_view(left, wlen)]
    pass
    #
    # x = [i[0] for i in Coordinates]
    # y = [len(i[1][0]) for i in Coordinates]
    return new


def IfFeaturePoll(jsonDict):
    ifFeaturePoll = []
    for frame in jsonDict:
        for keypoints in frame[1]:  # like each person ; keypoints has t
            pointDict = {int(x[2]): {"x": x[0], "y": x[1]} for x in keypoints}
            # if pointDict.get(18) and pointDict.get(0):
            #     dif = abs(pointDict.get(18).get('x') - pointDict.get(0).get('x')) / abs(
            #         pointDict.get(18).get('y') - pointDict.get(0).get('y'))
            # elif pointDict.get(17) and pointDict.get(0):
            #     dif = abs(pointDict.get(17).get('x') - pointDict.get(0).get('x')) / abs(
            #         pointDict.get(17).get('y') - pointDict.get(0).get('y'))
            if pointDict.get(2) and pointDict.get(12) and pointDict.get(5) and pointDict.get(9):
                if (pointDict.get(2).get('x') > pointDict.get(12).get('x') and pointDict.get(5).get(
                        'x') > pointDict.get(9).get('x')) or \
                        (pointDict.get(2).get('x') < pointDict.get(12).get('x') and pointDict.get(5).get(
                            'x') < pointDict.get(9).get('x')):
                    ifFeaturePoll.append(1)
                else:
                    ifFeaturePoll.append(0)
            else:
                ifFeaturePoll.append(0)

            # # elif pointDict.get(17) and pointDict.get(0):
            #     dif = abs(pointDict.get(17).get('x') - pointDict.get(0).get('x')) / abs(
            #         pointDict.get(17).get('y') - pointDict.get(0).get('y'))
            # else:
            #     dif = 0
            # if dif < 1:
            #     dif = 0
            # else:
            #     dif = 1
            # ifFeaturePoll.append(dif)
    # itertools.groupby(ifFeaturePoll)
    return ifFeaturePoll


import math


def dot(vA, vB):
    return vA[0] * vB[0] + vA[1] * vB[1]


def ang(lineA, lineB):
    # Get nicer vector form
    vA = [(lineA[0]['x'] - lineA[1]['x']), (lineA[0]['y'] - lineA[1]['y'])]
    vB = [(lineB[0]['x'] - lineB[1]['x']), (lineB[0]['y'] - lineB[1]['y'])]
    # Get dot prod
    dot_prod = dot(vA, vB)
    # Get magnitudes
    magA = dot(vA, vA) ** 0.5
    magB = dot(vB, vB) ** 0.5
    # Get cosine value
    cos_ = dot_prod / magA / magB
    # Get angle in radians and then convert to degrees
    angle = math.acos(dot_prod / magB / magA)
    # Basically doing angle <- angle mod 360
    ang_deg = math.degrees(angle) % 360

    if ang_deg - 180 >= 0:
        # As in if statement
        return 360 - ang_deg
    else:

        return ang_deg


def HeadAngle(jsonDict):
    HeadAngle = []
    for frame in jsonDict:
        for keypoints in frame[1]:  # like each person ; keypoints has t
            pointDict = {int(x[2]): {"x": x[0], "y": x[1]} for x in keypoints}

            if pointDict.get(0) and pointDict.get(1) and pointDict.get(2):
                line1 = [pointDict.get(0), pointDict.get(1)]
                line2 = [pointDict.get(2), pointDict.get(1)]
                angle = ang(line1, line2)
                HeadAngle.append(angle)
                pass
    return HeadAngle


import io


def ExportNeckCSV(request):
    s = io.StringIO()
    df = pd.DataFrame(list(VideoAnnotations.objects.filter(type='NeckMovement').values('pid', 'start', 'end', )))
    df['start'] = df['start'].apply(lambda x: x * 100)
    df['end'] = df['end'].apply(lambda x: x * 100)
    df.to_csv(s)
    return HttpResponse(s.getvalue(),
                        # content_type='text/csv',
                        content_type='application/force-download')


def ComparePlots(request):
    files = os.listdir('D:\\DystoniaCoalition\\processed\\xlinePlot_and_gifs')
    data = {}

    for file in files:
        x = file.split('_')
        pid = int(x[1])
        score = int(x[3].replace('.gif', ''))
        old = list(data.get(score, []))
        old.append("\static\\xlinePlot_and_gifs\\" + file)
        data[score] = old
    # print(data)

    return render(request, 'compare.html', {'images': dict(sorted(data.items()))})


def CompareAvgPlots(request):
    files = os.listdir('D:\DystoniaCoalition\processed\\averagePLot')
    data = {}

    for file in files:
        # file.replace('.png', '').replace(" ", "")
        if 'Mean_' in file:
            name = "Mean"
        else:
            name = 'StandardDeviation'

        old = list(data.get(name, []))
        old.append("\static\\averagePLot\\" + file)
        data[name] = old
    print(data)

    return render(request, 'compareAvg.html', {'images': dict(sorted(data.items()))})

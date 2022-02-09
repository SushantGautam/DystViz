import json
from collections import deque, Counter
from io import StringIO
from math import ceil, floor

import numpy as np
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView
from numpy import nan


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


def SingleGraph(request, projectID):
    context = {}
    df = getvideoProfile()
    singleF = df[df['PID'] == projectID]
    fileName = singleF['NAME'].values[0]
    context['graph'], JSONDict = PlotSingleMP4Json(fileName)
    context['scatter'], context['most_common'] = CoordinateToChange(JSONDict)
    context['IfFeaturePoll'] = IfFeaturePoll(JSONDict)
    context['EstimateCLasses'] = EstimateCLasses(JSONDict)
    context['fileName'] = fileName

    context['singleF'] = singleF.T.to_html(escape=False, border = 0)

    return render(request, 'demo.html', context)


import os


def closest_node(node, nodes):
    nodes = np.asarray(nodes)
    dist_2 = np.sum((nodes - node) ** 2, axis=1)
    return np.argmin(dist_2)


# @cache_page(60 * 60 * 15)
def MP4toJson(mp4JsonFolder):
    mp4foldername = os.path.join(openposeOutputDirectory, mp4JsonFolder)
    openposeOutputs = os.listdir(mp4foldername)

    mp4toJSON = []

    temp_queue = deque([(0, 0)], maxlen=1)

    for idx, filex in enumerate(openposeOutputs):
        try:
            frameNumber = int(filex.split('_')[2])
        except:
            frameNumber = int(filex.split('_')[1])
        data = json.load(open(os.path.join(mp4foldername, filex)))
        peoples_frame = []
        singlePersonData = []
        peopleCoordinate = []

        if (len(data['people']) >= 1):
            if (len(data['people']) > 1):
                NeckPoints = []
                for kP in data['people']:
                    eP = kP['pose_keypoints_2d']
                    neckpoint = [(eP[i], eP[i + 1]) for i in range(0, 75, 3)][1]
                    NeckPoints.append(neckpoint)
                singlePersonData = data['people'][closest_node(temp_queue[0], NeckPoints)]['pose_keypoints_2d']
            elif (len(data['people']) == 1):
                singlePersonData = data['people'][0]['pose_keypoints_2d']
            temp_queue.append([(singlePersonData[i], singlePersonData[i + 1]) for i in range(0, 75, 3)][1])

            # for people in singlePersonData:

            for i in range(0, 75, 3):
                if not [singlePersonData[i], singlePersonData[i + 1]] == [0, 0]:
                    peopleCoordinate.append(
                        [singlePersonData[i], singlePersonData[i + 1], np.floor((i + 1) / 3)])

        peoples_frame.append(peopleCoordinate)

        # for people in singlePersonData['people']:
        #     peopleCoordinate = []
        #     for i in range(0, 75, 3):
        #         if not [people['pose_keypoints_2d'][i], people['pose_keypoints_2d'][i + 1]] == [0, 0]:
        #             peopleCoordinate.append(
        #                 [people['pose_keypoints_2d'][i], people['pose_keypoints_2d'][i + 1], np.floor((i + 1) / 3)])
        #     peoples_frame.append(peopleCoordinate)

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


def list(request):
    # D:\DystoniaCoalition\scripts\videoProfile.ipynb
    df = getvideoProfile()
    df = df.drop(['NAME', ], axis=1)
    df['PID'] = df['PID'].apply(lambda x: '<a href="/SingleGraph/' + str(x) + '">' + str(x) + '</a>')

    table_html = df.to_html(escape=False)
    return render(request, 'list.html', {"table": table_html[:7] + 'id="%s" ' % "example" + table_html[7:]})


def Profiling(request):
    return HttpResponse(open("D:/DystoniaCoalition/processed/videoProfiling.html").read())


def CoordinateToChange(Coordinates):
    for idx, eachFrame in enumerate(Coordinates):
        data = (eachFrame[1][0], len(eachFrame[1]))
    x = [i[0] for i in Coordinates]
    y = [len(i[1][0]) for i in Coordinates]

    with StringIO() as path:
        # with os.fdopen(figureVar, 'w') as f:
        #     # f.write('TEST\n')

        fig = px.scatter(y)
        most_common = Counter(y).most_common(5)
        fig.write_html(file=path,
                       # post_script=post_script,
                       full_html=False, include_plotlyjs='cdn', )
        path.seek(0)
        return path.read(), most_common


from numpy.lib.stride_tricks import sliding_window_view

wlen = 30


def EstimateCLasses(Coordinates):
    arr = [len(i[1][0]) for i in Coordinates]
    left = [nan] * ceil(wlen / 2)
    left.extend(arr)
    right = [nan] * floor(wlen / 2)
    left.extend(right)
    new = [Counter(e[e != 0]).most_common(1)[0][0] for e in
           sliding_window_view(left, wlen)]
    pass
    #
    # x = [i[0] for i in Coordinates]
    # y = [len(i[1][0]) for i in Coordinates]
    with StringIO() as path:
        fig = px.scatter(new)
        # fig.show()
        fig.write_html(file=path,
                       # post_script=post_script,
                       full_html=False, include_plotlyjs='cdn', )
        path.seek(0)
        return path.read()


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
    pass
    with StringIO() as path:
        fig = px.scatter(ifFeaturePoll)
        # fig.show()
        fig.write_html(file=path,
                       # post_script=post_script,
                       full_html=False, include_plotlyjs='cdn', )
        path.seek(0)
        return path.read()

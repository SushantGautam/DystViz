import shutil
import os
import subprocess
import datetime
import re
import glob
import time
from datetime import datetime
import json
from collections import deque
import numpy as np
from tslearn.utils import to_time_series_dataset
from tslearn.clustering import TimeSeriesKMeans
import json
import tempfile
from collections import deque, Counter
from io import StringIO
from math import ceil, floor
from numpy import nan
from numpy.lib.stride_tricks import sliding_window_view


deque_size = 1

videoDirectory = "D:\DystoniaCoalition\RawVideos\\"
openposeOutputDirectory = "D:\DystoniaCoalition\OpenPose100\\"
weaklyTagOutPutDirectory = "D:\DystoniaCoalition\weakTags"

# use a clean temp folder
tmpDirectory ="d:\.openposeTemp\\"

def closest_node(node, nodes):
    nodes = np.asarray(nodes)
    dist_2 = np.sum((nodes - node)**2, axis=1)
    return np.argmin(dist_2)


def MP4toJson(mp4JsonFolder):
    mp4foldername = os.path.join(openposeOutputDirectory, mp4JsonFolder)
    openposeOutputs = os.listdir(mp4foldername)

    mp4toJSON = []

    temp_queue = deque([(0, 0)], maxlen=1)

    for idx, filex in enumerate(openposeOutputs):
        # frameNumber = int(filex.split('_')[2])
        if not filex.split('_')[2].isdigit():
                frameNumber = int(filex.split('_')[1]) #problem with space
        else:
                frameNumber  = int(filex.split('_')[2])
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

wlen=30

series_dataset  =[]
openposeOutputsMain =  os.listdir(openposeOutputDirectory)
for id, file in enumerate(openposeOutputsMain):
        
        TotalFrames, JsonDict  = MP4toJson(file)
        # x = [i[0] for i in JsonDict]
        y = [len(i[1][0]) for i in JsonDict]
        
        arr = y
        left = [nan] * ceil(wlen / 2)
        left.extend(arr)
        right = [nan] * floor(wlen / 2)
        left.extend(right)
        y = [Counter(e[e != 0]).most_common(1)[0][0] if len(e[e != 0]) else 0  for e in
                sliding_window_view(left, wlen)]
        series_dataset.append(y)

from itertools import chain
import matplotlib.pyplot as plt

flatten_list = list(chain.from_iterable(series_dataset))
plt.hist(flatten_list, bins=25)
plt.xticks(range(1, 26))

plt.show() 
pass


        # = os.path.join(openposeOutputDirectory, file)
        # openposeOutputs =  os.listdir(mp4foldername)
        # temp_queue = deque([(0,0)], maxlen = deque_size)

        # for idx, filex in enumerate(openposeOutputs):
        #         os.system('cls')
        #         print("Processing: ",id, " : " , file)
        #         print("%.2f" %(idx*100/len(openposeOutputs)) + " of "+ str(len(openposeOutputs))+  " frames")
        #         filename = os.path.join(mp4foldername, filex)
        #         with open(filename, 'r') as f:
        #                 data = json.load(f)
        #                 if (len(data['people']) >= 1):
        #                         if (len(data['people']) > 1):
        #                                 print(len(data['people']) , filex   )
        #                                 print(videoDirectory+file )
        #                                 if (len(data['people'])>1):
        #                                         NeckPoints = []
        #                                         for kP in data['people']:
        #                                                 eP = kP['pose_keypoints_2d']
        #                                                 neckpoint = [(eP[i], eP[i+1]) for i in range(0, 75, 3)][1]
        #                                                 NeckPoints.append(neckpoint)
        #                                         data['people'][closest_node(temp_queue[0], NeckPoints)]
        #                                         temp_queue.append([(eP[i], eP[i+1]) for i in range(0, 75, 3)][1])
        #                         else:
        #                                 eP= data['people'][0]['pose_keypoints_2d']
        #                                 temp_queue.append([(eP[i], eP[i+1]) for i in range(0, 75, 3)][1])

                
        #         pass


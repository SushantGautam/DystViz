import json
import os
from collections import deque
from functools import lru_cache

import numpy as np


def closest_node(node, nodes):
    nodes = np.asarray(nodes)
    dist_2 = np.sum((nodes - node) ** 2, axis=1)
    return np.argmin(dist_2)

@lru_cache(maxsize=None)
def MP4toJson(mp4JsonFolder, openposeOutputDirectory):
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

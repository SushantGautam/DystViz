import requests
import shutil
import os
import subprocess
import datetime
import re
import glob
import time
from datetime import datetime
import pandas as pd

videoDirectory = "D:\DystoniaCoalition\RawVideos\\"
openposeOutputDirectory = "C:\DystoniaCoalition\OpenPoseFullFrame\\"

# use a clean temp folder
tmpDirectory ="d:\.openposeTemp\\"
                    
                    
# videos = ["DYS3497_20190122.mp4"]

ResumeIfAlready =  True

def extract_number(f):
    s = re.findall("\d+$",f.replace("_keypoints.json","" ))
    return (int(s[0]) if s else -1,f)


df = pd.read_csv("D:\DystoniaCoalition\processed\ExportNeckCSV.csv", index_col=0)

start = datetime.now() #for time logging
            
# videos =  os.listdir(videoDirectory)
videos =['DYS1232_20130515.mp4', 'DYS36_20170510.mp4', 'DYS311_20120126.mp4']
for idx, filex in enumerate(videos):
    lastFrameProcessed = 0 #resume openpose from last frame
    lastFrametoProcess =  -1
    totalFrames = 0
    # if  (os.path.isdir(openposeOutputDirectory + filex)):
    #      continue
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! many videos are empty - -  so that arent tagged

    
    for calibrate in [True, False]:
        if filex.endswith(".mp4"):
            filename = os.path.join(videoDirectory, filex)
            
            try:
                projectID = filex.upper().split("_")[0]
            except Exception as e:
                projectID = filex.upper().split(" ")[0]
            projectID  = projectID.replace("DYS","")
            projectID  = projectID.replace("!","")
            projectID  = projectID.replace(" ","")
            projectID  = projectID.replace(".MP4","")
            
            row = df[df['pid'] == int(projectID)]
            if not len(row):
                continue
            pass
            #get PID
            #check if PID is in DF  if not break for loop
            
            lastFrameProcessed  = int(row.start)
            lastFrametoProcess  =  int(row.end)
            
            print("Processing ", filename)
            if not (os.path.getsize(filename)> 10000): #10KB
                print("The file size is very small, inspect: "+filename )
            else:

                # File is Okey. Ready to run openpose
                os.chdir("E:\MSCProjects\mobile-gaitlab\openpose")
                
                if calibrate and ResumeIfAlready:
                    #check if OpenPose has been tried already
                    if not (os.path.isdir(openposeOutputDirectory + filex)):
                        pass #no worry. this is the first time.
                    else:
                        list_of_files  = glob.glob(openposeOutputDirectory + filex+ '/*.json')
                        lastFrameProcessed = extract_number(max(list_of_files,key=extract_number))[0]  
                        if lastFrameProcessed>= lastFrametoProcess:
                            continue
        
                    for root, dirs, files in os.walk(tmpDirectory):
                            for d in dirs: shutil.rmtree(os.path.join(root, d))
                            
                    
                cmd = ['bin\OpenPoseDemo.exe',"--video", filename, '--net_resolution', '-1x256', "--cli_verbose", "1", 
                        "--display",  "0", "--render_pose", "0", "--frame_first", str(lastFrameProcessed),
                        # "--frame_step", "100",
                        "--frame_last", str(lastFrametoProcess),
                        "-write_json", tmpDirectory if calibrate else openposeOutputDirectory + filex
                        ]
                p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
                for line in p.stdout:
                    # print(datetime.datetime.now().time(), ": ", line)
                    if "Processing frame " in str(line):
                        m = str(line)[str(line).find("Processing frame ")+17 : str(line).find("...")]
                        totalFrames = int(m.split("/")[1]) #gives total number of frames
                        lastFrameProcessed = int(m.split("/")[0])-1
                        if calibrate: 
                            p.kill()
                            print(totalFrames, " found in the video.")

                        # if (lastFrameProcessed%10== 0):
                        os.system('cls')
                        print("Video:", idx+1, " of " + str(len(videos)) + " --> Processing frame", lastFrameProcessed,"(" + "%.2f" % (lastFrameProcessed/totalFrames) +"%)",  " of ", str(totalFrames)
                            + "  -> "+ filex+ " "+ str(int(totalFrames/(30*60)))+ " Minutes")
                        # print("\n", int(((datetime.now().microsecond- start.microsecond)*(totalFrames-lastFrameProcessed))/ 60000000), "Minutes Reamining FPS: ",
                        #         str(int(60000000/(datetime.now().microsecond- start.microsecond))))
                        start = datetime.now()    
                
                
                p.wait()
                print(p.returncode)

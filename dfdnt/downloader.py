import urlgenerator
import dfdnt.repeatfileremover
import urllib.request
import os
from datetime import datetime
from datetime import timedelta

    
def download(configure):
    print ("downloader : start download task !")
    if not os.path.exists("./data/"):
        os.makedirs("./data/")
    now = datetime.now()
    timelable = now.strftime('_%Y-%m-%d-%H-%M')
    for target in configure.namelist:
        if configure.switch[target] == 1 :
            print ("downloader : downloading",target)
            savedir = "./data/"+target+"/"
            if not os.path.exists(savedir):
                os.makedirs(savedir)
            [mode, base_url, filenamelist, extension] = urlgenerator.geturl(configure,target)
            
            counter = 0
            for filename in filenamelist:
                ## generate filename
                if (mode == 0):
                # if (target == "JMA_Weather_Chart_1") or (target == "CWB_Skew"):
                    savepath = savedir+filename+extension
                elif (mode == 1):
                    savepath = savedir+filename+timelable+extension

                ## error checks
                # check if file is already downloaded or not
                if (os.path.exists(savepath) and configure.again[target] == 0):
                    continue
                # check if file exist on the server or not
                try:
                   response = urllib.request.urlopen(base_url+filename+extension)
                except:
                    continue
                else:
                    pass
                    
                ## download
                urllib.request.urlretrieve(base_url+filename+extension, savepath)
                counter += 1
            print ("downloader : download",counter,target,"files")
            if (configure.repeatcheck[target]):
                dfdnt.repeatfileremover.removerepeatedfiles(savedir)
        else :
            print ("downloader :",target,"is cancelled")
    return
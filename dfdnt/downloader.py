import urlgenerator
import dfdnt.repeatfileremover
import urllib.request
import os
import sys
from datetime import datetime
import threading
    
def download(configure):
    print ("start download task !")
    if not os.path.exists("./data/"):
        os.makedirs("./data/")
    now = datetime.now()
    timelable = now.strftime('_%Y-%m-%d-%H-%M')

    threads = []
    for target in configure.namelist:
        thread = downloaderThread(target, configure, target, timelable)
        threads.append(thread)
    
    for thread in threads:
        thread.start()
        
    for thread in threads:
        thread.join()

class downloaderThread(threading.Thread):
    def __init__(self, name, configure, target, timelable):
        threading.Thread.__init__(self)
        self.name = name
        self.configure = configure
        self.target = target
        self.timelable = timelable
    def run(self):
        coreByFilenamelist(self.configure, self.target, self.timelable)

def coreByFilenamelist(configure,target,timelable):
    if configure.switch[target] != 1 :
        print (target,"is cancelled")
        return
    savedir = "./data/"+target+"/"
    if not os.path.exists(savedir):
        os.makedirs(savedir)
    [mode, base_url, filenamelist, extension] = urlgenerator.geturl(configure,target)
    
    ## stateMessage
    ctTotal = len(filenamelist)
    ctProcessed = 0
    ctDownloaded = 0
    ctAgain = 0
    ctExisted = 0
    ctNotAvailable = 0
    ctRemoved = 0

    for filename in filenamelist:
        ctProcessed = ctProcessed+1
        ## generate filename
        if (mode == 0):
            savepath = savedir+filename+extension
        elif (mode == 1):
            savepath = savedir+filename+timelable+extension

        ## error checks
        # check if file is already downloaded or not
        if (os.path.exists(savepath)):
            ctExisted += 1 
            if (configure.again[target] == 0):
                continue
            else:
                ctAgain += 1
                pass
        # check if file exist on the server or not
        try:
            response = urllib.request.urlopen(base_url+filename+extension)
        except:
            ctNotAvailable += 1
            continue
        else:
            pass

        ## download
        urllib.request.urlretrieve(base_url+filename+extension, savepath)
        ctDownloaded += 1
    ## delete repeated data
    if (mode == 1):
        ctRemoved = dfdnt.repeatfileremover.removerepeatedfiles(savedir)
    print("{:<32}".format(target)+"{:0>3d}".format(ctProcessed)+"/"+"{:0>3d}".format(ctTotal)+" files "+\
                            "(D:"+"{:0>3d}".format(ctDownloaded)+"/A:"+"{:0>3d}".format(ctAgain)+\
                            "/E:"+"{:0>3d}".format(ctExisted)+"/N:"+"{:0>3d}".format(ctNotAvailable)+\
                            "/R:"+"{:0>3d}".format(ctRemoved)+") - Done")
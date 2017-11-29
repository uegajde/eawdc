import urlgenerator
import dfdnt.repeatfileremover
import urllib.request
import os
import sys
import time
from datetime import datetime
import threading
    
def download(timeConfigure):
    print ("start download tasks!")
    if not os.path.exists("./data/"):
        os.makedirs("./data/")
    now = datetime.now()
    timelable = now.strftime('_%Y-%m-%d-%H-%M')

    stateCounter(timeConfigure)

    threads = []
    for target in timeConfigure.namelist:
        if timeConfigure.switch[target] == 1 :
            thread = downloaderThread(timeConfigure, target, timelable)
            threads.append(thread)
    for thread in threads:
        thread.start()
    printState(timeConfigure.namelist)

    printSummary(timeConfigure.namelist)

class downloaderThread(threading.Thread):
    def __init__(self, timeConfigure, target, timelable):
        threading.Thread.__init__(self)
        self.timeConfigure = timeConfigure
        self.target = target
        self.timelable = timelable
    def run(self):
        coreByFilenamelist(self.timeConfigure, self.target, self.timelable)

def coreByFilenamelist(timeConfigure,target,timelable):
    global stateCounter 

    savedir = "./data/"+target+"/"
    if not os.path.exists(savedir):
        os.makedirs(savedir)
    [mode, base_url, filenamelist, extension] = urlgenerator.geturl(timeConfigure,target)

    for filename in filenamelist:
        ## generate filename
        if (mode == 0):
            savepath = savedir+filename+'.'+extension
        elif (mode == 1):
            savepath = savedir+filename+timelable+'.'+extension

        ## error checks
        # check if file is already downloaded or not
        if (os.path.exists(savepath)):
            stateCounter.existed[target] += 1
            if (timeConfigure.again[target] == 0):
                stateCounter.remaining[target] -= 1
                continue
            else:
                stateCounter.again[target] += 1
        # check if file exist on the server or not
        try:
            response = urllib.request.urlopen(base_url+filename+'.'+extension)
        except:
            stateCounter.unavailable[target] += 1
            stateCounter.remaining[target] -= 1
            continue
        else:
            pass
        if response != 200:
            stateCounter.unavailable[target] += 1
            stateCounter.remaining[target] -= 1
            continue

        ## download
        urllib.request.urlretrieve(base_url+filename+'.'+extension, savepath)
        stateCounter.downloaded[target] += 1
        stateCounter.remaining[target] -= 1

    ## delete repeated data
    if (mode == 1):
        stateCounter.removed[target] = dfdnt.repeatfileremover.removerepeatedfiles(savedir)
    stateCounter.working[target] = 0

class stateCounter:
    working = {}
    remaining = {}
    downloaded = {}
    again = {}
    existed = {}
    unavailable = {}
    removed = {}
    def __init__(self, timeConfigure):
        for target in timeConfigure.namelist:
            [mode, base_url, filenamelist, extension] = urlgenerator.geturl(timeConfigure,target)
            stateCounter.working[target] = 1
            stateCounter.remaining[target] = len(filenamelist)
            stateCounter.downloaded[target] = 0
            stateCounter.again[target] = 0
            stateCounter.existed[target] = 0
            stateCounter.unavailable[target] = 0
            stateCounter.removed[target] = 0

def printState(namelist):
    global stateCounter

    sys.stdout.write("tasks    ")
    for itarget in range(1,len(namelist)+1):
        sys.stdout.write(" "+"{: >3d}".format(itarget))
    sys.stdout.write("\n")
    
    messagelength = 9+4*len(namelist)
    while True:
        sys.stdout.write("remaining")
        for target in namelist:
            sys.stdout.write(" "+"{: >3d}".format(stateCounter.remaining[target]))
        sys.stdout.flush()
        sys.stdout.write("\b" * messagelength)
        time.sleep(0.06)
        if (sum(stateCounter.working.values()) == 0):
            break
    sys.stdout.write("remaining")
    for target in namelist:
        sys.stdout.write(" "+"{: >3d}".format(0))
    sys.stdout.flush()
    sys.stdout.write("\n")
    print ("all tasks are done")

def printSummary(namelist):
    print("SUMMARY   -   D:Download / A:Again / E:Exist / U:Unavailable / R:RemoveRepeat")
    
    for target in namelist:
        print("{:<32}".format(target)+\
            "{: >3d}".format(stateCounter.downloaded[target]-stateCounter.removed[target]-stateCounter.again[target])+" new files "+\
            "(D:"+"{: <3d}".format(stateCounter.downloaded[target])+\
            " A:"+"{: <3d}".format(stateCounter.again[target])+\
            " E:"+"{: <3d}".format(stateCounter.existed[target])+\
            " U:"+"{: <3d}".format(stateCounter.unavailable[target])+\
            " R:"+"{: <3d}".format(stateCounter.removed[target])+")")
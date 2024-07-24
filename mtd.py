import os
import sys
import urllib.request
import threading
import time
import hashlib

destinationDir = './download/'

def download(tasklist, again, removeRepeat, urls, filenamesToSaveAs):
    # initial
    print("start download tasks!")
    if not os.path.exists(destinationDir):
        os.makedirs(destinationDir)

    # initial download state
    DLState(tasklist, urls)

    # open thread for download tasks
    threads = []
    for task in tasklist:
        savedir = destinationDir +'/' + task + "/"
        if not os.path.exists(savedir):
            os.makedirs(savedir)
        thread = downloaderThread(task, again[task], removeRepeat[task], urls[task], savedir, filenamesToSaveAs[task])
        threads.append(thread)
    for thread in threads:
        thread.start()

    # print progress
    printState(tasklist)
    printSummary(tasklist)


class downloaderThread(threading.Thread):
    def __init__(self, task, again, removeRepeat, urls, savedir, filenamesToSaveAs):
        threading.Thread.__init__(self)
        self.task = task
        self.again = again
        self.removeRepeat = removeRepeat
        self.urls = urls
        self.savedir = savedir
        self.filenamesToSaveAs = filenamesToSaveAs

    def run(self):
        coreByFilenamelist(self.task, self.again, self.removeRepeat, self.urls, self.savedir, self.filenamesToSaveAs)


def coreByFilenamelist(task, again, removeRepeat, urls, savedir, filenamesToSaveAs):
    global DLState

    for iurl in range(0,len(urls)):
        # check if file is already downloaded or not
        if os.path.exists(savedir+filenamesToSaveAs[iurl]):
            DLState.existed[task] += 1
            if not again:
                DLState.remaining[task] -= 1
                DLState.new = True
                continue
            else:
                DLState.again[task] += 1
        # check if file exist on the server or not
        try:
            urllib.request.urlopen(urls[iurl])
        except:
            DLState.unavailable[task] += 1
            DLState.remaining[task] -= 1
            DLState.new = True
            continue

        # download
        try:
            urllib.request.urlretrieve(urls[iurl], savedir+filenamesToSaveAs[iurl])
            DLState.downloaded[task] += 1
            DLState.remaining[task] -= 1
            DLState.new = True
        except:
            if os.path.exists(savedir+filenamesToSaveAs[iurl]):
                os.remove(savedir+filenamesToSaveAs[iurl])
            DLState.error[task] += 1
            DLState.remaining[task] -= 1
            DLState.new = True
    # delete repeated data
    if removeRepeat:
        DLState.removed[task] = removeRepeatedfiles(savedir)
        DLState.new = True


class DLState:
    new = False
    remaining = {}
    downloaded = {}
    again = {}
    existed = {}
    unavailable = {}
    removed = {}
    error = {}

    def __init__(self, tasklist, urls):
        for task in tasklist:
            DLState.remaining[task] = len(urls[task])
            DLState.downloaded[task] = 0
            DLState.again[task] = 0
            DLState.existed[task] = 0
            DLState.unavailable[task] = 0
            DLState.removed[task] = 0
            DLState.error[task] = 0


def printState(namelist):
    global DLState

    sys.stdout.write("tasks    ")
    for itask in range(1, len(namelist) + 1):
        sys.stdout.write(" " + "{: >3d}".format(itask))
    sys.stdout.write("\n")

    messagelength = 9 + 4 * len(namelist)
    while True:
        time.sleep(0.06)
        if DLState.new:
            sys.stdout.write("remaining")
            for task in namelist:
                sys.stdout.write(" " + "{: >3d}".format(DLState.remaining[task]))
            sys.stdout.flush()
            sys.stdout.write("\b" * messagelength)
            DLState.new = False
        elif threading.active_count() == 1:
            break
    sys.stdout.write("\nall tasks are done\n")


def printSummary(namelist):
    print("SUMMARY      -      (Download / Again / Exist / Unavailable / RemoveRepeat / Error)")
    for task in namelist:
        print("{:<32}".format(task) +
              "{: >3d}".format(DLState.downloaded[task] - DLState.removed[task] - DLState.again[task]) + " new files " +
              "(D:" + "{: <3d}".format(DLState.downloaded[task]) +
              " A:" + "{: <3d}".format(DLState.again[task]) +
              " E:" + "{: <3d}".format(DLState.existed[task]) +
              " U:" + "{: <3d}".format(DLState.unavailable[task]) +
              " R:" + "{: <3d}".format(DLState.removed[task]) +
              " E:" + "{: <3d}".format(DLState.error[task]) + ")")


def removeRepeatedfiles(path):
    delfiles = 0
    hashlist = []
    for tops, _, files in os.walk(path):
        for f in files:
            filepath = os.path.join(tops, f)
            checkingfile = open(filepath, 'rb')
            buf = checkingfile.read()
            checkingfile.close()
            hasher = hashlib.md5()
            hasher.update(buf)
            newhash = hasher.hexdigest()

            vailed = True
            for vailedhash in hashlist:
                if vailedhash == newhash:
                    vailed = False
                    break
            if vailed:
                hashlist.append(newhash)
            else:
                delfiles += 1
                os.remove(filepath)
    return delfiles

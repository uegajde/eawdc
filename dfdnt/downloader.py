import os
import sys
import urllib.request
import threading
import time
from datetime import datetime
import hashlib
import urlgenerator


def download(timeConfigure):
    print("start download tasks!")
    if not os.path.exists("./data/"):
        os.makedirs("./data/")
    now = datetime.now()
    timelable = now.strftime('_%Y-%m-%d-%H-%M')

    DLState(timeConfigure)

    threads = []
    for target in timeConfigure.namelist:
        if timeConfigure.switch[target] == 1:
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


def coreByFilenamelist(timeConfigure, target, timelable):
    global DLState

    savedir = "./data/" + target + "/"
    if not os.path.exists(savedir):
        os.makedirs(savedir)
    [mode, base_url, filenamelist, extension] = urlgenerator.geturl(
        timeConfigure, target)

    for filename in filenamelist:
        # generate filename
        if mode == 0:
            savepath = savedir + filename + '.' + extension
        elif mode == 1:
            savepath = savedir + filename + timelable + '.' + extension

        # error checks
        # check if file is already downloaded or not
        if os.path.exists(savepath):
            DLState.existed[target] += 1
            if timeConfigure.again[target] == 0:
                DLState.remaining[target] -= 1
                DLState.new = True
                continue
            else:
                DLState.again[target] += 1
        # check if file exist on the server or not
        try:
            response = urllib.request.urlopen(
                base_url + filename + '.' + extension)
        except:
            DLState.unavailable[target] += 1
            DLState.remaining[target] -= 1
            DLState.new = True
            continue

        # download
        try:
            urllib.request.urlretrieve(
                base_url + filename + '.' + extension, savepath)
            DLState.downloaded[target] += 1
            DLState.remaining[target] -= 1
            DLState.new = True
        except:
            if os.path.exists(savepath):
                os.remove(savepath)
            DLState.error[target] += 1
            DLState.remaining[target] -= 1
            DLState.new = True
    # delete repeated data
    if mode == 1:
        DLState.removed[target] = removerepeatedfiles(savedir)
    DLState.working[target] = 0


class DLState:
    new = False
    working = {}
    remaining = {}
    downloaded = {}
    again = {}
    existed = {}
    unavailable = {}
    removed = {}
    error = {}

    def __init__(self, timeConfigure):
        for target in timeConfigure.namelist:
            [mode, base_url, filenamelist, extension] = urlgenerator.geturl(
                timeConfigure, target)
            DLState.working[target] = 1
            DLState.remaining[target] = len(filenamelist)
            DLState.downloaded[target] = 0
            DLState.again[target] = 0
            DLState.existed[target] = 0
            DLState.unavailable[target] = 0
            DLState.removed[target] = 0
            DLState.error[target] = 0


def printState(namelist):
    global DLState

    sys.stdout.write("tasks    ")
    for itarget in range(1, len(namelist) + 1):
        sys.stdout.write(" " + "{: >3d}".format(itarget))
    sys.stdout.write("\n")

    messagelength = 9 + 4 * len(namelist)
    while True:
        time.sleep(0.06)
        if DLState.new:
            sys.stdout.write("remaining")
            for target in namelist:
                sys.stdout.write(
                    " " + "{: >3d}".format(DLState.remaining[target]))
            sys.stdout.flush()
            sys.stdout.write("\b" * messagelength)
            DLState.new = False
        elif sum(DLState.working.values()) == 0:
            break
    sys.stdout.write("remaining")
    for target in namelist:
        sys.stdout.write(" " + "{: >3d}".format(0))
    sys.stdout.flush()
    sys.stdout.write("\nall tasks are done\n")


def printSummary(namelist):
    print("SUMMARY      -      (Download / Again / Exist / Unavailable / RemoveRepeat / Error)")

    for target in namelist:
        print("{:<32}".format(target) +
              "{: >3d}".format(DLState.downloaded[target] - DLState.removed[target] - DLState.again[target]) + " new files " +
              "(D:" + "{: <3d}".format(DLState.downloaded[target]) +
              " A:" + "{: <3d}".format(DLState.again[target]) +
              " E:" + "{: <3d}".format(DLState.existed[target]) +
              " U:" + "{: <3d}".format(DLState.unavailable[target]) +
              " R:" + "{: <3d}".format(DLState.removed[target]) +
              " E:" + "{: <3d}".format(DLState.error[target]) + ")")


def removerepeatedfiles(path):
    delfiles = 0
    hashlist = []
    for tops, dirs, files in os.walk(path):
        for f in files:
            filepath = os.path.join(tops, f)
            checkingfile = open(filepath, 'rb')
            buf = checkingfile.read()
            checkingfile.close()
            hasher = hashlib.md5()
            hasher.update(buf)
            newhash = hasher.hexdigest()

            vailed = 1
            for vailedhash in hashlist:
                if vailedhash == newhash:
                    vailed = 0
                    break
            if vailed == 1:
                hashlist.append(newhash)
            elif vailed == 0:
                delfiles += 1
                os.remove(filepath)
    return delfiles

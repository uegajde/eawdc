import urlgenerator
import dfdnt.repeatfileremover
import urllib.request
import os
import sys
from datetime import datetime

    
def download(configure):
    print ("downloader : start download task !")
    if not os.path.exists("./data/"):
        os.makedirs("./data/")
    now = datetime.now()
    timelable = now.strftime('_%Y-%m-%d-%H-%M')
    for target in configure.namelist:
        if configure.switch[target] == 1 :
            sys.stdout.write("downloader : "+"{:<32}".format(target)+" ")
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
            writeStateMessage(0,ctTotal,ctProcessed,ctDownloaded,ctAgain,ctExisted,ctNotAvailable)

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
                        writeStateMessage(1,ctTotal,ctProcessed,ctDownloaded,ctAgain,ctExisted,ctNotAvailable)
                        continue
                    else:
                        ctAgain += 1
                        pass
                # check if file exist on the server or not
                try:
                    response = urllib.request.urlopen(base_url+filename+extension)
                except:
                    ctNotAvailable += 1
                    writeStateMessage(1,ctTotal,ctProcessed,ctDownloaded,ctAgain,ctExisted,ctNotAvailable)
                    continue
                else:
                    pass

                ## download
                urllib.request.urlretrieve(base_url+filename+extension, savepath)
                ctDownloaded += 1
                writeStateMessage(1,ctTotal,ctProcessed,ctDownloaded,ctAgain,ctExisted,ctNotAvailable)
            writeStateMessage(2,ctTotal,ctProcessed,ctDownloaded,ctAgain,ctExisted,ctNotAvailable)

            ## delete repeated data
            if (mode == 1):
                dfdnt.repeatfileremover.removerepeatedfiles(savedir)
        else :
            print ("downloader :",target,"is cancelled")
    return

def writeStateMessage(mode,ctTotal,ctProcessed,ctDownloaded,ctAgain,ctExisted,ctNotAvailable):
    if (mode == 0):
        stateMessage = "000/040 files (D:000/A:000/E:000/N:000)"
        sys.stdout.write(stateMessage)
        sys.stdout.flush()
    elif (mode == 1):
        sys.stdout.write("\b" * 39)
        stateMessage = "{:0>3d}".format(ctProcessed)+"/"+"{:0>3d}".format(ctTotal)+" files "+\
                            "(D:"+"{:0>3d}".format(ctDownloaded)+\
                            "/A:"+"{:0>3d}".format(ctAgain)+\
                            '/E:'+"{:0>3d}".format(ctExisted)+\
                            "/N:"+"{:0>3d}".format(ctNotAvailable)+")"
        sys.stdout.write(stateMessage)
        sys.stdout.flush()
    elif (mode == 2):
        sys.stdout.write(' - Done')
        sys.stdout.flush()
        sys.stdout.write("\n")

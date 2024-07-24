# East Asia Weather Data Collector
import settings
import urlgenhelper
import urlgenerator
import mtd
mtd.destinationDir = settings.destinationDir

print("East Asia Weather Data Collector")

# preparing
again = {}
removeRepeat = {}
urls = {}
filenamesToSaveAs = {}
tasklist = urlgenhelper.timeConfigure.namelist
for task in tasklist:
    again[task], removeRepeat[task], urls[task], filenamesToSaveAs[task] = urlgenerator.geturl(urlgenhelper.timeConfigure, task)

if settings.show_toDownload:
    for ikey in urls.keys():
        print("------------------------------------------------")
        print(ikey)
        for url in urls[ikey]:
            print(url)

# start to download
if settings.doDownload:
    mtd.download(tasklist, again, removeRepeat, urls, filenamesToSaveAs)

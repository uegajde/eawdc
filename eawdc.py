# East Asia Weather Data Collector
import settings
import urlgenhelper
import urlgenerator
import mtd
mtd.destinationDir = settings.destinationDir

print("East Asia Weather Data Collector")

# initial tasks
again = {}
removeRepeat = {}
urls = {}
filenamesToSaveAs = {}
tasklist = urlgenhelper.timeConfigure.namelist
for task in tasklist:
    again[task], removeRepeat[task], urls[task], filenamesToSaveAs[task] = urlgenerator.geturl(urlgenhelper.timeConfigure, task)

# report tasks
print('task list:')
for itask, taskName in enumerate(tasklist):
    print('{:2d}: '.format(itask+1) + taskName)

    # print urls to request
    if settings.show_toDownload:
        for url in urls[taskName]:
            print('    '+url)

# start to download
if settings.doDownload:
    mtd.download(tasklist, again, removeRepeat, urls, filenamesToSaveAs)

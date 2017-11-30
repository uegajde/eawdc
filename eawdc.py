# East Asia Weather Data Collector
import settings
import urlgenhelper
import urlgenerator
import mtd

print("East Asia Weather Data Collector")

# preparing
again = {}
removerepeat = {}
urls = {}
savenames = {}
tasklist = urlgenhelper.timeConfigure.namelist
for task in tasklist:
    again[task], removerepeat[task], urls[task], savenames[task] = urlgenerator.geturl(urlgenhelper.timeConfigure, task)

# start to download
mtd.download(tasklist, again, removerepeat, urls, savenames)

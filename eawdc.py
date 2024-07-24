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

if settings.show_toDownload:
    for ikey in urls.keys():
        print("------------------------------------------------")
        print(ikey)
        for url in urls[ikey]:
            print(url)

# start to download
if settings.doDownload:
    mtd.download(tasklist, again, removerepeat, urls, savenames)

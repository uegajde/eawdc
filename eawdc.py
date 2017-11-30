# East Asia Weather Data Collector
import configloader
import dfdnt.downloader


version = "2.0 beta-8 (20171130)"
author = "Lin Zhe-Hui"
print("East Asia Weather Data Collector")
print("Version : ", version)
print("__________________________")


# start to download
dfdnt.downloader.download(dfdnt.defconfig.timeConfigure)

# East Asia Weather Data Collector
import configloader
import dfdnt.downloader


version = "2.0 beta-7 (20171129)"
author = "Lin Zhe-Hui"
print("East Asia Weather Data Collector")
print("Version : ", version)
print("__________________________")
# github site : https://github.com/uegajde/LZ_Downloader


# start to download
dfdnt.downloader.download(dfdnt.defconfig.timeConfigure)

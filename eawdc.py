# East Asia Weather Data Collector

# program version information

version = "2.0 beta-6 (20171129)"
author = "Lin Zhe-Hui"
print ("East Asia Weather Data Collector")
print ("Version : ",version)
print ("__________________________")
# github site : https://github.com/uegajde/LZ_Downloader

import configloader
import dfdnt.downloader

# start to download
dfdnt.downloader.download(dfdnt.defconfig.timeConfigure)
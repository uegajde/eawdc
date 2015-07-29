# LZ Weather Data Downloader

# program version information

version = "2.0 beta-1 (20150729)"
author = "Lin Zhe-Hui"
print ("LZ Weather Data Downloader")
print ("Version : ",version)
print ("__________________________")
# github site : 

import downloader
import configloader
import repeatfileremover

# read configure file
#configloader.readconfig() 

# start to download
downloader.download(configloader.configure)

# finalize
print ("all task is done")
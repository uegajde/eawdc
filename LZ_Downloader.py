# LZ Downloader

# program version information

version = "2.0 beta-2 (20150804)"
author = "Lin Zhe-Hui"
print ("LZ Downloader")
print ("Version : ",version)
print ("__________________________")
# github site : https://github.com/uegajde/LZ_Downloader

import configloader
import downloader

# start to download
downloader.download(configloader.configure)

# finalize
print ("all task is done")
# East Asia Weather Data Collector (eawdc)

    Author : Zhe-Hui Lin
    Github : https://github.com/uegajde/eawdc  

### compoents:
| script          | description | advice for normal user |
| --------------- | ----------- | ---------------------- |
| eawdc.py        | main script to do the download | use this to perform download, not recommend to modify |
| settings.py     | save settings about time-interval of data to download, and so on | modify settings here |
| urlgenerator.py | responsible for generate url for each resource | add/update resource here |
| urlgenhelper.py | a url generation helper module | not recommend to modify |
| mtd.py          | a multi-thread downloader module with simple progress showing function | not recommend to modify |

### How to use  
* prepare the env  
    1. check do you have a python 3, if not install one
    2. this package only relies on python's basic packages/modules and does not require any third-party package
* perform download
    1. python eawdc.py (for Linux/MacOS) or python.exe eawdc.py (for Windows)
    2. you can find data in the folder named 'download' (default)
* modify settings
    1. understand the basic python syntax
    2. understand what the option going to affect
    3. edit settings.py
* add/update resource
    1. get a correct url and understand what it should be for a different timing
    2. edit urlgenerator.py based on the rules you observed in step 1
    3. add corresponding timeConfigure in the settings

### settings
* destinationDir: (str) the directory/folder to save downloaded files
* doDownload: (bool) perform download or not, set to False when you just want to obtain the urls
* show_toDownload: show the url list going to request. it is useful for debug
* blankTime: blank time for the data productor preparing the latest one and avoid meaningless request trial 
* urlgenhelper.timeConfigure: register the wanted resource, setup the download behavior and configs related to timelabel generating
    * if you do not require some resource, just comment them
    * the resouce should has corresponding rules in urlgenhelper.py
    * urlgenhelper.timeConfigure intro: 

    | arg | description |
    | --- | ----------- |
    | name | name of resource |
    | unit | unit of time interval |
    | period | decide the time coverage |
    | timeInterval | time interval of data to download |
    | again | should download file again even if there already exist a file with same name |
    | timeAlignUnit | the time unit used for time-align |
    | timeAlignShift | the base time shift in time-align |
    | timeAlignMultiplier |the multiplier (i.e., interval) in time-align |

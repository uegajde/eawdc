# East Asia Weather Data Collector (eawdc)

    Author : Lin Z.H.  
    Github : https://github.com/uegajde/eawdc  
    Language : Python (v3 and later)  
    License : FREE  

# compoents:
    eawdc : main script
    settings : decide the time-density of data
    urlgenerator : generate urls
    urlgenhelper : a helper for url generation
    mtd : multi-thread downloader

# How to use  
## to download  
1. install python v3 or later  
2. python.exe eawdc.py  
3. you can find data in the folder named "download"  

## to modify the time configs
modify settings.py  

## to modify urls
modify urlgenerator.py  

## add a new target
add in both settings.py and urlgenerator.py
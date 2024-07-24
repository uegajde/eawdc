import urlgenhelper 

# destinationDir
# the directory/folder to save downloaded files
destinationDir = './download/'

# doDownload
# perform download, set to False when you just want to obtain the urls
doDownload = False

# show the url list going to request
show_toDownload = True

# blankTime:
# blank time for the data productor preparing the latest one
# timelabel within blank time will been skipped to avoid meaningless request trial 
blankTime = 30 # unit: minute

# load time configure
# name, unit, period, timeInterval, again
maxHr = 12
urlgenhelper.timeConfigure('JMA_Weather_Chart_ASAS'         , "hour"  , maxHr   ,  6, False)
urlgenhelper.timeConfigure('JMA_Weather_Chart_AUPQ78'       , "hour"  , maxHr   , 12, False)
urlgenhelper.timeConfigure('JMA_Weather_Chart_AUPQ35'       , "hour"  , maxHr   , 12, False)
urlgenhelper.timeConfigure('CWA_Surface_Analysis'           , "hour"  , maxHr   ,  6, False)
urlgenhelper.timeConfigure('CWA_Skew'                       , "hour"  , maxHr   , 12, False)
urlgenhelper.timeConfigure('CWA_Radar'                      , "minute", maxHr*60, 10, False)
urlgenhelper.timeConfigure('CWA_Satellite_Visible_EastAsia' , "minute", maxHr*60, 10, False)
urlgenhelper.timeConfigure('CWA_Satellite_Visible_TW'       , "minute", maxHr*60, 10, False)
urlgenhelper.timeConfigure('CWA_Satellite_Infrared_EastAsia', "minute", maxHr*60, 10, False)
urlgenhelper.timeConfigure('CWA_Satellite_Infrared_TW'      , "minute", maxHr*60, 10, False)
urlgenhelper.timeConfigure('CWA_Surface_Temperature'        , "hour"  , maxHr   ,  1, False)
urlgenhelper.timeConfigure('CWA_Precipitation'              , "minute", maxHr*60, 30, False)
urlgenhelper.timeConfigure('CWA_Precipitation_ex'           , "minute", maxHr*60, 30, False)
urlgenhelper.timeConfigure('CWA_WindSpeed_Observation'      , "hour"  , maxHr   ,  1, False)

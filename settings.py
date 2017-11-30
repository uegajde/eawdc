import urlgenhelper 

# load time configure
# name, unit, period, density, again
urlgenhelper.timeConfigure('JMA_Weather_Chart'              , "hour",      1,  1, False)
urlgenhelper.timeConfigure('JMA_Weather_Chart_ASAS'         , "hour",     48,  6, False)
urlgenhelper.timeConfigure('JMA_Weather_Chart_AUPQ78'       , "hour",     48, 12, False)
urlgenhelper.timeConfigure('JMA_Weather_Chart_AUPQ35'       , "hour",     48, 12, False)
urlgenhelper.timeConfigure('JMA_WaterVapor_Image'           , "minute", 1080, 10, False)
urlgenhelper.timeConfigure('CWB_Surface_Weather_Chart'      , "hour",     48,  6, False)
urlgenhelper.timeConfigure('CWB_Skew'                       , "hour",      1,  1, False)
urlgenhelper.timeConfigure('CWB_Radar'                      , "minute", 1080, 30, False)
urlgenhelper.timeConfigure('CWB_Satellite_Visible'          , "minute", 1080, 10, False)
urlgenhelper.timeConfigure('CWB_Satellite_Infrared'         , "minute", 1080, 10, False)
urlgenhelper.timeConfigure('CWB_Surface_Temperature'        , "hour",     18,  1, False)
urlgenhelper.timeConfigure('CWB_Precipitation'              , "minute", 1080, 30, False)
urlgenhelper.timeConfigure('CWB_850hpa_WindSpeed_Streamline', "hour",     48,  6, False)
urlgenhelper.timeConfigure('CWB_850hpa_RH_Streamline'       , "hour",     48,  6, False)

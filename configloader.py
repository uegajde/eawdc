import dfdnt.defconfig 

# load configure
print ("configloader : loading configure")
dfdnt.defconfig.configure('JMA_Weather_Chart_1'            , 1, "hour",      1,  1, 0)
dfdnt.defconfig.configure('JMA_Weather_Chart_2'            , 1, "hour",     48,  6, 0)
dfdnt.defconfig.configure('JMA_WaterVapor_Image'           , 1, "minute", 1080, 10, 0)
dfdnt.defconfig.configure('CWB_Surface_Weather_Chart'      , 1, "hour",     48,  1, 0)
dfdnt.defconfig.configure('CWB_Skew'                       , 1, "hour",      1,  1, 0)
dfdnt.defconfig.configure('CWB_Radar'                      , 1, "minute", 1080, 30, 0)
dfdnt.defconfig.configure('CWB_Satellite_Visible'          , 1, "minute", 1080, 10, 0)
dfdnt.defconfig.configure('CWB_Satellite_Infrared'         , 1, "minute", 1080, 10, 0)
dfdnt.defconfig.configure('CWB_Surface_Temperature'        , 1, "hour",     18,  1, 0)
dfdnt.defconfig.configure('CWB_Precipitation'              , 1, "minute", 1080, 30, 0)
dfdnt.defconfig.configure('CWB_850hpa_WindSpeed_Streamline', 1, "hour",     48,  6, 0)
dfdnt.defconfig.configure('CWB_850hpa_RH_Streamline'       , 1, "hour",     48,  6, 0)

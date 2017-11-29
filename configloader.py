import dfdnt.defconfig 

# load time configure
print ("configloader : loading time configure")
# name, switch, unit, period, density, again
dfdnt.defconfig.timeConfigure('JMA_Weather_Chart_1'            , 1, "hour",      1,  1, 0)
dfdnt.defconfig.timeConfigure('JMA_Weather_Chart_2'            , 1, "hour",     48,  6, 0)
dfdnt.defconfig.timeConfigure('JMA_WaterVapor_Image'           , 1, "minute", 1080, 10, 0)
dfdnt.defconfig.timeConfigure('CWB_Surface_Weather_Chart'      , 1, "hour",     48,  1, 0)
dfdnt.defconfig.timeConfigure('CWB_Skew'                       , 1, "hour",      1,  1, 0)
dfdnt.defconfig.timeConfigure('CWB_Radar'                      , 1, "minute", 1080, 30, 0)
dfdnt.defconfig.timeConfigure('CWB_Satellite_Visible'          , 1, "minute", 1080, 10, 0)
dfdnt.defconfig.timeConfigure('CWB_Satellite_Infrared'         , 1, "minute", 1080, 10, 0)
dfdnt.defconfig.timeConfigure('CWB_Surface_Temperature'        , 1, "hour",     18,  1, 0)
dfdnt.defconfig.timeConfigure('CWB_Precipitation'              , 1, "minute", 1080, 30, 0)
dfdnt.defconfig.timeConfigure('CWB_850hpa_WindSpeed_Streamline', 1, "hour",     48,  6, 0)
dfdnt.defconfig.timeConfigure('CWB_850hpa_RH_Streamline'       , 1, "hour",     48,  6, 0)


## prepare for future version
# load url configure
# name, mode, 
# base_url, prefix, suffix, extension, 
# timezone, timeformat, tr_unit, tr_shift, tr_multiplier

# name, mode, 
# base_url, 
# timezone, timeformat, extension, tr_unit, tr_shift, tr_multiplier
# print ("configloader : loading url configure")
# dfdnt.defconfig.urlConfigure('JMA_Weather_Chart_1', 1,\
#     "http://www.jma.go.jp/jp/metcht/pdf/kosou/",\
#     +9,{"aupq35_00","aupq35_12","aupq78_00","aupq78_12"},"pdf",0,0,0)
# dfdnt.defconfig.urlConfigure('JMA_Weather_Chart_2', 0,\
#     )
# dfdnt.defconfig.urlConfigure('JMA_WaterVapor_Image', 0,\
#     "http://www.jma.go.jp/jp/gms/imgs/0/watervapor/1/",\
#     +9,"%Y%m%d%H%M-00","png","min",0,10)
# dfdnt.defconfig.urlConfigure('CWB_Surface_Weather_Chart', 0,\
#     "http://www.cwb.gov.tw/V7/forecast/fcst/Data/",\
#     +8,"%Y-%m%d-%H00_SFCcombo","jpg","hour",0,6)
# dfdnt.defconfig.urlConfigure('CWB_Skew', 1,\
#     "http://www.cwb.gov.tw/V7/station/Data/",\
#     +8,{"SKW_46692","SKW_46699","SKW_46750"},'pdf',0,0,0)
# dfdnt.defconfig.urlConfigure('CWB_Radar', 0,\
#     "http://www.cwb.gov.tw/V7/observe/radar/Data/HD_Radar/",\
#     +8,"CV1_3600_%Y%m%d%H%M","png","min",0,10)
# dfdnt.defconfig.urlConfigure('CWB_Satellite_Visible', 0,\
#     "http://www.cwb.gov.tw/V7/observe/satellite/Data/sbo/",\
#     +8,"sbo-%Y-%m-%d-%H-%M","jpg","min",0,10)
# dfdnt.defconfig.urlConfigure('CWB_Satellite_Infrared', 0,\
#     "http://www.cwb.gov.tw/V7/observe/satellite/Data/s3q/",\
#     +8,"s3q-%Y-%m-%d-%H-%M","jpg","min",0,10)
# dfdnt.defconfig.urlConfigure('CWB_Surface_Temperature', 0,\
#     "http://www.cwb.gov.tw/V7/observe/temperature/Data/",\
#     +8,"%Y-%m-%d_%H00.GTP","jpg",0,0,0)
# dfdnt.defconfig.urlConfigure('CWB_Precipitation', 0,\
#     )
# dfdnt.defconfig.urlConfigure('CWB_850hpa_WindSpeed_Streamline', 0,\
#     "http://www.cwb.gov.tw/V7/forecast/nwp/Data/GFS/",\
#     +8,"GFS_%y%m%d%H_DS2-GE_000","gif","hour",0,6)
# dfdnt.defconfig.urlConfigure('CWB_850hpa_RH_Streamline', 0,\
#     "http://www.cwb.gov.tw/V7/forecast/nwp/Data/GFS/",\
#     +8,"GFS_%y%m%d%H_D51D2S-GE_000","gif","hour",0,6)
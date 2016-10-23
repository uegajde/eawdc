import dfdnt.defconfig 

# load configure
print ("configloader : loading configure")
JMA_Weather_Chart_1             = dfdnt.defconfig.configure('JMA_Weather_Chart_1'            ,1,"hour",     1, 1,1)
JMA_Weather_Chart_2             = dfdnt.defconfig.configure('JMA_Weather_Chart_2'            ,1,"hour",    48, 6,0)
JMA_WaterVapor_Image            = dfdnt.defconfig.configure('JMA_WaterVapor_Image'           ,1,"hour",    18, 1,1)
CWB_Surface_Weather_Chart       = dfdnt.defconfig.configure('CWB_Surface_Weather_Chart'      ,1,"hour",    48, 1,1)
CWB_Skew                        = dfdnt.defconfig.configure('CWB_Skew'                       ,1,"hour",     1, 1,1)
CWB_Radar                       = dfdnt.defconfig.configure('CWB_Radar'                      ,1,"minute",1080,30,1)
CWB_Satellite_Visible           = dfdnt.defconfig.configure('CWB_Satellite_Visible'          ,1,"minute",1080,10,1)
CWB_Satellite_Infrared          = dfdnt.defconfig.configure('CWB_Satellite_Infrared'         ,1,"minute",1080,10,1)
CWB_Surface_Temperature         = dfdnt.defconfig.configure('CWB_Surface_Temperature'        ,1,"hour",    18, 1,1)
CWB_Precipitation               = dfdnt.defconfig.configure('CWB_Precipitation'              ,1,"minute",1080,30,1)
CWB_850hpa_WindSpeed_Streamline = dfdnt.defconfig.configure('CWB_850hpa_WindSpeed_Streamline',1,"hour",    48, 6,1)
CWB_850hpa_RH_Streamline        = dfdnt.defconfig.configure('CWB_850hpa_RH_Streamline'       ,1,"hour",    48, 6,1)

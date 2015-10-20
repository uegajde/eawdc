# define class
class configure:
    number = 0
    switch = {}
    period = {}
    unit = {}
    density = {}
    repeatcheck = {}
    namelist = []
    def __init__(self, name, switch, unit, period, density, repeatcheck):
        configure.namelist.append(name)
        configure.switch[name] = switch
        configure.period[name] = period
        configure.unit[name] = unit
        configure.density[name] = density
        configure.repeatcheck[name] = repeatcheck
        self.name = name
        self.switch = switch
        self.period = period
        self.unit = unit
        self.density = density
        self.order = configure.number
        
        
# load configure
print ("configloader : loading configure")
JMA_Weather_Chart_1             = configure('JMA_Weather_Chart_1'            ,1,"hour",     1, 1,1)
JMA_Weather_Chart_2             = configure('JMA_Weather_Chart_2'            ,1,"hour",    48, 6,0)
JMA_WaterVapor_Image            = configure('JMA_WaterVapor_Image'           ,1,"hour",    18, 1,1)
CWB_Surface_Weather_Chart       = configure('CWB_Surface_Weather_Chart'      ,1,"hour",    48, 1,1)
CWB_Skew                        = configure('CWB_Skew'                       ,1,"hour",     1, 1,1)
CWB_Radar                       = configure('CWB_Radar'                      ,1,"minute",1080,30,1)
CWB_Satellite_Visible           = configure('CWB_Satellite_Visible'          ,1,"minute",1080,10,1)
CWB_Satellite_Infrared          = configure('CWB_Satellite_Infrared'         ,1,"minute",1080,10,1)
CWB_Surface_Temperature         = configure('CWB_Surface_Temperature'        ,1,"hour",    18, 1,1)
CWB_Precipitation               = configure('CWB_Precipitation'              ,1,"minute",1080,30,1)
CWB_850hpa_WindSpeed_Streamline = configure('CWB_850hpa_WindSpeed_Streamline',1,"hour",    48, 6,1)
CWB_850hpa_RH_Streamline        = configure('CWB_850hpa_RH_Streamline'       ,1,"hour",    48, 6,1)

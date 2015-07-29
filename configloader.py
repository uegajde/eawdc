# define class
class configure:
    number = 0
    switch = {}
    period = {}
    unit = {}
    density = {}
    errorlog = {}
    namelist = []
    def __init__(self, name, switch, unit, period, density, errorlog):
        configure.number += 1
        configure.namelist.append(name)
        self.name = name
        self.switch = switch
        self.period = period
        self.unit = unit
        self.density = density
        self.errorlog = errorlog
        self.order = configure.number
        configure.switch[name] = switch
        configure.period[name] = period
        configure.unit[name] = unit
        configure.density[name] = density
        configure.errorlog[name] = errorlog
    def update(self, switch, period, density, errorlog):
        self.switch = switch
        self.period = period
        self.density = density
        self.errorlog = errorlog
        configure.switch[self.name] = switch
        configure.period[self.name] = period
        configure.density[self.name] = density
        configure.errorlog[self.name] = errorlog
        
# default configure
print ("configloader : loading default configure")
JMA_Weather_Chart_1             = configure('JMA_Weather_Chart_1'            ,1,"hour",     1, 1,0)
JMA_Weather_Chart_2             = configure('JMA_Weather_Chart_2'            ,1,"hour",    48, 6,0)
JMA_WaterVapor_Image            = configure('JMA_WaterVapor_Image'           ,1,"hour",    18, 1,0)
CWB_Surface_Weather_Chart       = configure('CWB_Surface_Weather_Chart'      ,1,"hour",    48, 1,0)
CWB_Skew                        = configure('CWB_Skew'                       ,1,"hour",     1, 1,0)
CWB_Radar                       = configure('CWB_Radar'                      ,1,"minute",1080,30,0)
CWB_Satellite                   = configure('CWB_Satellite'                  ,1,"minute",1080,30,0)
CWB_Surface_Temperature         = configure('CWB_Surface_Temperature'        ,1,"hour",    18, 1,0)
CWB_Precipitation               = configure('CWB_Precipitation'              ,1,"minute",1080,30,0)
CWB_850hpa_WindSpeed_Streamline = configure('CWB_850hpa_WindSpeed_Streamline',1,"hour",    48, 6,0)
CWB_850hpa_RH_Streamline        = configure('CWB_850hpa_RH_Streamline'       ,1,"hour",    48, 6,0)

def readconfig():
    
    # read custom configure
    print ("configloader : loading custom configure")
    
    JMA_Weather_Chart_1.update(0,0,0,0)
    JMA_Weather_Chart_2.update(0,0,0,0)
    JMA_WaterVapor_Image.update(0,0,0,0)
    CWB_Surface_Weather_Chart.update(0,0,0,0)
    CWB_Skew.update(0,0,0,0)
    CWB_Radar.update(0,0,0,0)
    CWB_Satellite.update(0,0,0,0)
    CWB_Surface_Temperature.update(0,0,0,0)
    CWB_Precipitation.update(0,0,0,0)
    CWB_850hpa_WindSpeed_Streamline.update(0,0,0,0)
    CWB_850hpa_RH_Streamline.update(0,0,0,0)
    
    
    return configure
from datetime import datetime
from datetime import timedelta

now = datetime.now()


def geturl(configure,target):
    filenamelist = []
    fixtimeshift = timedelta(0)

    if   target == "JMA_Weather_Chart_1":
        # example : http://www.jma.go.jp/jp/metcht/pdf/kosou/aupq35_00.pdf (only one)
        extension = ".pdf"
        base_url = "http://www.jma.go.jp/jp/metcht/pdf/kosou/"
        filenamelist.append("aupq35_00")
        filenamelist.append("aupq35_12")
        filenamelist.append("aupq78_00")
        filenamelist.append("aupq78_12")
    elif target == "JMA_Weather_Chart_2":
        # example : http://www.hbc.co.jp/tecweather/archive/pdf/ASAS_042509.pdf   (every 6  hr)
        # example : http://www.hbc.co.jp/tecweather/archive/pdf/AUPQ78_042509.pdf (every 12 hr)
        # example : http://www.hbc.co.jp/tecweather/archive/pdf/AUPQ35_042509.pdf (every 12 hr)
        timelabelformat = "%m%d%H"
        extension = ".pdf"
        base_url = "http://www.hbc.jp/tecweather/archive/pdf/"
        fixtimeshift = getfixtimeshift(0,24,"hour",-3,6)
        timelabels = gettimelabel(configure.period[target],configure.density[target],configure.unit[target],fixtimeshift,timelabelformat)
        for timelabel in timelabels:
            filename = "ASAS_"+timelabel
            filenamelist.append(filename)
        fixtimeshift = getfixtimeshift(0,24,"hour",-9,12)
        if configure.density[target] == 6:
            density = 12
        timelabels = gettimelabel(configure.period[target],density,configure.unit[target],fixtimeshift,timelabelformat)
        for timelabel in timelabels:
            filename = "AUPQ78_"+timelabel
            filenamelist.append(filename)
            filename = "AUPQ35_"+timelabel
            filenamelist.append(filename)
    elif target == "JMA_WaterVapor_Image":
        # example : http://www.jma.go.jp/jp/gms/imgs/1/watervapor/1/201502021715-00.png (every 15 or 00 min)
        timelabelformat = "%Y%m%d%H"
        extension = ".png" 
        base_url = "http://www.jma.go.jp/jp/gms/imgs/1/watervapor/1/"
        timelabels = gettimelabel(configure.period[target],configure.density[target],configure.unit[target],fixtimeshift,timelabelformat)
        for timelabel in timelabels:
            filename = timelabel+"00-00"
            filenamelist.append(filename)
            filename = timelabel+"15-00"
            filenamelist.append(filename)
    elif target == "CWB_Surface_Weather_Chart":
        # example : http://www.cwb.gov.tw/V7/forecast/fcst/Data/2014-0508-0600_SFCcombo.jpg (every 6 hr)
        timelabelformat = "%Y-%m%d-%H00"
        extension = ".jpg" 
        base_url = "http://www.cwb.gov.tw/V7/forecast/fcst/Data/"
        fixtimeshift = getfixtimeshift(0,24,"hour",0,6)
        timelabels = gettimelabel(configure.period[target],configure.density[target],configure.unit[target],fixtimeshift,timelabelformat)
        for timelabel in timelabels:
            filename = timelabel+"_SFCcombo"
            filenamelist.append(filename)
    elif target == "CWB_Skew":
        # example : http://www.cwb.gov.tw/V7/station/Data/SKW_46692.pdf (only one)
        timelabelformat = "%Y-%m%d-%H00"
        extension = ".pdf"
        base_url = "http://www.cwb.gov.tw/V7/station/Data/"
        filenamelist.append("SKW_46692")
        filenamelist.append("SKW_46699")
        filenamelist.append("SKW_46750")
    elif target == "CWB_Radar":
        # example : http://www.cwb.gov.tw/V7/observe/radar/Data/HD_Radar/CV1_3600_201605161930.png (every 10 min)
        timelabelformat = "%Y%m%d%H%M"
        extension = ".png" 
        base_url = "http://www.cwb.gov.tw/V7/observe/radar/Data/HD_Radar/"
        if configure.density[target] != 10:
            multiplier = configure.density[target]
        else:
            multiplier = 10
        fixtimeshift = getfixtimeshift(0,60,"min",0,multiplier)
        timelabels = gettimelabel(configure.period[target],configure.density[target],configure.unit[target],fixtimeshift,timelabelformat)
        for timelabel in timelabels:
            filename = "CV1_3600_"+timelabel
            filenamelist.append(filename)
    elif target == "CWB_Satellite_Visible":
        # example : http://www.cwb.gov.tw/V7/observe/satellite/Data/sbo/sbo-2016-08-12-19-50.jpg (every 10 min)
        timelabelformat = "%Y-%m-%d-%H-%M"
        extension = ".jpg" 
        base_url = "http://www.cwb.gov.tw/V7/observe/satellite/Data/sbo/"
        fixtimeshift = getfixtimeshift(0,60,"min",0,10)
        timelabels = gettimelabel(configure.period[target],configure.density[target],configure.unit[target],fixtimeshift,timelabelformat)
        for timelabel in timelabels:
            filename = "sbo-"+timelabel
            filenamelist.append(filename)
    elif target == "CWB_Satellite_Infrared":
        # example : http://www.cwb.gov.tw/V7/observe/satellite/Data/s3q/s3q-2016-08-12-23-30.jpg (every 10 min)
        timelabelformat = "%Y-%m-%d-%H-%M"
        extension = ".jpg" 
        base_url = "http://www.cwb.gov.tw/V7/observe/satellite/Data/s3q/"
        fixtimeshift = getfixtimeshift(0,60,"min",0,10)
        timelabels = gettimelabel(configure.period[target],configure.density[target],configure.unit[target],fixtimeshift,timelabelformat)
        for timelabel in timelabels:
            filename = "s3q-"+timelabel
            filenamelist.append(filename)
    elif target == "CWB_Surface_Temperature":
        # example : http://www.cwb.gov.tw/V7/observe/temperature/Data/2014-04-20_2000.GTP.jpg (every 1 hr)
        timelabelformat = "%Y-%m-%d_%H00"
        extension = ".jpg" 
        base_url = "http://www.cwb.gov.tw/V7/observe/temperature/Data/"
        timelabels = gettimelabel(configure.period[target],configure.density[target],configure.unit[target],fixtimeshift,timelabelformat)
        for timelabel in timelabels:
            filename = timelabel+".GTP"
            filenamelist.append(filename)
    elif target == "CWB_Precipitation":
        # example : http://www.cwb.gov.tw/V7/observe/rainfall/Data/hka09100.jpg (every 30 min)
        timelabelformat = "%m%d%H%M"
        extension = ".jpg" 
        base_url = "http://www.cwb.gov.tw/V7/observe/rainfall/Data/"
        fixtimeshift = getfixtimeshift(0,60,"min",0,30)
        timelabels = gettimelabel(configure.period[target],configure.density[target],configure.unit[target],fixtimeshift,timelabelformat)
        for timelabel in timelabels:
            monlabel = int(timelabel[0:2])
            if monlabel == 10:
                monlabel = "a"
            elif monlabel == 11:   
                monlabel = "b"
            elif monlabel == 12:    
                monlabel = "c"
            monlabel = str(monlabel)
            filename = "hk"+monlabel+timelabel[2:7]
            filenamelist.append(filename)
    elif target == "CWB_850hpa_WindSpeed_Streamline":
        # example : http://www.cwb.gov.tw/V7/forecast/nwp/Data/GFS/GFS_14041918_DS2-GE_000.gif (every 6 hr)
        timelabelformat = "%y%m%d%H"
        extension = ".gif" 
        base_url = "http://www.cwb.gov.tw/V7/forecast/nwp/Data/GFS/"
        fixtimeshift = getfixtimeshift(0,24,"hour",0,6)
        timelabels = gettimelabel(configure.period[target],configure.density[target],configure.unit[target],fixtimeshift,timelabelformat)
        for timelabel in timelabels:
            filename = "GFS_"+timelabel+"_DS2-GE_000"
            filenamelist.append(filename)
    elif target == "CWB_850hpa_RH_Streamline":
        # example : http://www.cwb.gov.tw/V7/forecast/nwp/Data/GFS/GFS_15020200_D51D2S-GE_000.gif (every 6 hr)
        timelabelformat = "%y%m%d%H"
        extension = ".gif" 
        base_url = "http://www.cwb.gov.tw/V7/forecast/nwp/Data/GFS/"
        fixtimeshift = getfixtimeshift(0,24,"hour",0,6)
        timelabels = gettimelabel(configure.period[target],configure.density[target],configure.unit[target],fixtimeshift,timelabelformat)
        for timelabel in timelabels:
            filename = "GFS_"+timelabel+"_D51D2S-GE_000"
            filenamelist.append(filename)
    return [base_url, filenamelist, extension]

    
def gettimelabel(period,density,unit,fixtimeshift,format):
    timelabels = []
    before = 0
    while (before < period):
        if (unit == "minute") or (unit == "min"):
            timeshift = timedelta(0,int(-1*60*before))
        elif (unit == "hour") or (unit == "hr"):
            timeshift = timedelta(0,int(-1*3600*before))
        elif unit == "day":
            timeshift = timedelta(int(-1*before))
        targettime = now + timeshift + fixtimeshift
        timelabels.append(targettime.strftime(format))
        before += density
    return timelabels
    
def getfixtimeshift(start,end,unit,timezoneshift,multiplier):
    if (unit == "minute") or (unit == "min"):
        format = "%M"
    elif (unit == "hour") or (unit == "hr"):
        format = "%H"
    elif unit == "day":
        format = "%d"
    for before in range(start,end):
        if (unit == "minute") or (unit == "min"):
            fixtimeshift = timedelta(0,int(-1*60*before))
            format = "%M"
        elif (unit == "hour") or (unit == "hr"):
            fixtimeshift = timedelta(0,int(-1*3600*before))
            format = "%H"
        elif unit == "day":
            fixtimeshift = timedelta(int(-1*before))
            format = "%d"
        fixedtime = now + fixtimeshift
        if (int(fixedtime.strftime(format))+timezoneshift)%multiplier == 0:
            break
    return fixtimeshift
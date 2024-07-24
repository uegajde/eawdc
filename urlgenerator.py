import settings
import datetime
import urlgenhelper

now = datetime.datetime.now(datetime.UTC)-datetime.timedelta(minutes=settings.blankTime)

def getTimeDependFileNameList(cfg, task, dataTimeZone, fileNameFormat):
    filenamelist = []
    fixtimeshift = urlgenhelper.getfixtimeshift(cfg.timeAlignUnit[task], cfg.timeAlignShift[task], cfg.timeAlignMultiplier[task], now)
    timelabels = urlgenhelper.gettimelabel(cfg.period[task], cfg.timeInterval[task], cfg.unit[task], fixtimeshift, fileNameFormat, dataTimeZone, now)
    for timelabel in timelabels:
        filenamelist.append(timelabel)
    return filenamelist

def geturl(timeConfigure, task):
    addDownloadTimeLabel = False
    removeRepeat = False

    if task == "JMA_Weather_Chart_ASAS":
        # example : http://www.hbc.co.jp/tecweather/archive/pdf/ASAS_2017112715.pdf   (every 6  hr)
        datatz = +9
        fileNameFormat = "ASAS_%Y%m%d%H.pdf"
        base_url = "http://www.hbc.jp/tecweather/archive/pdf/"
        filenamelist = getTimeDependFileNameList(timeConfigure, task, datatz, fileNameFormat)
    elif task == "JMA_Weather_Chart_AUPQ78":
        # example : http://www.hbc.co.jp/tecweather/archive/pdf/AUPQ78_2017112621.pdf (every 12 hr)
        datatz = +9
        fileNameFormat = "AUPQ78_%Y%m%d%H.pdf"
        base_url = "http://www.hbc.jp/tecweather/archive/pdf/"
        filenamelist = getTimeDependFileNameList(timeConfigure, task, datatz, fileNameFormat)
    elif task == "JMA_Weather_Chart_AUPQ35":
        # example : http://www.hbc.co.jp/tecweather/archive/pdf/AUPQ35_2017042509.pdf (every 12 hr)
        datatz = +9
        fileNameFormat = "AUPQ35_%Y%m%d%H.pdf"
        base_url = "http://www.hbc.jp/tecweather/archive/pdf/"
        filenamelist = getTimeDependFileNameList(timeConfigure, task, datatz, fileNameFormat)
    elif task == "CWA_Surface_Analysis":
        #  example : https://npd.cwa.gov.tw/NPD/irisme_data/Weather/ANALYSIS/GRA___000_24072400_103.gif
        datatz = +0
        fileNameFormat = "GRA___000_%y%m%d%H_103.gif"
        base_url = "https://npd.cwa.gov.tw/NPD/irisme_data/Weather/ANALYSIS/"
        filenamelist = getTimeDependFileNameList(timeConfigure, task, datatz, fileNameFormat)
    elif task == "CWA_Skew":
        # example : https://npd.cwa.gov.tw/NPD/irisme_data/Weather/SKEWT/SKW___000_24072400_46699.gif (every 12 min)
        # 台北氣象站(46692)/東沙島氣象站(46810)/花蓮氣象站(46699)/屏東機場(46750)/馬公機場(46734)/彭佳嶼(46695)/綠島探空站(46780)
        datatz = +0
        fileNameFormat = "SKW___000_%y%m%d%H"
        base_url = "https://npd.cwa.gov.tw/NPD/irisme_data/Weather/SKEWT/"
        fixtimeshift = urlgenhelper.getfixtimeshift(timeConfigure.timeAlignUnit[task], timeConfigure.timeAlignShift[task], timeConfigure.timeAlignMultiplier[task], now)
        timelabels = urlgenhelper.gettimelabel(timeConfigure.period[task], timeConfigure.timeInterval[task], timeConfigure.unit[task], fixtimeshift, fileNameFormat, datatz, now)
        filenamelist = []
        for timelabel in timelabels:
            filenamelist.append(timelabel+"_46692.gif")
            filenamelist.append(timelabel+"_46810.gif")
            filenamelist.append(timelabel+"_46699.gif")
            filenamelist.append(timelabel+"_46750.gif")
            filenamelist.append(timelabel+"_46734.gif")
            filenamelist.append(timelabel+"_46695.gif")
            filenamelist.append(timelabel+"_46780.gif")
    elif task == "CWA_Radar":
        # example : https://www.cwa.gov.tw/Data/radar/CV1_3600_202407241300.png (every 10 min)
        datatz = +8
        fileNameFormat = "CV1_3600_%Y%m%d%H%M.png"
        base_url = "https://www.cwa.gov.tw/Data/radar/"
        filenamelist = getTimeDependFileNameList(timeConfigure, task, datatz, fileNameFormat)
    elif task == "CWA_Satellite_Visible_EastAsia":
        # example : https://www.cwa.gov.tw/Data/satellite/LCC_VIS_TRGB_2750/LCC_VIS_TRGB_2750-2024-07-24-12-50.jpg (every 10 min)
        datatz = +8
        fileNameFormat = "LCC_VIS_TRGB_2750-%Y-%m-%d-%H-%M.jpg"
        base_url = "https://www.cwa.gov.tw/Data/satellite/LCC_VIS_TRGB_2750/"
        filenamelist = getTimeDependFileNameList(timeConfigure, task, datatz, fileNameFormat)
    elif task == "CWA_Satellite_Visible_TW":
        # example : https://www.cwa.gov.tw/Data/satellite/TWI_VIS_TRGB_1375/TWI_VIS_TRGB_1375-2024-07-24-12-50.jpg (every 10 min)
        datatz = +8
        fileNameFormat = "TWI_VIS_TRGB_1375-%Y-%m-%d-%H-%M.jpg"
        base_url = "https://www.cwa.gov.tw/Data/satellite/TWI_VIS_TRGB_1375/"
        filenamelist = getTimeDependFileNameList(timeConfigure, task, datatz, fileNameFormat)
    elif task == "CWA_Satellite_Infrared_EastAsia":
        # example : https://www.cwa.gov.tw/Data/satellite/LCC_IR1_MB_2750/LCC_IR1_MB_2750-2024-07-24-13-00.jpg (every 10 min)
        datatz = +8
        fileNameFormat = "LCC_IR1_MB_2750-%Y-%m-%d-%H-%M.jpg"
        base_url = "https://www.cwa.gov.tw/Data/satellite/LCC_IR1_MB_2750/"
        filenamelist = getTimeDependFileNameList(timeConfigure, task, datatz, fileNameFormat)
    elif task == "CWA_Satellite_Infrared_TW":
        # example : https://www.cwa.gov.tw/Data/satellite/TWI_IR1_MB_800/TWI_IR1_MB_800-2024-07-24-13-00.jpg (every 10 min)
        datatz = +8
        fileNameFormat = "TWI_IR1_MB_800-%Y-%m-%d-%H-%M.jpg"
        base_url = "https://www.cwa.gov.tw/Data/satellite/TWI_IR1_MB_800/"
        filenamelist = getTimeDependFileNameList(timeConfigure, task, datatz, fileNameFormat)
    elif task == "CWA_Surface_Temperature":
        # example : https://www.cwa.gov.tw/Data/temperature/2024-07-24_1300.GTP8.jpg (every 1 hr)
        datatz = +8
        fileNameFormat = "%Y-%m-%d_%H00.GTP8.jpg"
        base_url = "https://www.cwa.gov.tw/Data/temperature/"
        filenamelist = getTimeDependFileNameList(timeConfigure, task, datatz, fileNameFormat)
    elif task == "CWA_Precipitation":
        # example : https://www.cwa.gov.tw/Data/rainfall/2024-07-24_1300.QZJ8.jpg (every 30 min)
        datatz = +8
        fileNameFormat = "%Y-%m-%d_%H%M.QZJ8.jpg"
        base_url = "https://www.cwa.gov.tw/Data/rainfall/"
        filenamelist = getTimeDependFileNameList(timeConfigure, task, datatz, fileNameFormat)
    elif task == "CWA_Precipitation_ex":
        # example : https://www.cwa.gov.tw/Data/rainfall/2024-07-24_1330.QZJ8.grd2.jpg (every 30 min)
        datatz = +8
        fileNameFormat = "%Y-%m-%d_%H%M.QZJ8.grd2.jpg"
        base_url = "https://www.cwa.gov.tw/Data/rainfall/"
        filenamelist = getTimeDependFileNameList(timeConfigure, task, datatz, fileNameFormat)
    elif task == "CWA_WindSpeed_Observation":
        # example : https://www.cwa.gov.tw/Data/windspeed/2024-07-24_1000.GWD.png (every 1 hour)
        datatz = +8
        fileNameFormat = "%Y-%m-%d_%H00.GWD.png"
        base_url = "https://www.cwa.gov.tw/Data/windspeed/"
        filenamelist = getTimeDependFileNameList(timeConfigure, task, datatz, fileNameFormat)

    again = timeConfigure.again[task]
    removeRepeat = addDownloadTimeLabel

    urls, filenamesToSaveAs = urlgenhelper.urlcomposer(base_url, filenamelist, addDownloadTimeLabel)

    return again, removeRepeat, urls, filenamesToSaveAs 

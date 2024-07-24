import datetime
from datetime import timedelta
import urlgenhelper

now = datetime.datetime.now(datetime.UTC)


def geturl(timeConfigure, task):
    filenamelist = []
    fixtimeshift = timedelta(0)

    if task == "JMA_Weather_Chart_ASAS":
        # example : http://www.hbc.co.jp/tecweather/archive/pdf/ASAS_2017112715.pdf   (every 6  hr)
        # example : http://www.hbc.co.jp/tecweather/archive/pdf/AUPQ78_2017112621.pdf (every 12 hr)
        # example : http://www.hbc.co.jp/tecweather/archive/pdf/AUPQ35_2017042509.pdf (every 12 hr)
        mode = 0
        datatz = +9
        timelabelformat = "ASAS_%Y%m%d%H"
        extension = "pdf"
        base_url = "http://www.hbc.jp/tecweather/archive/pdf/"
        fixtimeshift = urlgenhelper.getfixtimeshift("hour", 0, 6, now)
        timelabels = urlgenhelper.gettimelabel(
            timeConfigure.period[task], timeConfigure.density[task], timeConfigure.unit[task], fixtimeshift, timelabelformat, datatz, now)
        for timelabel in timelabels:
            filenamelist.append(timelabel)
    elif task == "JMA_Weather_Chart_AUPQ78":
        # example : http://www.hbc.co.jp/tecweather/archive/pdf/ASAS_2017112715.pdf   (every 6  hr)
        # example : http://www.hbc.co.jp/tecweather/archive/pdf/AUPQ78_2017112621.pdf (every 12 hr)
        # example : http://www.hbc.co.jp/tecweather/archive/pdf/AUPQ35_2017042509.pdf (every 12 hr)
        mode = 0
        datatz = +9
        timelabelformat = "AUPQ78_%Y%m%d%H"
        extension = "pdf"
        base_url = "http://www.hbc.jp/tecweather/archive/pdf/"
        fixtimeshift = urlgenhelper.getfixtimeshift("hour", 0, 12, now)
        timelabels = urlgenhelper.gettimelabel(
            timeConfigure.period[task], timeConfigure.density[task], timeConfigure.unit[task], fixtimeshift, timelabelformat, datatz, now)
        for timelabel in timelabels:
            filenamelist.append(timelabel)
    elif task == "JMA_Weather_Chart_AUPQ35":
        # example : http://www.hbc.co.jp/tecweather/archive/pdf/ASAS_2017112715.pdf   (every 6  hr)
        # example : http://www.hbc.co.jp/tecweather/archive/pdf/AUPQ78_2017112621.pdf (every 12 hr)
        # example : http://www.hbc.co.jp/tecweather/archive/pdf/AUPQ35_2017042509.pdf (every 12 hr)
        mode = 0
        datatz = +9
        timelabelformat = "AUPQ35_%Y%m%d%H"
        extension = "pdf"
        base_url = "http://www.hbc.jp/tecweather/archive/pdf/"
        fixtimeshift = urlgenhelper.getfixtimeshift("hour", 0, 12, now)
        timelabels = urlgenhelper.gettimelabel(
            timeConfigure.period[task], timeConfigure.density[task], timeConfigure.unit[task], fixtimeshift, timelabelformat, datatz, now)
        for timelabel in timelabels:
            filenamelist.append(timelabel)
    elif task == "CWA_Surface_Analysis":
        #  example : https://npd.cwa.gov.tw/NPD/irisme_data/Weather/ANALYSIS/GRA___000_24072400_103.gif
        mode = 0
        datatz = +0
        timelabelformat = "GRA___000_%y%m%d%H_103"
        extension = "gif"
        base_url = "https://npd.cwa.gov.tw/NPD/irisme_data/Weather/ANALYSIS/"
        fixtimeshift = urlgenhelper.getfixtimeshift("hour", 0, 6, now)
        timelabels = urlgenhelper.gettimelabel(
            timeConfigure.period[task], timeConfigure.density[task], timeConfigure.unit[task], fixtimeshift, timelabelformat, datatz, now)
        for timelabel in timelabels:
            filenamelist.append(timelabel)
    elif task == "CWA_Skew":
        # example : https://npd.cwa.gov.tw/NPD/irisme_data/Weather/SKEWT/SKW___000_24072400_46699.gif (every 12 min)
        # 台北氣象站(46692)/東沙島氣象站(46810)/花蓮氣象站(46699)/屏東機場(46750)/馬公機場(46734)/彭佳嶼(46695)/綠島探空站(46780)
        mode = 0
        datatz = +0
        timelabelformat = "SKW___000_%y%m%d%H"
        extension = "gif"
        base_url = "https://npd.cwa.gov.tw/NPD/irisme_data/Weather/SKEWT/"
        fixtimeshift = urlgenhelper.getfixtimeshift("hour", 0, 12, now)
        timelabels = urlgenhelper.gettimelabel(
            timeConfigure.period[task], timeConfigure.density[task], timeConfigure.unit[task], fixtimeshift, timelabelformat, datatz, now)
        for timelabel in timelabels:
            filenamelist.append(timelabel+"_46692")
            filenamelist.append(timelabel+"_46810")
            filenamelist.append(timelabel+"_46699")
            filenamelist.append(timelabel+"_46750")
            filenamelist.append(timelabel+"_46734")
            filenamelist.append(timelabel+"_46695")
            filenamelist.append(timelabel+"_46780")
    elif task == "CWA_Radar":
        # example : https://www.cwa.gov.tw/Data/radar/CV1_3600_202407241300.png (every 10 min)
        mode = 0
        datatz = +8
        timelabelformat = "CV1_3600_%Y%m%d%H%M"
        extension = "png"
        base_url = "https://www.cwa.gov.tw/Data/radar/"
        fixtimeshift = urlgenhelper.getfixtimeshift("min", 0, 10, now)
        timelabels = urlgenhelper.gettimelabel(
            timeConfigure.period[task], timeConfigure.density[task], timeConfigure.unit[task], fixtimeshift, timelabelformat, datatz, now)
        for timelabel in timelabels:
            filenamelist.append(timelabel)
    elif task == "CWA_Satellite_Visible_EastAsia":
        # example : https://www.cwa.gov.tw/Data/satellite/LCC_VIS_TRGB_2750/LCC_VIS_TRGB_2750-2024-07-24-12-50.jpg (every 10 min)
        mode = 0
        datatz = +8
        timelabelformat = "LCC_VIS_TRGB_2750-%Y-%m-%d-%H-%M"
        extension = "jpg"
        base_url = "https://www.cwa.gov.tw/Data/satellite/LCC_VIS_TRGB_2750/"
        fixtimeshift = urlgenhelper.getfixtimeshift("min", 0, 10, now)
        timelabels = urlgenhelper.gettimelabel(
            timeConfigure.period[task], timeConfigure.density[task], timeConfigure.unit[task], fixtimeshift, timelabelformat, datatz, now)
        for timelabel in timelabels:
            filenamelist.append(timelabel)
    elif task == "CWA_Satellite_Visible_TW":
        # example : https://www.cwa.gov.tw/Data/satellite/TWI_VIS_TRGB_1375/TWI_VIS_TRGB_1375-2024-07-24-12-50.jpg (every 10 min)
        mode = 0
        datatz = +8
        timelabelformat = "TWI_VIS_TRGB_1375-%Y-%m-%d-%H-%M"
        extension = "jpg"
        base_url = "https://www.cwa.gov.tw/Data/satellite/TWI_VIS_TRGB_1375/"
        fixtimeshift = urlgenhelper.getfixtimeshift("min", 0, 10, now)
        timelabels = urlgenhelper.gettimelabel(
            timeConfigure.period[task], timeConfigure.density[task], timeConfigure.unit[task], fixtimeshift, timelabelformat, datatz, now)
        for timelabel in timelabels:
            filenamelist.append(timelabel)
    elif task == "CWA_Satellite_Infrared_EastAsia":
        # example : https://www.cwa.gov.tw/Data/satellite/LCC_IR1_MB_2750/LCC_IR1_MB_2750-2024-07-24-13-00.jpg (every 10 min)
        mode = 0
        datatz = +8
        timelabelformat = "LCC_IR1_MB_2750-%Y-%m-%d-%H-%M"
        extension = "jpg"
        base_url = "https://www.cwa.gov.tw/Data/satellite/LCC_IR1_MB_2750/"
        fixtimeshift = urlgenhelper.getfixtimeshift("min", 0, 10, now)
        timelabels = urlgenhelper.gettimelabel(
            timeConfigure.period[task], timeConfigure.density[task], timeConfigure.unit[task], fixtimeshift, timelabelformat, datatz, now)
        for timelabel in timelabels:
            filenamelist.append(timelabel)
    elif task == "CWA_Satellite_Infrared_TW":
        # example : https://www.cwa.gov.tw/Data/satellite/TWI_IR1_MB_800/TWI_IR1_MB_800-2024-07-24-13-00.jpg (every 10 min)
        mode = 0
        datatz = +8
        timelabelformat = "TWI_IR1_MB_800-%Y-%m-%d-%H-%M"
        extension = "jpg"
        base_url = "https://www.cwa.gov.tw/Data/satellite/TWI_IR1_MB_800/"
        fixtimeshift = urlgenhelper.getfixtimeshift("min", 0, 10, now)
        timelabels = urlgenhelper.gettimelabel(
            timeConfigure.period[task], timeConfigure.density[task], timeConfigure.unit[task], fixtimeshift, timelabelformat, datatz, now)
        for timelabel in timelabels:
            filenamelist.append(timelabel)
    elif task == "CWA_Surface_Temperature":
        # example : https://www.cwa.gov.tw/Data/temperature/2024-07-24_1300.GTP8.jpg (every 1 hr)
        mode = 0
        datatz = +8
        timelabelformat = "%Y-%m-%d_%H00.GTP8"
        extension = "jpg"
        base_url = "https://www.cwa.gov.tw/Data/temperature/"
        fixtimeshift = urlgenhelper.getfixtimeshift("hr", 0, 1, now)
        timelabels = urlgenhelper.gettimelabel(
            timeConfigure.period[task], timeConfigure.density[task], timeConfigure.unit[task], fixtimeshift, timelabelformat, datatz, now)
        for timelabel in timelabels:
            filenamelist.append(timelabel)
    elif task == "CWA_Precipitation":
        # example : https://www.cwa.gov.tw/Data/rainfall/2024-07-24_1300.QZJ8.jpg (every 30 min)
        mode = 0
        datatz = +8
        timelabelformat = "%Y-%m-%d_%H%M.QZJ8"
        extension = "jpg"
        base_url = "https://www.cwa.gov.tw/Data/rainfall/"
        fixtimeshift = urlgenhelper.getfixtimeshift("min", 0, 30, now)
        timelabels = urlgenhelper.gettimelabel(
            timeConfigure.period[task], timeConfigure.density[task], timeConfigure.unit[task], fixtimeshift, timelabelformat, datatz, now)
        for timelabel in timelabels:
            filenamelist.append(timelabel)
    elif task == "CWA_Precipitation_ex":
        # example : https://www.cwa.gov.tw/Data/rainfall/2024-07-24_1330.QZJ8.grd2.jpg (every 30 min)
        mode = 0
        datatz = +8
        timelabelformat = "%Y-%m-%d_%H%M.QZJ8.grd2"
        extension = "jpg"
        base_url = "https://www.cwa.gov.tw/Data/rainfall/"
        fixtimeshift = urlgenhelper.getfixtimeshift("min", 0, 30, now)
        timelabels = urlgenhelper.gettimelabel(
            timeConfigure.period[task], timeConfigure.density[task], timeConfigure.unit[task], fixtimeshift, timelabelformat, datatz, now)
        for timelabel in timelabels:
            filenamelist.append(timelabel)
    elif task == "CWA_WindSpeed_Observation":
        # example : https://www.cwa.gov.tw/Data/windspeed/2024-07-24_1000.GWD.png (every 1 hour)
        mode = 0
        datatz = +8
        timelabelformat = "%Y-%m-%d_%H00.GWD"
        extension = "png"
        base_url = "https://www.cwa.gov.tw/Data/windspeed/"
        fixtimeshift = urlgenhelper.getfixtimeshift("hour", 0, 1, now)
        timelabels = urlgenhelper.gettimelabel(
            timeConfigure.period[task], timeConfigure.density[task], timeConfigure.unit[task], fixtimeshift, timelabelformat, datatz, now)
        for timelabel in timelabels:
            filenamelist.append(timelabel)

    again = timeConfigure.again[task]
    if mode == 0:
        removerepeat = False
    elif mode == 1:
        removerepeat = True
    urls, savenames =  urlgenhelper.urlcomposer(mode, base_url, filenamelist, extension)

    return again, removerepeat, urls, savenames

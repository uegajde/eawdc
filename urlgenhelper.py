from datetime import datetime
from datetime import timedelta


class timeConfigure:
    period = {}
    unit = {}
    timeInterval = {}
    again = {}
    namelist = []

    timeAlignUnit = {}
    timeAlignShift = {}
    timeAlignMultiplier = {}

    def __init__(self, name, unit, period, timeInterval, again, timeAlignUnit, timeAlignShift, timeAlignMultiplier):
       timeConfigure.namelist.append(name)
       timeConfigure.period[name] = period
       timeConfigure.unit[name] = unit
       timeConfigure.timeInterval[name] = timeInterval
       timeConfigure.again[name] = again
       timeConfigure.timeAlignUnit[name] = timeAlignUnit
       timeConfigure.timeAlignShift[name] = timeAlignShift
       timeConfigure.timeAlignMultiplier[name] = timeAlignMultiplier


def gettimelabel(period, timeInterval, unit, fixtimeshift, tformat, datatimezone, now):
    timelabels = []
    before = 0
    while before < period:
        if unit in ['minutes', 'minute', 'min', 'm']:
            timeshift = timedelta(0, int(-1 * 60 * before))
        elif unit in ['hours', 'hour', 'hr', 'h']:
            timeshift = timedelta(0, int(-1 * 3600 * before))
        elif unit in ['days', 'day', 'd']:
            timeshift = timedelta(int(-1 * before))
        targettime = now + timeshift + fixtimeshift + timedelta(0, int(3600 * datatimezone))
        timelabels.append(targettime.strftime(tformat))
        before += timeInterval
    return timelabels


def getfixtimeshift(unit, shift, multiplier, now):
    start = 0
    if unit in ['minutes', 'minute', 'min', 'm']:
        end = 60
        tformat = "%M"
    elif unit in ['hours', 'hour', 'hr', 'h']:
        end = 24
        tformat = "%H"

    for before in range(start, end):
        if unit in ['minutes', 'minute', 'min', 'm']:
            fixtimeshift = timedelta(0, int(-1 * 60 * before))
            tformat = "%M"
        elif unit in ['hours', 'hour', 'hr', 'h']:
            fixtimeshift = timedelta(0, int(-1 * 3600 * before))
            tformat = "%H"
        elif unit in ['days', 'day', 'd']:
            fixtimeshift = timedelta(int(-1 * before))
            tformat = "%d"
        fixedtime = now + fixtimeshift
        if (int(fixedtime.strftime(tformat)) + shift) % multiplier == 0:
            break
    return fixtimeshift


def urlcomposer(base_url, filenamelist, addDownloadTimeLabel):
    # url info
    urls = []
    filenamesToSaveAs = []
    localnow = datetime.now()
    timelable = localnow.strftime('_%Y-%m-%d-%H-%M')

    if addDownloadTimeLabel is False:
        for filename in filenamelist:
            urls.append(base_url + filename)
            filenamesToSaveAs.append(filename)
    elif addDownloadTimeLabel is True:
        for filename in filenamelist:
            urls.append(base_url + filename)
            filenamesToSaveAs.append(filename + timelable)
    return urls, filenamesToSaveAs

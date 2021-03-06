from datetime import datetime
from datetime import timedelta


class timeConfigure:
    period = {}
    unit = {}
    density = {}
    again = {}
    namelist = []

    def __init__(self, name, unit, period, density, again):
       timeConfigure.namelist.append(name)
       timeConfigure.period[name] = period
       timeConfigure.unit[name] = unit
       timeConfigure.density[name] = density
       timeConfigure.again[name] = again


def gettimelabel(period, density, unit, fixtimeshift, tformat, datatimezone, now):
    timelabels = []
    before = 0
    while before < period:
        if (unit == "minute") or (unit == "min"):
            timeshift = timedelta(0, int(-1 * 60 * before))
        elif (unit == "hour") or (unit == "hr"):
            timeshift = timedelta(0, int(-1 * 3600 * before))
        elif unit == "day":
            timeshift = timedelta(int(-1 * before))
        targettime = now + timeshift + fixtimeshift + timedelta(0, int(3600 * datatimezone))
        timelabels.append(targettime.strftime(tformat))
        before += density
    return timelabels


def getfixtimeshift(unit, shift, multiplier, now):
    start = 0
    if (unit == "minute") or (unit == "min"):
        end = 60
        tformat = "%M"
    elif (unit == "hour") or (unit == "hr"):
        end = 24
        tformat = "%H"

    for before in range(start, end):
        if (unit == "minute") or (unit == "min"):
            fixtimeshift = timedelta(0, int(-1 * 60 * before))
            tformat = "%M"
        elif (unit == "hour") or (unit == "hr"):
            fixtimeshift = timedelta(0, int(-1 * 3600 * before))
            tformat = "%H"
        elif unit == "day":
            fixtimeshift = timedelta(int(-1 * before))
            tformat = "%d"
        fixedtime = now + fixtimeshift
        if (int(fixedtime.strftime(tformat)) + shift) % multiplier == 0:
            break
    return fixtimeshift


def urlcomposer(mode, base_url, filenamelist, extension):
    # url info
    urls = []
    savenames = []
    localnow = datetime.now()
    timelable = localnow.strftime('_%Y-%m-%d-%H-%M')

    if mode == 0:
        for filename in filenamelist:
            urls.append(base_url + filename + '.' + extension)
            savenames.append(filename + '.' + extension)
    elif mode == 1:
        for filename in filenamelist:
            urls.append(base_url + filename + '.' + extension)
            savenames.append(filename + timelable + '.' + extension)
    return urls, savenames

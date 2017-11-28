from datetime import timedelta

def gettimelabel(period,density,unit,fixtimeshift,format,now):
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
    
def getfixtimeshift(start,end,unit,timezoneshift,multiplier,now):
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
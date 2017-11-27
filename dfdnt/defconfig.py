# define class
class configure:
    number = 0
    switch = {}
    period = {}
    unit = {}
    density = {}
    again = {}
    repeatcheck = {}
    namelist = []
    mode = {}
    def __init__(self, name, switch, unit, period, density, again, repeatcheck, mode):
        configure.namelist.append(name)
        configure.switch[name] = switch
        configure.period[name] = period
        configure.unit[name] = unit
        configure.density[name] = density
        configure.again[name] = again
        configure.repeatcheck[name] = repeatcheck
        configure.mode[name] = mode

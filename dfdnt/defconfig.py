# define class
class configure:
    number = 0
    switch = {}
    period = {}
    unit = {}
    density = {}
    again = {}
    namelist = []
    def __init__(self, name, switch, unit, period, density, again):
        configure.namelist.append(name)
        configure.switch[name] = switch
        configure.period[name] = period
        configure.unit[name] = unit
        configure.density[name] = density
        configure.again[name] = again

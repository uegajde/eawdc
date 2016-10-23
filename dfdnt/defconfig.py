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

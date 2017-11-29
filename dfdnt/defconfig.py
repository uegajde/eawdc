# define class
class timeConfigure:
    switch = {}
    period = {}
    unit = {}
    density = {}
    again = {}
    namelist = []

    def __init__(self, name, switch, unit, period, density, again):
        timeConfigure.namelist.append(name)
        timeConfigure.switch[name] = switch
        timeConfigure.period[name] = period
        timeConfigure.unit[name] = unit
        timeConfigure.density[name] = density
        timeConfigure.again[name] = again

# prepare for future version
# class urlConfigure:
#     namelist = []
#     mode = {}
#     base_url = {}
#     datatz = {}
#     timeformat = {}
#     extension = {}
#     tr_unit = {}
#     tr_shift = {}
#     tr_multiplier = {}
#     def __init__(self, name, mode, base_url, datatz, timeformat, extension, tr_unit, tr_shift, tr_multiplier):
#         urlConfigure.namelist.append(name)
#         urlConfigure.mode[name] = mode
#         urlConfigure.base_url[name] = base_url
#         urlConfigure.datatz[name] = datatz
#         urlConfigure.timeformat[name] = timeformat
#         urlConfigure.extension[name] = extension
#         urlConfigure.suffix[name] = suffix
#         urlConfigure.tr_shift[name] = tr_shift
#         urlConfigure.tr_multiplier[name] = tr_multiplier

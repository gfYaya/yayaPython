# coding=utf-8

def timevalueAdd(timevalue, diff=15):
    # print "timevalueAdd",timevalue
    if diff > 60:
        diff = diff % 60
    timeValueDay = int(timevalue[0:6])
    timeValueHour = int(timevalue[-6:-4])
    timeValueMinu = int(timevalue[-4:-2])
    timeValueSecond = int(timevalue[-2:])
    timeValueSecond = timeValueSecond + diff

    if timeValueSecond >= 60:
        timeValueSecond, timeValueMinu = timeValueSecond - 60, timeValueMinu + 1
    if timeValueMinu >= 60:
        timeValueMinu, timeValueHour = timeValueMinu - 60, timeValueHour + 1
    if timeValueHour >= 24:
        timeValueHour, timeValueDay = timeValueHour - 24, timeValueDay + 1

    if len('%d' % timeValueSecond) == 1:
        timeValueSecond = '0' + '%d' % timeValueSecond
    if len('%d' % timeValueMinu) == 1:
        timeValueMinu = '0' + '%d' % timeValueMinu
    if len('%d' % timeValueHour) == 1:
        timeValueHour = '0' + '%d' % timeValueHour

    return ('%d' + '%s' * 3) % (timeValueDay, timeValueHour, timeValueMinu, timeValueSecond)


# 增加 时间值区间下限
def timevalueMin(timevalue, diff=15):
    # print "timevalueMin", timevalue
    if diff > 60:
        diff = diff % 60
    timeValueDay = int(timevalue[0:6])
    timeValueHour = int(timevalue[-6:-4])
    timeValueMinu = int(timevalue[-4:-2])
    timeValueSecond = int(timevalue[-2:])
    timeValueSecond = timeValueSecond - diff

    if timeValueSecond < 0:
        timeValueSecond, timeValueMinu = timeValueSecond + 60, timeValueMinu - 1
    if timeValueMinu < 0:
        timeValueMinu, timeValueHour = timeValueMinu + 60, timeValueHour - 1
    if timeValueHour > 24:
        timeValueHour, timeValueDay = timeValueHour + 24, timeValueDay - 1

    if len('%d' % timeValueSecond) == 1:
        timeValueSecond = '0' + '%d' % timeValueSecond
    if len('%d' % timeValueMinu) == 1:
        timeValueMinu = '0' + '%d' % timeValueMinu
    if len('%d' % timeValueHour) == 1:
        timeValueHour = '0' + '%d' % timeValueHour

    return ('%d' + '%s' * 3) % (timeValueDay, timeValueHour, timeValueMinu, timeValueSecond)


print(timevalueMin("170307005955"))
print(timevalueAdd("170307010955"))

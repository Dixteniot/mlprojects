# expectation.py


def divisionByX(dividend, divisor=2):
    if(divisor == 0):
        raise(ZeroDivisionError)
    return dividend // divisor

def remainderOfX(dividend, divisor=2):
    if(divisor == 0):
        raise(ZeroDivisionError)
    return dividend % divisor

def decimalToBinary(decimal):
    binary = 2
    quotient = divisionByX(decimal, binary)
    remainder = remainderOfX(decimal, binary)
    if(quotient > 0):
        remainder = '%s%s'%(remainderOfX(quotient, binary), remainder)
    while(quotient > 0):
        quotient = divisionByX(quotient, binary)
        remainder = '%s%s'%(remainderOfX(quotient, binary), remainder)
    return remainder

def validExpectation(expectations, events):
    expected = False
    event = False
    valid = False
    for x in expectations:
        if(int(x) == 1):
            expected = True
            break
    for y in events:
        if(int(y) == 1):
           event = True
           break
    if(event == expected):
        valid = True
    return valid

def probability(events):
    totalEvents = len(events)
    sumEvents = 0
    for x in events:
        sumEvents += int(x)
    return (sumEvents / totalEvents) * 100

def truthTable(lines=128):
    head = ['time', '#', 'user1', 'user2', 'user3', 'decade1', 'decade2', 'decade3', 'decade4', 'valid', 'probability']
    data = [1, 0,0,0,0,0,0,0,0, True, 0]
    probabilityX = len(data) - 1
    validX = probabilityX - 1
    timeX = 0
    dataTable = []
    dataTable.append('%s'%(head))
    max = 128
    if(lines > max):
        lines = max
    firstTime = True
    for x in range(lines):
        data[timeX] = x + 1
        binary = '%s'%(decimalToBinary(x))
        i = len(data) - 1 - 2
        b = len(binary) - 1
        for y in binary:
            data[i] = binary[b]
            i -= 1
            b -= 1
        users = data[2:5]
        events = data[5:9]
        data[probabilityX] = probability(events)
        data[validX] = validExpectation(users, events)
        dataTable.append('%s'%(data))
        firstTime = False
    return dataTable

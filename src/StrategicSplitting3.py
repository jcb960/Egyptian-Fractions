"""
Copyright (c) 2025, [Patrick (my teamate)].
All rights reserved.

This source code is licensed under the Apache License, Version 2.0 license found in the
LICENSE file in the root directory of this source tree. 
"""

import ast

case = ast.literal_eval(open("o3.txt", "r").read())
# inList2 = ast.literal_eval(open("JCB2000908.txt","r").read())
# inList2 = ast.literal_eval(open("JCB2000907.txt","r").read())
inList = eval(open("JCB2000906.txt", "r").read())


def listSum(listToSum):
    total = 0
    for x in listToSum:
        total += 1 / x
    return (total)


def reciprical(x):
    return (1 / x)


def generalFormula3(x, splitTwoL):
    gF3M = []

    if x <= 674:
        lim = int(x * 3) + 2
        if lim > 2023:
            lim = 2024

        for n in range(int(x) + 1, lim):
            if 1 / x == 1 / n:
                continue
            b = (1 / x) - (1 / n)
            rB = round(1 / b, 9)

            if 1 / b > 1012:
                r = []
            elif rB.is_integer():
                r = splitTwoL[int(rB) - 2]
            else:
                r = generalFormulaFrac2(1 / b)

            for t in r:
                if n not in t:
                    i = sorted([n, t[0], t[1]])

                    if i not in gF3M:
                        gF3M.append(i)

    return gF3M


def generalFormula2(x):
    gF2M = []

    if x <= 1012:
        lim = int(x * 2) + 2
        if lim > 2023:
            lim = 2024

        for n in range(1, lim):
            sFD = round((x * x + x * n) / n, 9)

            if sFD.is_integer():
                fFD = x + n

                if fFD != sFD and 2 <= fFD <= 2023 and 2 <= sFD <= 2023:
                    i = sorted([int(fFD), int(sFD)])

                    if i not in gF2M:
                        gF2M.append(i)

    return gF2M


def generalFormulaFrac2(x):
    gFF2M = []

    if x <= 1012:
        lim = int(x * 2) + 2
        if lim > 2023:
            lim = 2024

        for y in range(int(x) + 1, lim):
            n = y - x
            sFD = round((x * x + x * n) / n, 9)

            if sFD.is_integer():
                fFD = round(x + n, 9)

                if fFD != sFD and 2 <= fFD <= 2023 and 2 <= sFD <= 2023:
                    i = sorted([int(fFD), int(sFD)])

                    if i not in gFF2M:
                        gFF2M.append(i)

    return gFF2M


def recSubDiv(passUp, localDepth, v):
    global case
    newCase = case[:]
    newCase.remove(v[0])
    newCase.remove(v[1])
    if localDepth == 1:
        for x in passUp:
            if newCase.__contains__(x) or passUp.count(x) > 1:
                return None
        return passUp

    global inList

    # if dicti.__contains__(passUp[0]):
    valueList = []
    inValue = 1 / (1 / v[0] + 1 / v[1])
    dicti = generalFormula3(inValue, inList)
    # print (dicti)

    for x in dicti:
        valueList.append(sum(x) * max(x))

    valueListHold = valueList[:]

    for y in valueList:
        value = dicti[valueList.index(max(valueListHold))]

        output = recSubDiv(value, localDepth + 1, v)
        if output != None:
            return (output)

        valueListHold.remove(max(valueListHold))

    return (None)


def recSubDivbasic(passUp, localDepth):
    global case
    if localDepth == 1:
        for x in passUp:
            if case.__contains__(x) or passUp.count(x) > 1:
                return None
        return passUp

    global inList2
    dicti = inList2

    valueList = []

    for x in dicti[passUp]:
        valueList.append(sum(x) * max(x))

    valueListHold = valueList[:]

    for y in valueList:
        value = dicti[passUp][valueList.index(max(valueListHold))]

        output = recSubDivbasic(value, localDepth + 1)
        if output != None:
            return (output)

        valueListHold.remove(max(valueListHold))

    return (None)


def recSubDiv2(v, target, depth, targetDepth):
    global case

    if depth == targetDepth:
        remainder = 1 / sum(list(map(reciprical, v))) - sum(list(map(reciprical, target)))
        if remainder.is_integer() and not (case.__contains__(remainder)):
            v.append(remainder)
            return (v)
        else:
            return (None)

    if len(v) > 0:
        minimum = v[-1]
    else:
        minimum = 2

    for x in reversed(range(minimum, 2024)):
        if case.__contains__(x):
            continue
        vHold = v[:]
        vHold.append(x)
        if (1 / (sum(list(map(reciprical, target))) - sum(list(map(reciprical, vHold)))) < 0):
            break

        output = recSubDiv2(vHold, target, depth + 1, targetDepth)

        if output != None:
            return (output)
    return (None)


def recDiv(l, depth, maxDepth):
    global case

    if depth == maxDepth:
        for x in l:
            if l.count(x) > 1 or case.__contains__(x) or not (int(x) == x):
                return (None)
        return (l)

    for x in l:
        lim = int(x * 2) + 2
        if lim > 2023 - int(x):
            lim = 2024 - int(x)

        for n in range(int(x) + 1, lim):
            major = x * ((x / n) + 1)

            if not (int(major) == major):
                continue

            lHold = l[:]
            lHold.remove(x)
            lHold.append(x + n)
            lHold.append(major)
            output = recDiv(lHold, depth + 1, maxDepth)

            if output != None:
                return (output)
    return (None)


def asBinaryList(num):
    binary = []
    binary[:0] = str(format(num, 'b'))
    print(list(reversed(binary)))


def divide(l, values):
    if len(values) == 0:
        return [l]
    else:
        returns = []
        x = values[0]
        values.remove(x)

        lim = int(x * 2) + 2
        if lim > 2023 - int(x):
            lim = 2024 - int(x)

        for n in range(x + 1, lim):
            major = x * ((x / n) + 1)
            if not (int(major) == major):
                continue
            lHold = l[:]
            lHold.append(major)
            lHold.append(x + n)

            output = divide(lHold, values)
            for y in output:
                returns.append(y)
        return returns


def recDiv2(l, maxDepth):
    global case

    if len(l) >= maxDepth:
        for x in l:
            if l.count(x) > 1 or case.__contains__(x) or not (int(x) == x):
                return (None)
        return (l)
    binary = []
    for x in range(len(l) ** 2 - 1):
        binary = asBinaryList(x + 1)
        divide

    return (None)


edited = True
runs = 0

while True:

    if edited == False:
        if runs >= 2:
            break
        runs += 1

    edited = False
    case.sort()

    for x in (case):
        print(x)

        for y in (case[case.index(x): -1]):
            if x == y:
                continue

            # case.remove(x)
            # case.remove(y)

            division = recSubDiv([], 0, [x, y])
            # division = recSubDivbasic(x-2,0)
            # division = recDiv([x,y],0,runs + 3)

            if division == None:
                # case.append(x)
                # case.append(y)
                continue

            edited = True
            case.remove(x)
            case.remove(y)
            for z in range(len(division)):
                case.append(division[z])
            break
        if edited:
            break
    """
    for y in (case):
        #if x == y :
        #    continue

        division = recSubDivbasic(y - 2,0)

        if division == None:
            continue

        edited = True
        #case.remove(x)
        case.remove(y)
        for z in range(len(division)):
            case.append(division[z])
        break
        """

    print(case)
    open("o1.txt", "w").write(str(case))

case.sort()
print(case, len(case))
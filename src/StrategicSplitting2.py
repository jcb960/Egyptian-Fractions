# import ast

primes = eval(open("PrimeL.txt", "r").read())
case = eval(open("o3.txt", "r").read())
# inList2 = eval(open("JCB2000908.txt","r").read())
# inList2 = eval(open("JCB2000907.txt","r").read())
inList2 = eval(open("JCB2000906.txt", "r").read())

print(len(case))


def recSubDivbasic(passUp, localDepth):
    global case
    if localDepth == 1:
        for x in passUp:
            if case.__contains__(x) or passUp.count(x) > 1:
                return None
        return passUp

    global inList2
    dicti = inList2
    global primes

    valueList = []

    for x in dicti[passUp]:
        valueList.append(sum(x) * max(x))

    valueListHold = valueList[:]

    for y in valueList:
        value = dicti[passUp][valueList.index(max(valueListHold))]

        output = recSubDivbasic(value, localDepth + 1)

        if output != None and not (primes.__contains__(value[0]) or primes.__contains__(value[1])):
            return (output)

        valueListHold.remove(max(valueListHold))

    return (None)


lenCASE = [-1]
edited = False
while True:
    case.sort(reverse=True)
    for y in (case):
        division = recSubDivbasic(y - 2, 0)

        if division == None:
            continue

        edited = True
        case.remove(y)
        for z in range(len(division)):
            case.append(division[z])
        break
    if edited == False:
        break

    print(len(case))
    lenCASE.append(len(case))
    if lenCASE[-1] == lenCASE[-2]:
        break
    del lenCASE[0]

open("o1.txt", "w").write(str(sorted(case)))
case.sort()
print(case, len(case))
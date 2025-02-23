import ast

splitTwoList = eval(open("JCB2000906.txt", "r").read())
splitThreeList = eval(open("JCB2000907.txt", "r").read())
splitFourList = eval(open("JCB2000908.txt", "r").read())


def checkIfNumsIn(bigList, smallList):
    for num in smallList:
        if num in bigList:
            return False

    return True


def sortByNum(kL, target):
    kL.sort()
    belowTarget = list(filter(lambda num: num <= target, kL))
    aboveTarget = list(filter(lambda num: num > target, kL))

    belowTarget.reverse()

    return belowTarget + aboveTarget


kO = [eval(open("o3.txt", "r").read())]
# k.sort()
print(len(kO))
for k in kO:
    alphaLK = [-1, -1]

    while True:

        lengthK = [-1]
        while True:
            k = sortByNum(k, 490)
            for w in range(len(k)):
                q = k[w]
                g = splitFourList[q - 2]

                for j in g:
                    if checkIfNumsIn(k, j):
                        del k[w]
                        k.append(j[0])
                        k.append(j[1])
                        k.append(j[2])
                        k.append(j[3])
                        break

            lengthK.append(len(k))
            if lengthK[-1] == lengthK[-2]:
                break

        alphaLK.append(len(k))
        if alphaLK[-1] == alphaLK[-3]:
            break
        print(len(k))

        lengthK = [-1]
        while True:
            k = sortByNum(k, 645)
            for w in range(len(k)):
                q = k[w]
                g = splitTwoList[q - 2]
                # g.reverse()

                for j in g:
                    if checkIfNumsIn(k, j):
                        del k[w]
                        k.append(j[0])
                        k.append(j[1])
                        break

            lengthK.append(len(k))
            if lengthK[-1] == lengthK[-2]:
                break

        alphaLK.append(len(k))
        if alphaLK[-1] == alphaLK[-3]:
            break
        print(len(k))

        lengthK = [-1]
        while True:
            k = sortByNum(k, 992)
            for w in range(len(k)):
                q = k[w]
                g = splitThreeList[q - 2]
                # g.reverse()

                for j in g:
                    if checkIfNumsIn(k, j):
                        del k[w]
                        k.append(j[0])
                        k.append(j[1])
                        k.append(j[2])
                        break

            lengthK.append(len(k))
            if lengthK[-1] == lengthK[-2]:
                break

        alphaLK.append(len(k))
        if alphaLK[-1] == alphaLK[-3]:
            break
        print(len(k))

    print(len(k), sorted(k))
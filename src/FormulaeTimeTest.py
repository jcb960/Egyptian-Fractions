from fractions import Fraction
import cProfile
import pstats


def generalFormula2(x):
    gF2M = []
    for n in range(1, 962):
        sFD = round((x * x + x * n) / n, 9)

        if sFD.is_integer():
            fFD = x + n

            if x != n and 2 <= fFD <= 2023 and 2 <= sFD <= 2023:
                i = sorted([int(fFD), int(sFD)])

                if i not in gF2M:
                    gF2M.append(i)

    return gF2M


def generalFormulaFrac2(fracX):
    gFF2M = []
    x = eval(str(Fraction(str(1 / fracX)).limit_denominator()))

    for y in range(int(x) + 1, 2024):
        n = y - x
        sFD = round((x * x + x * n) / n, 9)

        if sFD.is_integer():
            fFD = round(x + n, 9)

            if x != n and 2 <= fFD <= 2023 and 2 <= sFD <= 2023:
                i = sorted([int(fFD), int(sFD)])

                if i not in gFF2M:
                    gFF2M.append(i)

    return gFF2M


def generalFormula3(x):
    gF3M = []
    for n in range(int(x) + 1, 2024):
        b = round(1 / ((1 / x) - (1 / n)), 9)

        if b.is_integer():
            r = generalFormula2(b)
        else:
            fB = (1 / x) - (1 / n)
            r = generalFormulaFrac2(fB)

        for t in r:
            if n not in t:
                i = sorted([n, t[0], t[1]])

                if i not in gF3M:
                    gF3M.append(i)

    return gF3M


def generalFormula4(x):
    gF4M = []

    for n in range(x + 1, 2024):
        b = (1 / x) - (1 / n)
        r = generalFormula3(1 / b)

        for t in r:
            if n not in t:
                i = sorted([n, t[0], t[1], t[2]])

                if i not in gF4M:
                    gF4M.append(i)
    return gF4M


def numsToFracs(lM):
    lC = []
    for x in lM:
        lC.append(1 / x)

    return lC


if __name__ == "__main__":
    with cProfile.Profile() as profile:

        splitTwoFile = open("JCB2000906.txt", "r")
        splitTwoList = eval(splitTwoFile.read())
        splitTwoFile.close()

        splitThreeFile = open("JCB2000907.txt", "r")
        splitThreeList = eval(splitThreeFile.read())
        splitThreeFile.close()

        k = [2, 3, 6]

        alphaLK = [-1]

        while True:

            lengthK = [-1]
            while True:
                # k.sort()
                for w in range(len(k)):
                    q = k[w]
                    g = splitTwoList[q - 2]
                    g.reverse()

                    for j in g:
                        if j[0] not in k and j[1] not in k:
                            del k[w]
                            k.append(j[0])
                            k.append(j[1])
                            break

                lengthK.append(len(k))
                if lengthK[-1] == lengthK[-2]:
                    break

            alphaLK.append(len(k))
            if alphaLK[-1] == alphaLK[-2]:
                break

            lengthK = [-1]
            while True:
                k.sort()
                for w in range(len(k)):
                    q = k[w]
                    g = splitThreeList[q - 2]
                    g.reverse()

                    for j in g:
                        if j[0] not in k and j[1] not in k and j[2] not in k:
                            del k[w]
                            k.append(j[0])
                            k.append(j[1])
                            k.append(j[2])
                            break

                lengthK.append(len(k))
                if lengthK[-1] == lengthK[-2]:
                    break

            alphaLK.append(len(k))
            if alphaLK[-1] == alphaLK[-2]:
                break

        print(k)
        print(len(k), sum(numsToFracs(k)))

    results = pstats.Stats(profile)
    results.sort_stats(pstats.SortKey.TIME)
    results.print_stats()



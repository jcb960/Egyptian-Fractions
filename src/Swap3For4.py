soln = eval(open("solutions957.txt", "r").read())
Two = eval(open("JCB2000906.txt", "r").read())
Three = eval(open("JCB2000907.txt", "r").read())
Four = eval(open("JCB2000908.txt", "r").read())

primeSet = eval(open("PrimeL.txt", "r").read())

print(len(soln), soln)


def generalFormulaFrac2(x):
    gFF2M = []

    if x <= 1012:
        lim = int(x * 2) + 2
        if lim > 2023:
            lim = 2024

        for y in range(int(x) + 1, lim):
            n = y - x
            sFD = round(x * (x + n) / n, 9)

            if sFD.is_integer():
                fFD = round(x + n, 9)

                if fFD != sFD and 2 <= fFD <= 2023 and 2 <= sFD <= 2023:
                    i = sorted([int(fFD), int(sFD)])

                    if i not in gFF2M:
                        gFF2M.append(i)

    return gFF2M


def generalFormula3(x, splitTwoL):
    gF3M = []

    if x <= 674:
        lim = int(x * 3) + 2
        if lim > 2023:
            lim = 2024

        for n in range(int(x) + 1, lim):
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


def generalFormula4(x, splitTwoL, splitThreeL):
    gF4M = []

    if x <= 506:
        lim = int(x * 4) + 2
        if lim > 2023:
            lim = 2024

        for n in range(int(x) + 1, lim):
            b = (1 / x) - (1 / n)
            rB = round(1 / b, 9)

            if 1 / b > 674:
                r = []
            elif rB.is_integer():
                r = splitThreeL[int(rB) - 2]
            else:
                r = generalFormula3(1 / b, splitTwoL)

            for t in r:
                if n not in t:
                    i = sorted([n, t[0], t[1], t[2]])

                    if i not in gF4M:
                        gF4M.append(i)

    return gF4M


def checkIfNumsIn(bigList, smallList):
    for num in smallList:
        if num in bigList:
            return False

    return True


counter = 0

while True:

    st1 = False

    for m in range(1, len(soln) - 2):
        f1 = soln[m]
        if f1 in primeSet:
            continue

        for v in range(100, len(soln) - 1):
            f2 = soln[v]
            if f2 in primeSet:
                continue

            for u in range(600, len(soln)):
                f3 = soln[u]
                if f3 in primeSet:
                    continue

                print(f1, f2, f3, counter)

                uF = 1 / (1 / f1 + 1 / f2 + 1 / f3)

                tempSoln = soln.copy()
                tempSoln.remove(f1)
                tempSoln.remove(f2)
                tempSoln.remove(f3)

                if round(uF, 9).is_integer():
                    uF = round(uF, 9)
                    g = Four[int(uF) - 2]
                else:
                    g = generalFormula4(uF, Two, Three)

                for s in g:
                    if checkIfNumsIn(tempSoln, s):
                        soln.append(s[0])
                        soln.append(s[1])
                        soln.append(s[2])
                        soln.append(s[3])

                        soln.remove(f1)
                        soln.remove(f2)
                        soln.remove(f3)

                        soln.sort()
                        upL = soln.copy()

                        qF = open("r3a3.txt", "a")
                        qF.write("\n\n" + str(upL))
                        qF.close()

                        st1 = True
                        counter += 1
                        break
                if st1:
                    break

            if st1:
                break

        if st1:
            break
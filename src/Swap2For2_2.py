"""
Copyright (c) 2025, jcb960.
All rights reserved.

This source code is licensed under the Apache License, Version 2.0 license found in the
LICENSE file in the root directory of this source tree. 
"""

from ast import literal_eval

soln = literal_eval(open("o3.txt", "r").read())
soln.sort()


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


def checkIfNumsIn(bigList, smallList):
    for num in smallList:
        if num in bigList:
            return False

    return True


counter = 0

while True:

    st1 = False

    mSt = False
    vSt = False

    for m in range(0, len(soln) - 1):
        f1 = soln[m]

        for v in (range(m + 1, len(soln))):
            f2 = soln[v]
            uF = 1 / (1 / f1 + 1 / f2)

            tempSoln = soln.copy()
            tempSoln.remove(f1)
            tempSoln.remove(f2)

            g = generalFormulaFrac2(uF)
            g.reverse()

            validSolutions = []

            for s in g:
                if checkIfNumsIn(tempSoln, s):

                    validSolutions.append(s)

                    if sorted([s[0], s[1]]) != sorted([f1, f2]):
                        st1 = True
                    break

            rank = []

            for s in validSolutions:
                rank.append(min(s))

            if len(validSolutions) != 0:
                soln.remove(f1)
                soln.remove(f2)

                soln.insert(m, validSolutions[rank.index(min(rank))][0])
                soln.insert(v, validSolutions[rank.index(min(rank))][1])

            if v == len(soln) - 1:
                vSt = True
            if st1:
                break

        if m == len(soln) - 2:
            mSt = True
        if st1:
            break

    if mSt and vSt:
        break

    counter += 1
    soln.sort()
    print(counter, len(soln), soln)

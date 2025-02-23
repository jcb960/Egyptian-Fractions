"""
Copyright (c) 2025, jcb960.
All rights reserved.

This source code is licensed under the Apache License, Version 2.0 license found in the
LICENSE file in the root directory of this source tree. 
"""

from ast import literal_eval as leval


def checkIfNumsIn(bigList, smallList):
    for num in smallList:
        if num in bigList:
            return False

    return True


def generalFormula2(x):
    gF2M = []

    if x <= 1012:
        lim = int(x*2)+2
        if lim > 2023:
            lim = 2024

        for n in range(1, lim):
            sFD = round(x*(x+n)/n, 9)

            if sFD.is_integer():
                fFD = x+n

                if fFD != sFD and 2 <= fFD <= 2023 and 2 <= sFD <= 2023:
                    i = sorted([int(fFD), int(sFD)])

                    if i not in gF2M:
                        gF2M.append(i)

    return gF2M


def generalFormulaFrac2(x):
    gFF2M = []

    if x <= 1012:
        lim = int(x*2)+2
        if lim > 2023:
            lim = 2024

        for y in range(int(x)+1, lim):
            n = y-x
            sFD = round(x*(x+n)/n, 9)

            if sFD.is_integer():
                fFD = round(x+n, 9)

                if fFD != sFD and 2 <= fFD <= 2023 and 2 <= sFD <= 2023:
                    i = sorted([int(fFD), int(sFD)])

                    if i not in gFF2M:
                        gFF2M.append(i)

    return gFF2M


def generalFormula3(x, splitTwoL):
    gF3M = []

    if x <= 674:
        lim = int(x*3)+2
        if lim > 2023:
            lim = 2024

        for n in range(int(x)+1, lim):
            b = (1/x)-(1/n)
            if b != 0:
                rB = round(1/b, 9)
            else:
                rB = 1/2023

            if 1/b > 1012:
                r = []
            elif rB.is_integer():
                r = splitTwoL[int(rB)-2]
            else:
                r = generalFormulaFrac2(1/b)

            for t in r:
                if n not in t:
                    i = sorted([n, t[0], t[1]])

                    if i not in gF3M:
                        gF3M.append(i)

    return gF3M

def generalFormula4(x, splitTwoL, splitThreeL):
    gF4M=[]
    
    if x<=506:
        lim=int(x*4)+2
        if lim>2023:
            lim=2024        
        
        for n in range(int(x)+1, lim):
            b=(1/x)-(1/n)
            rB=round(1/b, 9)
            
            if 1/b > 674:
                r=[]
            elif rB.is_integer():
                r=splitThreeL[int(rB)-2]
            else:
                r=generalFormula3(1/b, splitTwoL)
            
            for t in r:
                if n not in t:
                    i=sorted([n, t[0], t[1], t[2]])
                
                    if i not in gF4M:
                        gF4M.append(i)
        
    return gF4M

Two = leval(open("JCB2000906.txt", "r").read())
Three = leval(open("JCB2000907.txt", "r").read())
#Four = leval(open("JCB2000908.txt", "r").read())
primeSet = leval(open("PrimeL.txt", "r").read())

soln = leval(open("solutions957.txt", "r").read())
print(len(soln), soln)

while True:

    st1=False
    uSt=False
    vSt=False
    
    lenS = [len(soln)]

    for u in range(91, len(soln)-1):
        frac1 = soln[u]
        
        for v in range(u+1, len(soln)):            
            frac2 = soln[v]
            
            unitFrac = 1/(1/frac1+1/frac2)
            print(u, v, len(soln))

            if unitFrac <= 674:
                rUF = round(unitFrac, 9)

                if rUF.is_integer():
                    g = Three[int(rUF)-2]
                else:
                    g = generalFormula3(unitFrac, Two)

                tempSoln = soln.copy()
                tempSoln.remove(frac1)
                tempSoln.remove(frac2)

                for s in g:
                    if checkIfNumsIn(tempSoln, s):
                        soln.append(s[0])
                        soln.append(s[1])
                        soln.append(s[2])

                        soln.remove(frac1)
                        soln.remove(frac2)
                        break

            lenS.append(len(soln))
            if lenS[-1] > lenS[-2]:
                soln.sort()
                contin = open("o10.txt", "w")
                contin.write(str(soln)+"\n\nLength: "+str(len(soln)))
                contin.close()
                st1=True
                
            del lenS[0]
            
            if st1:
                break
            if v==len(soln)-1:
                vSt=True           

        if st1:
            break
        if u==len(soln)-2:
            uSt=True

    if uSt and vSt:
        break

print(len(soln), soln)


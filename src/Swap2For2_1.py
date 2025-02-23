"""
Copyright (c) 2025, jcb960.
All rights reserved.

This source code is licensed under the Apache License, Version 2.0 license found in the
LICENSE file in the root directory of this source tree. 
"""

from ast import literal_eval as leval

soln = leval(open("o1.txt", "r").read())
soln.sort()
primeSet=leval(open("PrimeL.txt", "r").read())

print(len(soln), soln)

def generalFormulaFrac2(x):
    gFF2M=[]
    
    if x<=1012:
        lim=int(x*2)+2
        if lim>2023:
            lim=2024        

        for y in range(int(x)+1, lim):
            n=y-x
            sFD=round((x*x+x*n)/n, 9)
                
            if sFD.is_integer():
                fFD=round(x+n, 9)
                    
                if fFD!=sFD and 2<=fFD<=2023 and 2<=sFD<=2023:
                    i=sorted([int(fFD), int(sFD)])
                    
                    if i not in gFF2M:
                        gFF2M.append(i)
              
    return gFF2M

def checkIfNumsIn(bigList, smallList):
    for num in smallList:
        if num in bigList:
            return False

    return True

counter=0
allSSS=[]

while True:

    st1=False
    
    mSt=False
    vSt=False
    
    for m in range(0, len(soln)-1):
        f1=soln[m]
        #if f1 in primeSet:
            #continue
        
        for v in range(m+1, len(soln)):
            f2=soln[v]
            #if f2 in primeSet:
                #continue
            
            uF=1/(1/f1+1/f2)
            
            tempSoln = soln.copy()
            tempSoln.remove(f1)
            tempSoln.remove(f2)
            
            g=generalFormulaFrac2(uF)
            #g.reverse()
            
            for s in g:
                if checkIfNumsIn(tempSoln, s):
                    if s[0]<f1 and not(s[0] in primeSet or s[1] in primeSet):
                        soln.append(s[0])
                        soln.append(s[1])

                        soln.remove(f1)
                        soln.remove(f2)
                        
                        soln.sort()
                        upio=soln.copy()
                        allSSS.append(upio)
                        
                        st1=True
                        break
                
            if v==len(soln)-1:
                vSt=True               
            if st1:
                break
            
        if m==len(soln)-2:
            mSt=True
        if st1:
            break

    if mSt and vSt:
        break
    
    counter+=1
    print(counter, len(soln), soln)

fi=open("solnn.txt", "w")
fi.write(str(allSSS))
fi.close()

soln.sort()
print(counter, len(soln), soln)


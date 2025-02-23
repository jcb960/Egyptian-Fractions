"""
Copyright (c) 2025, jcb960.
All rights reserved.

This source code is licensed under the Apache License, Version 2.0 license found in the
LICENSE file in the root directory of this source tree. 
"""

from ast import literal_eval as leval

def generalFormula2(x):
    gF2M=[]
    
    if x<=1012:
        lim=int(x*2)+2
        if lim>2023:
            lim=2024
        
        for n in range(1, lim):
            sFD=round((x*x+x*n)/n, 9)
            
            if sFD.is_integer():
                fFD=x+n
                
                if fFD!=sFD and 2<=fFD<=2023 and 2<=sFD<=2023:
                    i=sorted([int(fFD), int(sFD)])
                
                    if i not in gF2M:
                        gF2M.append(i)
              
    return gF2M

def generalFormulaFrac2(x):
    gFF2M=[]
    
    if x<=1012:
        lim=int(x*2)+2
        if lim>2023:
            lim=2024        

        for y in range(int(x)+1, lim):
            n=y-x
            sFD=round(x*(x+n)/n, 9)
                
            if sFD.is_integer():
                fFD=round(x+n, 9)
                    
                if fFD!=sFD and 2<=fFD<=2023 and 2<=sFD<=2023:
                    i=sorted([int(fFD), int(sFD)])
                    
                    if i not in gFF2M:
                        gFF2M.append(i)
              
    return gFF2M

def generalFormula3(x, splitTwoL):
    gF3M=[]
    
    if x<=674:
        lim=int(x*3)+2
        if lim>2023:
            lim=2024

        for n in range(int(x)+1, lim):
            b=(1/x)-(1/n)
            rB=round(1/b, 9)
            
            if 1/b > 1012:
                r=[]
            elif rB.is_integer():
                r=splitTwoL[int(rB)-2]
            else:
                r=generalFormulaFrac2(1/b)
            
            for t in r:
                if n not in t:
                    i=sorted([n, t[0], t[1]])
                    
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

def generalFormula5(x, splitTwoL, splitThreeL, splitFourL):
    gF5M=[]
    
    if x<=405:
        lim=int(x*5)+2
        if lim>2023:
            lim=2024        

        for n in range(int(x)+1, lim):
            b=(1/x)-(1/n)
            rB=round(1/b, 9)
            
            if 1/b > 506:
                r=[]
            elif rB.is_integer():
                r=splitFourL[int(rB)-2]
            else:
                r=generalFormula4(1/b, splitTwoL, splitThreeL)
            
            for t in r:
                if n not in t:
                    i=sorted([n, t[0], t[1], t[2], t[3]])
                
                    if i not in gF5M:
                        gF5M.append(i)
                        
            print(n, len(gF5M))
    
    return gF5M
"""
Two=eval(open("JCB2000906.txt", "r").read())
Three=eval(open("JCB2000907.txt", "r").read())
Four=eval(open("JCB2000908.txt", "r").read())
"""


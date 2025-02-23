# Egyptian Fractions
 DLT - Computational Thinking Competition
 Problem statement:
    Find a set of unique rationals in the form 1/x that sum to 1 (with 2 <= x <= 2023).

 Colin - Invented formulas and inserted ALL decompositions of unit fractions (from 2 to 2023) into 2, 3, 4 in the JCB... text files
 Patrick - Created algorithms to find the best (longest) solution given the decompositions in the JCB... text files

 I (Colin) found this formula in April 2023, but since I am publishing it now, I'll mark it as found on 2025.
 
 Majority of the people in this competition have found the formula:

 1/x = 1/(x+1) + 1/(x*x + x)

 But there's a formula where instead "1/(x+1)", it goes to "1/(x+n)" where x can be any number
 I believe I am the first one to come across this (I haven't found any of the sort on the internet, I may be wrong)
 Until then I'd like to say I invented it, called "Colin's Fraction Decompostion Formula", and this works for any fraction.

 Colin's Fraction Decompostion Formula
 
 1/x = 1/(x+n) + 1/((x*x + x*n)/n), where 'x' and 'n' can be any number, and it will hold true

 I used this formula to get ALL decompositions of integers from 2 -> 2023, into 2, 3 and 4.
 E.g.

 x=4, n=2
 1/4 = 1/(4+2) + 1/((4*4 + 4*2)/2) = 1/6 + 1/12

 You may wonder, hold on Colin, how do we get 3, and then 4? Do have another formula to get all possible decompositions for 3?
 Well kinda of, remember this formula works for any fractions, not just when trying to get unit fractions.
 So x = [a, b], we use the above formula to split b (could be a UF or non-UF) into [c, d], hence x = [a, c, d]

 Syntax: x = [a, b, ...] which is 1/x = 1/a + 1/b + ...
 So for e.g.
 2 = [3, 7, 42]    well that's obvious because 6 = [7, 42]

 Okay, what about this e.g.
 5 = [6, 31, 930]    well that's obvious again because 30 = [31, 930]

 Well what about this e.g. (!=  - not equal to, unit fraction (UF) = 1/x where 'x' is an integer)
 5 = [12, 15, 20]    1/12 + 1/15 != UF | 1/12 + 1/20 != UF | 1/15 + 1/20 != UF.... wait, this is a valid solution but it wasn't obvious... we know we can catch the obvious ones, but what about the non-obvious ones, so as said before, remember it works for any fraction.

    1/5 = 1/12 + 7/60, remember numerator needs to be 1, so 1/5 = 1/12 + 1/(60/7)
 So 5 = [12, a], 'a' needs to be '60/7' (1/(60/7) = 7/60), we now have to try to get two distinct unit fractions to get '60/7'
 We plug 60/7 as 'x' into the formula, and go through 'n' and find the unit fractions, n = 15 - 60/7 = 45/7
 15 = 60/7 + 45/7,   20 = ((60/7)^2 + (45/7)*(60/7))/(45/7),   and we got 5 = [12, 15, 20]

 Now that we understood that concept, we got all the decompostions into 2 and 3.
 We use the same concept for decompositions into 4 (all the way to infinity)
 But after 4, getting the decompositions will take FOREVER to run even after all the optimizations to minimize the time it needed to run. Which can be seen in the code, and will not be explained here.

 Getting decompositions into 4 (JCB2000908.txt) alone took me 12 continuous hours of running before it gave me that file. So doing 5 was not feasible and hence we stopped at 4, maybe there is a way to get 5 and so on, who knows?
 That explains my formula and understanding behind and how it can be used.
 Please credit me if you're going to use my formula!

 We used the splitting algorithm, start from [2, 3, 6] (sum to 1), then splitting it until it cannot be splitted no more.
 Patrick implemented the an algorithm to pick the best decomposition from the array of decompositions there are for an integer to maximize yield (get the longest set). You can check that out in the code, as I'll be not explaining it!
 Please credit Patrick if you're going to use his algorithms!



 Formula.py - my formulas (algorithms) to get the text files for all decompositions
 FormulaTimeTest.py - using cProfile and pstats to time the functions ('fraction' consumed way too much time, so removed it)
 
 StrategicSplitting1.py - my splitting algorithm (no strategy) got me 856
 StrategicSplitting2.py - Patrick's splitting algorithm (strategy) got 888
 StrategicSplitting3.py - Patrick's splitting algorithm that got us around 950 (implemented after doing 'swapping' algorithm)

 Swap2For2_1.py - Swaps 2 fractions with another 2 fractions. ([10, 15] with [7, 42], to get a smaller number because 7 has more chances of getting split into again)
 Swap2For2_2.py - More strategy to this one which gave better results (from 888 to 910-930)

 Swap2For3.py - Removing 2 fractions and adding 3 fractions (got us 957)
 Swap3For4.py - Removing 3 fractions and adding 4 fractions, Didn't use, took too long but it functions correctly

 2 <= x <= 2023
 JCB2000906.txt - decompositions into 2
 JCB2000907.txt - decompositions into 3
 JCB2000908.txt - decompositions into 4

 PrimeL.txt - Prime numbers between 2 and 2023 (inclusive), for algorithm purposes
 solutions957.txt - Our final submission, we got 957.

 The rest of the text files, are some small submissions in the past

 We secured 3rd place with 957, 10th got 945, ..., 2nd got 958, 1st got 964. A very close battle! Congratulations to the winners and participants for getting this far!
 Again, don't forget to credit us if you're using any of this information, thank you very much!

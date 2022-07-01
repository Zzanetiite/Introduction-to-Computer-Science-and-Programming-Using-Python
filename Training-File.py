# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file / dump file.
"""
"""

t1 = 6+4*10
t2 = (6+4)*10
t3 = 23**5

import math
a = 1
b = 1 
c = 1

x = (-b + (b*b - 4*a*c)**0.5)/(2*a)

t4 = math.cos(3.4)**2+math.sin(3.4)**2

print(t1,t2,t3,x,t4)

import numpy
import matplotlib


num = 10
for num in range(5):
    print(num)
print(num)

school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons)) 

s = 'azcbobobegghakl'
ValidVowels = 'aeiou'
NumberOfVowels = 0

for letter in s :
    if letter in ValidVowels :
        NumberOfVowels += 1
print('Number of vowels:',NumberOfVowels)


s = 'azcbobobegghakl'
s2 = 'bob'
TimesOccurs = 0

for i in (range(len(s))) :
    if i < 2 : continue
    if i > (len(s))-1 : break
    s1 = s[i-2] + s[i-1] + s[i]
    if s1 in s2 :
        TimesOccurs += 1
print(TimesOccurs)


#test two
#s = 'abcbcd'
s = 'azcbobobegghakl'
#the English alphabet from Wikipedia
s2 = 'abcdefghijklmnopqrstuvwxyz'
LongestString = '0'

for i in (range(len(s))) :
    print("i=", s[i])
    if s[i] in s2 :
        i2 = s2.index(s[i])
        LetterCount = 0
        TemporaryString = ''
        while i > i2 :
            LetterCount += 1
            TemporaryString = TemporaryString + s[i]
            if i > len(s)-2 : break
            i += 1
            i3 = s2.index(s[i])
            if i2 > i3 : break
            i2 = i3
            print(TemporaryString)
            print(LetterCount)
        if LetterCount > len(LongestString) :
            LongestString = TemporaryString 
        else :
            LetterCount = 0
            TemporaryString = ''            


print('Longest substring in alphabetical order is:', LongestString)

"""
"""
#How to print from 2 lines:
print("Hi",end='')
print("there")
print("Hi",end='*')
print("there")   

def factorial_test (n):
    prod = 1
    for i in range (1, n + 1) :
        prod *= i
        print('i= ', i)
        print(prod)
    return prod

factorial_test (5)
"""
"""
def recurPower(base, exp):
    if exp == 0 :
        return 1
    if exp == 1 :
        return base
    else :
        return (base * (recurPower(base,(exp-1))))
print(recurPower(2, 6))


def iterPower(base, exp):
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result

print(iterPower(2, 6))

"""
"""
# Hanoi Towers break down.
def printMove(fr, to) :
    print('move from ' + str(fr) + ' to ' + str(to))

# n - the amount of disks to be moved
# fr - stick disk is to be moved from
# to - stick disk is to be moved to
# spare - the free stick   
def Towers(n, fr, to, spare, branch) :
    print(n,fr,to,spare, branch)
    if n == 1 :
        printMove(fr, to)
    else :
        Towers(n-1, fr, spare, to, 1)
        Towers(1, fr, to, spare, 2)
        Towers(n-1, spare, to, fr, 3)
        print('next')
        
print(Towers(4, 'A', 'B', 'C', 'Mother')) 

"""
"""
testList = [1, -4, 8, -9]

def timesFive(a):
    return abs(a)*abs(a)

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
applyToEach(testList, timesFive)

print(testList)
"""
"""
animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

animals['d'] = 'donkey'

animals['a'] = 'anteater'

print('baboon' in animals)

print(animals.values())
"""
"""
def fancy_divide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            fancy_divide(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        print("-2")

"""
"""

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
   try :
       return item / denom
   except ZeroDivisionError:
       return 0
        
        
fancy_divide([0, 2, 4], 0)

"""

"""
def normalize(numbers):
    max_number = max(numbers)
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
    return numbers  

try:
      normalize([0, 0, 0])
except ZeroDivisionError:
      print('Invalid maximum element')

def normalize(numbers):
    max_number = max(numbers)
    assert(max_number != 0), "Cannot divide by 0"
    for i in range(len(numbers)):
        numbers[i]  /= float(max_number)
        assert(0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
    return numbers    

"""















 



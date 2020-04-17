# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 23:15:58 2018

@author: RICHKINWE
"""

cube=36;guess=0.8;h=0.01
num_guesses=0; tolerance=0.0000001
while abs(guess**3-cube)>=tolerance and guess<=cube:
    guess+=h; num_guesses+=1
print('Total guess =', num_guesses)
if abs(guess**3-cube)>=tolerance:
    print(guess, 'Not close to cube root of', cube)
else:
    print(guess,'is the approximate cube root of', cube)

cube=25; high=cube; low=0.0; num_guesses=0
tol=0.01; ans=(high+low)/2.0
while abs(ans**3 - cube)>= tol:
    print('low= '+ str(low)+ 'high= '+ str(high)+ 'ans= ' + str(ans))
    if ans**3 < cube:
        low=ans
    else:
        high=ans
    ans=(high+low)/2.0
    num_guesses+= 1
print('num_guess ='+ str(num_guesses))
print(ans, 'is close to the cube root of', cube)

x=25; high=x; low=0.0; num_guesses=0;
tol=0.00001; ans=(high+low)/2.0;
while abs(ans**2 - x)>= tol:
    print('low= '+ str(low)+ 'high= '+ str(high)+ 'ans= ' + str(ans))
    num_guesses += 1
    if ans**2 > x:
        high = ans
    else:
        low = ans
    ans= (high+low)/2.0
print('num_guess ='+ str(num_guesses))
print(str(ans), 'is close to the square root of', str(x))
if abs(5 - ans)<= tol:
    print('Good approximation!')
else:
    print('Not a good approximation!')
    # To find the cube root of an integer
    x=int(input('Enter an integer:'))
    ans=0
    while ans**3 < x :
        ans +=1
    if ans**3 != x:
            print( ans, ' is not a perfect cube root of', x)
    else:
            print(ans, 'is a perfect cube root of', x)
    # Cube root of a neggative integer
cube=0.25
for guess in range(1,2):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, 'is not a perfect cube ')
else:
    print(cube, 'is a perfect cube root,', guess,' is the root')
        #hailing club
scrabble= 'wtopxzfHCE'

club=input('I will cheer for you, enter your club name:')
times=int(input('Enthusiasm level(1-10):'))
i=0

while i < len(club):
    char=club[i]
    if char in scrabble:
        print('Give me a',char, '!', char)
    else:
        print('Give me an', char, '!', char)
        i+=1
print('What club is that?')
for i in range(times):
    print('Up', club , '!!!')
    #hailingMIT
an_letters= 'wtopxzIfHCEM'
word=input('I will cheer for you, enter a word:')
times=int(input('Enthusiasm level(1-10):'))
i=0

while i < len(word):
    char=word[i]
    if char in an_letters:
        print('Give me an',char, '!', char)
    else:
        print('Give me a', char, '!', char)
        i+=1
print('What word is that?')
for i in range(times):
    print('Up', word , '!!!')

#Newton-rhapson
#To obtain square roots
y=101; tol=0.001; x = y/2.0
Iteration=0
while abs(x**2-y)>= tol:
    Iteration += 1
    x = x-((x**2)-y)/(2*x)
print('No of iteration is' , Iteration)
print(x,'is the approximate square root of', y)

#Binary
num=0.375
if num<0:
    isNeg=True
    num= abs(num)
else:
    isNeg=False
result= ''
if num==0:
    result='0'
while num>0:
    result=str(num%2)+ result
    num=num//2
if isNeg:
    result='-' + result
    
#Binary
x=float(input('Enter a decimal no between 0 and 1:'))
p=0
while ((2**p)*x)%1 !=0:
    print('Remainder='+ str((2**p)*x)- int((2**p)*x))
    p+=1
num=(2**p)*x
result=''
if num==0:
    result='0'
while num>0:
    result=str(num%2)+ result
    num=num//2
for i in range(p- len(result)):
        result='0'+result
result=result[0:-p] + '.' + result[p:]
print('The binary representation of', x, 'is', result)
    
#Vowels
s='asdflkjhyrevxbhtrtinghtolfhur'
numVowels=0
numCons=0
for char in s:
    while char=='a' or char=='e' or char== 'i' or char=='o' or char=='u'in s:
        numVowels+=1
        break
        print('Number of Vowels:', numVowels)    
            
s='asdflkjhyrevxbhtrtinghtolfhur'
vowel=0
while 'a' or 'e' or 'i' or 'o' or 'u'in char(s):
    vowel+=1
    print('Number of vowels:', vowel)
    break
#Exercise
x=100
tol=0.01; h= 0.1; guess=0
while guess <= x:
    if abs(guess**2-x)< tol:
        break
    else:
        guess+=h
if abs(guess**-x)>=tol:
    print('failed')
else:
    print('succeeded:',guess)
        
#Modifications 
x=23
tol=0.01; h= 0.1; guess=0
while abs(guess**2-x)>= tol:
    if guess<=x:
       guess+=h 
    else:
           break
       
if abs(guess**-x)>=tol:
    print('failed')
else:
    print('succeeded:',guess)
    
    #Exc: Guess Search
x=25; high=x; low=0.0; num_guesses=0;
tol=0.00001; ans=(high+low)/2.0;
while abs(ans**2 - x)>= tol:
    print('low= '+ str(low)+ 'high= '+ str(high)+ 'ans= ' + str(ans))
    num_guesses += 1
    if ans**2 > x:
        high = ans
    else:
        low = ans
    ans= (high+low)/2.0
print('num_guess ='+ str(num_guesses))
print(str(ans), 'is close to the square root of', str(x))
if abs(5 - ans)<= tol:
    print('Good approximation!')
else:
    print('Not a good approximation!')
    
x= int(input('Please think of an integer number :'))
high=100; low=0
guessed=False 
#tol=0.00001
while not guessed:
    guess=(high+low)//2.0;
    print('Is your secret number', guess, '?')
    y=input("Enter 'h', 'l' or 'c' to indicate guess is too high, low or correct :")
    if y=='c':
        guessed=True
    elif y=='h':
        high=guess
    elif y=='l':
        low=guess
    else:
        print("Sorry, I did not understand your input.")
print('Game over. Your secret number was:', guess)


def fib(x):
    """ assume x an int >=0
    returns fibonacci of x"""
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)
def feb(x):
    """ assume x an int >=0
    returns fibonacci of x"""
    if x==0 or x==1:
        return 1
    else:
        return feb(x-1)+feb(x-2)
    #Functions
    def is_even(i): 
        """
        input: i is a positive int
        return True if i is even, otherwise False
        """
        print('Hi')
        return i%2==0
is_even(29)
#-------------------------
def square(x):
    '''
    x: int or float
    '''
    return x**2

#--------------------------
    def a(x,y,z):
        if x:
            return y
        else:
            return z
        
    def b(q,r):
        return a(q>r,q,r)
    a(False,2,3)
    #-----------------------
    def printname(firstname,lastname,reverse):
        if reverse:
            print(lastname,',',firstname )
        else:
                print(firstname,',',lastname)
    #--------------------------
    def mult(a,b):
        result=0
        while b>0:
            result+=a
            b-=1
            return result
       
    #--------------------------
    def mul(a,b):
        if b==1:
            return a
        else:
            return a+a*(b-1)
    #---------------------------
    def fact(n):
        if n==1:
            return 1
        else:
            return n*fact(n-1)
    #---------------------------
    def foo(x):
        def bar(z,x=0):
            return z+x
        return bar(3)
    #-----------------------------
    def cube(y):
        return y**3
    
    def fourthpower(x):
        return square(square(x))
    fourthpower(3)
    
    def odd(x):
        return x%2==1
    odd(3)
    #-------------------
    def iterPower(base,exp):
        if exp==0:
            return 1
        else:
            return base*(base**(exp-1))
        iterPower(3,4)
        #------------
    def power(base,exp):
        result=1
        while exp>0:
            result*=base
            exp-=1
            return result
        print(result)
        
        def iterPower(base,exp):
            if exp==0:
                return 1
            else:
                return base*iterPower(base, exp-1)
        print(iterPower(3,4))
        #-----------------------
        import math
        def quad(a,b,c,x):
        #    return x= -b+((b*b-4*a*c)**(0.5))/2*a
   #==================================
   def printMove(fr,to):
       print('move from', fr, 'to',to)
   def towers(n,fr,spare,to):
       if n==1:
           printMove(fr, to)
       else:
           towers(n-1,fr,spare,to)
           towers(1,fr,to,spare)
           towers(n-1,spare,to,fr)
   print(towers(10,'P1','P2','P3'))
   #====================================
   def gcdIter(a,b):
       d=min(a,b)
       while a%d!=0 or b%d!=0:
           d-=1
       return d
   #=====================================
   def gcdRecur(a,b):
       if b==0:
           return a
       else:
           return gcdRecur(b,a%b)
       print(gcdrecur(12,6))
   #====================================
   def Palindrome(s):
       def Char(s):
           s=s.lower()
           ans=''
           for c in s:
               if c in 'abcdefghijklmnopqrstuvwxyz':
                   ans=ans+c
           return ans
       def isPal(s):
           if len(s)<=1:
               return True
           else:
               return s[0]==s[-1] and isPal(s[1:-1])
           
       return isPal(Char(s))
                
       print('')
       print('Is eve a palindrome')
       print(Palindrome('eve'))
       #=====================================
       def isIn(char,aStr):
           if aStr=='':
               return False
           if len(aStr)==1:
               return aStr==char
           midIndex=len(aStr)//2
           midChar=aStr[midIndex]
           if char==midChar:
               return True
           elif char< midChar:
               return isIn(char, aStr[:midIndex])
           else:
               return isIn(char, aStr[midIndex+1:]) 
        #=========================================
        def oddTuples(aTup):
            return aTup[::2]
        
        print(oddTuples('I', 'am', 'a', 'test', 'tuple'))
        #===========================
        def applyToEach(l,f):
            for i in range(len(l)):
                l[i]=f(l[i])
        def divideFive(x):
            return x//5
        
        testList=[5,20,40,45]
        applyToEach(testList,divideFive)
        print(testList)
        #=========================
        def applyFuns(L,x):
            for f in L:
                print(f(x))
            
            
        def divideFive(x):
            return x//5
        
        def MultMinus(x):
            return x*-1
        grades={'Akinwe': 'A', 'Adeseto': 'A+', 'Abiola': 'A+'}
        
        animals={'a':['aardwark'], 'b':['baboon'], 'c':['coati']}
        #==============
        x=int(input('enter an integer :'))
        high=100; low=0; numG=0
        guess=high+low//2
        y=int(input('is your secret number', guess, '?  Enter h,l or c:' ))
        if y=='h':
            high=guess
        elif y=='l':
            low=guess
        elif y=='c'
            break
            print(guess, 'is your secret number')
        else:
            print('Enter a valid entry')
        numG+=1
        guess=high+low//2
        print('Number of guess=', numG)
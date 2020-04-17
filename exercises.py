# -*- coding: utf-8 -*-
"""
Created on Fri May 11 09:29:10 2018

@author: RICHKINWE
"""

def e(d,st):
    '''
    decription: to check maybe character is in a string
    Returns: a boolean if decscription is true
    '''
    if st=='':
        return False
    if len(st)==1:
        return d==st
    mid=len(st)//2
    midchar=st[mid]
    if d==midchar:
        return True
    elif d > midchar:
        return e(d, st[midchar+1:])
    else:
        return e(d, st[0:midchar])
    #===============
    from math import tan,pi
    def polysum(n,s):
        a=0.25*n*s**2/(tan(pi/n)) #area
        p=n*s #perimeter
        return round(a+p**2,4)
    #===============
    def gcdIter(a,b):
        d=min(a,b)
        while a%d != 0 or b%d != 0:
            d-=1
        return d
    
    gcdIter(12,8)
    #==============
    def gcdRecur(a,b):
        if b==0:
            return a
        else:
            return gcdRecur(b, a%b)
            
    gcdRecur(12,8)
    #=============
    def loan(b,mpay,r,n):
        for i in range(1,n+1):
            p=mpay*b
            ub=b-p
            b=ub+((r/12.0)*ub)
            #print('At month',n,'balance=',b)       
        print('Remaining balance:',round(b,2))
        return (round(b,2))
        
        loan(5000,0.02,0.18,12)
#====================
b=int(input('Enter a credit balance: '))
n=12.0; r=18/100; numG=0
lowMR=b/n; highMR=(b*((1+r)**n)/n)
MR=0.5*(lowMR+highMR)
while abs(MR*n - (b+highMR))>0.5:
   # print('lowMR=',lowMR,'highMR=',highMR,'MR=',MR)
    numG+=1
    if MR*n > b+highMR:
        highMR=MR
    else:
        lowMR=MR
    MR=0.5*(lowMR+highMR)  
    print('Number of guesses is:', numG )
    print('Lowest monthly pay is', round(MR))
#===========================
    #import time
    name=input('what is your name: ')
    print('Hello', name, "let's play hangman!")
    print(" ")
    #time.sleep(1)
    print("start guessing")
    #time.sleep(0.5)
    word='secret'
    guesses=''
    turns=10
    while turns >0:
        failed=0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print('_')
            failed+=1
        if failed==0:
            print('You won')
            break
    guess=input('guess a character: ')
    guesses+=guess
    if guess not in word:
        turns-=1
        print('Wrong')
        print('You have', turns, 'more guesses left')
    if turns==0:
        print('You loose')
     # ====HANGMAN=======    
   import random 
   word=['world', 'cook', 'hello', 'goodbye']
   random.shuffle(word)
   answer=list(word[0])
   display=[]; used=[]
   display.extend(answer); used.extend(answer)
   #print(display)
   for i in range(len(display)):
       display[i]='_ '
   print(' '.join(display))    
   print()
   count=0
   while count < len(answer):
       guess=input('Please guess a letter: ')
       guess=guess.lower()
       print(count)
       
       for i in range(len(answer)):
           if answer[i]==guess and guess in used:
               display[i]=guess
               count+=1
               used.remove(guess)
       if guess not in display:
           print('Sorry, it is a wrong guess')
       print('You have guessed', count, 'correct letters')
       print(' '.join(display))
       print()
   print('Well done , you guessed the word')
#===========

club='chelsea manutd mancity spurs arsenal liverpool psg barca'
print('clubs are not up to 12 to form three groups')
club_list= club.split(' ')
#club_list=list(club)
club2=['madrid', 'roma', 'munich', 'everton', 'milan', 'villa', 'bolton']   
while len(club_list)<12:
    add=club2.pop()
    print( "we've added",add)
    club_list.append(add)
    print('we now have', len(club_list),'clubs')
    groups=[club_list[0:4], club_list[4:8],club_list[8:]]
print('The complete list', club_list)
print(groups)
#+++++++++++++GOTHON++++++++++++++++++=
from sys import exit
 from random import randint

 def death():
  quips = ["You died. You kinda suck at this.",
 "Nice job, you died ...jackass.",
 "Such a luser.",
 "I have a small puppy that's better at this."]

 print quips[randint(0, len(quips)-1)]
11 exit(1)
12
13
14 def central_corridor():
15 print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
16 print "your entire crew. You are the last surviving member and your last"
   print "mission is to get the neutron destruct bomb from the Weapons Armory,"
18 print "put it in the bridge, and blow the ship up after getting into an "
19 print "escape pod."
20 print "\n"
21 print "You're running down the central corridor to the Weapons Armory when"
22 print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
23 print "flowing around his hate filled body. He's blocking the door to the"
24 print "Armory and about to pull a weapon to blast you."
25
26 action = raw_input("> ")
27
28 if action == "shoot!":
29 print "Quick on the draw you yank out your blaster and fire it at the Gothon."
30 print "His clown costume is flowing and moving around his body, which throws"
31 print "off your aim. Your laser hits his costume but misses him entirely. This"
32 print "completely ruins his brand new costume his mother bought him, which"
33 print "makes him fly into an insane rage and blast you repeatedly in the face until"
34 print "you are dead. Then he eats you."
35 return 'death'
36
37 elif action == "dodge!":
38 print "Like a world class boxer you dodge, weave, slip and slide right"
39 print "as the Gothon's blaster cranks a laser past your head."
40 print "In the middle of your artful dodge your foot slips and you"
41 print "bang your head on the metal wall and pass out."
42 print "You wake up shortly after only to die as the Gothon stomps on"
43 print "your head and eats you."
44 return 'death'
45
46 elif action == "tell a joke":
47 print "Lucky for you they made you learn Gothon insults in the academy."
48 print "You tell the one Gothon joke you know:"
49 print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
50 print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
51 print "While he's laughing you run up and shoot him square in the head"
52 print "putting him down, then jump through the Weapon Armory door."
53 return 'laser_weapon_armory'
54
55 else:
56 print "DOES NOT COMPUTE!"
57 return 'central_corridor'
58
59 def laser_weapon_armory():
60 print "You do a dive roll into the Weapon Armory, crouch and scan the room"
61 print "for more Gothons that might be hiding. It's dead quiet, too quiet."
62 print "You stand up and run to the far side of the room and find the"
63 print "neutron bomb in its container. There's a keypad lock on the box"
64 print "and you need the code to get the bomb out. If you get the code"
   print "wrong 10 times then the lock closes forever and you can't"
66 print "get the bomb. The code is 3 digits."
67 code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
68 guess = raw_input("[keypad]> ")
69 guesses = 0
70
71 while guess != code and guesses < 10:
72 print "BZZZZEDDD!"
73 guesses += 1
74 guess = raw_input("[keypad]> ")
75
76 if guess == code:
77 print "The container clicks open and the seal breaks, letting gas out."
78 print "You grab the neutron bomb and run as fast as you can to the"
79 print "bridge where you must place it in the right spot."
80 return 'the_bridge'
81 else:
82 print "The lock buzzes one last time and then you hear a sickening"
83 print "melting sound as the mechanism is fused together."
84 print "You decide to sit there, and finally the Gothons blow up the"
85 print "ship from their ship and you die."
86 return 'death'
87
88
89 def the_bridge():
90 print "You burst onto the Bridge with the netron destruct bomb"
91 print "under your arm and surprise 5 Gothons who are trying to"
92 print "take control of the ship. Each of them has an even uglier"
93 print "clown costume than the last. They haven't pulled their"
94 print "weapons out yet, as they see the active bomb under your"
95 print "arm and don't want to set it off."
96
97 action = raw_input("> ")
98
99 if action == "throw the bomb":
100 print "In a panic you throw the bomb at the group of Gothons"
101 print "and make a leap for the door. Right as you drop it a"
102 print "Gothon shoots you right in the back killing you."
103 print "As you die you see another Gothon frantically try to disarm"
104 print "the bomb. You die knowing they will probably blow up when"
105 print "it goes off."
106 return 'death'
107
108 elif action == "slowly place the bomb":
109 print "You point your blaster at the bomb under your arm"
110 print "and the Gothons put their hands up and start to sweat."
111 print "You inch backward to the door, open it, and then carefully"
112 print "place the bomb on the floor, pointing your blaster at it."
    print "You then jump back through the door, punch the close button"
114 print "and blast the lock so the Gothons can't get out."
115 print "Now that the bomb is placed you run to the escape pod to"
116 print "get off this tin can."
117 return 'escape_pod'
118 else:
119 print "DOES NOT COMPUTE!"
120 return "the_bridge"
121
122 def escape_pod():
123 print "You rush through the ship desperately trying to make it to"
124 print "the escape pod before the whole ship explodes. It seems like"
125 print "hardly any Gothons are on the ship, so your run is clear of"
126 print "interference. You get to the chamber with the escape pods, and"
127 print "now need to pick one to take. Some of them could be damaged"
128 print "but you don't have time to look. There's 5 pods, which one"
129 print "do you take?"
130
131 good_pod = randint(1,5)
132 guess = raw_input("[pod #]> ")
133
134
135 if int(guess) != good_pod:
136 print "You jump into pod %s and hit the eject button." % guess
137 print "The pod escapes out into the void of space, then"
138 print "implodes as the hull ruptures, crushing your body"
139 print "into jam jelly."
140 return 'death'
141 else:
142 print "You jump into pod %s and hit the eject button." % guess
143 print "The pod easily slides out into space heading to"
144 print "the planet below. As it flies to the planet, you look"
145 print "back and see your ship implode then explode like a"
146 print "bright star, taking out the Gothon ship at the same"
147 print "time. You won!"
148 exit(0)
149
150
151 ROOMS = {
152 'death': death,
153 'central_corridor': central_corridor,
154 'laser_weapon_armory': laser_weapon_armory,
155 'the_bridge': the_bridge,
156 'escape_pod': escape_pod
157 }
158
159
160 def runner(map, start):
131next = start
162
 while True:
 room = map[next]
 print "\n--------"
 next = room()

 runner(ROOMS, 'central_corridor')
         
 #=============
try:
    a=int(input('Enter an integer: '))
    b=int(input('Enter another integer: '))
    print('a+b=',a+b)
    print('a/b=',a/b)
except ValueError:
    print('cannot divide strings and int')
except ZeroDivisionError:
    print('cannot divide by zero' )
except:
    print('unspecified error')
#++++++++++++        
 def getratio(l1,l2):
     ratio=[] 
     for i in range(len(l1)):
         try: 
             ratio.append(l1[i]/float(l2[i]))
         except ZeroDivisionError:
             ratio.append(float('NaN'))
         except:
             raise ValueError('get ratio called with a bad argument')           
     return ratio
 #++++++++++++++
 L=[[['Adeseto Akinwe'], [84,92,46]],
    [['Abiola Richard'], [85,85,45]],
    ['Oluwatosin Richy',[]]]
#++++++++
def avg(x):
    try:
        return sum(x)/len(x)
    except ZeroDivisionError:
        return 0.0
def testgrade(L):
    newgrade=[]
    for elt in L:
        newgrade.append([elt[0],elt[1],avg(elt[1])])
    return newgrade
#++++++++
def fancy(num,index):
    try:
        den=num[index]
        for i in range(len(num)):
            num[i]/=den
    except IndexError:
            print('-1')
    else:
            print('1')
    finally:
            print('0')
#+++++++
    def fancyd(num,index):
        den=num[index]
        return[sd(item,den) for item in num]
    def sd(item,den):
        try:
            return item/den
        except ZeroDivisionError:
            return 0
  #+++++++++++++
v={'a':1,'b':3,'c':8,'d':6}
v[c]     
     
        
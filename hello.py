# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 05:02:50 2018

@author: RICHKINWE
"""
#print("Hello world")
#print('I like edX')
#if 6>7:
#    print("yep")
#if 6>7:
 #   print("yep")
#else:
 #   print("nope")
#var='Panda'
#if var=="Panda":
 #   print("Cute!")
#elif var=="Panda":
 #   print("Regal!")
#else:
 #   print("Ugly...")
#temp=50
#if temp>85:
 #   print("Hot")
#elif temp>100:
  #  print("REALY HOT!")
#elif temp>60:
   # print("comfortable")
#else:
 #       print("cold")

#x=3**3
#ans=0
#itersLeft=x
#while(itersLeft!=0):
 #   ans=ans+x
  #  itersLeft=itersLeft-1
#print(str(x)+ "*" + str(x)+ "="+ str(ans))

varA=2; varB=3
if type(varA)==str or type(varB)==str:
    print("string involved")
elif varA  > varB:
    print("bigger")#elif varA==varB:
    print("equal")
elif varA!=varB:
    print('not equal')
else: #varA < varB:
    print("smaller")
#num=2
#while num<=10:
 #   print(num)
  #  num+=2
   # print ('Goodbye!')

#num=10
#print('Hello!')
#while num>0:
 #   print (num)
 #   num-=2

#n=10
#print('Hello!')
#while True:
 #   print(n)
 #   n-=2
 #   if n<2:
   #     break
total=0; end=3
current=1
while current <= end:
    total+=current
    current+=1

print(total)

n=0
for i in range(2,12,2):
    n+=2
    print(n)
    print('Goodbye!')
    #====================
    def ModEul(f,a,b,N,IV):
    h = (b-a)/float(N)
    x = np.arange(a,b+h,h)
    y = np.zeros((N+1,))
    x[0],y[0]= IV
    for i in range(1,N+1):
        f1 = f(x[i-1],y[i-1])
        f2 = f(x[i], y[i-1] + h*f1)
        y[i] = y[i-1]+ h*(f1+f2)/2.0
    return x, y


def f(x, y):
    return x**3+x*y


x, y = ModEul(f, 0, 1, 10,(0,1))
for x, y in list(zip(x, y))[:]:
    #print("%4.1f  %10.16f  %10.16f  %12.4e" % (x, y, 3*math.exp(x**2/2)-x**2-2, abs(y-(3*math.exp(x**2/2)-x**2-2))))
    plt.plot(x, y,'rs', label='ModEuler')
    plt.plot(vx, vy, 'b-', label='Runge-Kutta')
    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.title('h=0.1')
    #plt.legend(loc='best')
    plt.grid(True)
    #======================
    kofoworola='black','bold','beauty','brainy'
    for Bcharacter in kofoworola:
        print(list(Bcharacter))
        
    for i in 'clap':
        print(clap(i))
    07069321717
    #=============
    def product(listA,listB):
        result=[]
        for i in (listA,listB):
        #while result < len(listA):
            #ans=(listA[i]*listB[i])
            result=+i
        return result
       # print(result[0]*result[3],result[1]*result[4],result[2]*result[5])
            print( '''
                  this guys are funny
                  i mean they are so weird
                  hence, case closed
                  ''')
    #=================
    p=0; no=[]
    while p<6:
        print(p)
        no.append(p)
        p+=1
        
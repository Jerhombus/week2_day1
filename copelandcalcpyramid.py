import time
print ("Jerome Copeland Week 2 Day 1")
time.sleep(2)
print("\n")
print("Lets calculate two numbers")
time.sleep(1)

def jcalc():
    x = int(input("What's your first number?"+"\n"))
    y = int(input("What's your second number?"+"\n"))
    jfun = input("What function would you like to perform? (A)dd (S)ubtract (M)ultiply (D)ivide+"+"\n")
    if jfun == 'a':
        return (x+y)
    elif jfun == 's':
        return(x-y)
    elif jfun == 'm':
        return(x*y)
    elif jfun == 'd':
        return(x/y)
print (jcalc())
print("\n")
time.sleep(1.5)

print("To be honest, I didn't even know to even approach this next question. The majority of this is copied, but I'm going to attempt to make it interactable."+"\n")
time.sleep(19)
def jtri():
    tri=int(input("Enter a number between 1 and 50."))
    for i in range(1, 2*tri, 2):
        print ('{:^{}}'.format('X'*i, (2*tri)-1))
        
jtri()
print ("\n")
time.sleep(1)
print("At least I figured that much out!")

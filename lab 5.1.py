import math
x=float(input("Введіть x:"))
def f1(x1):
    rez=-9+math.log(x)+math.sqrt(x)
    return(rez)
def f2(x2):
     rez=math.cos(x)+math.sin(2*x)
     return(rez)
def f3(x3):
    rez=math.fabs(-x**+2*x**-x)  
    return(rez)
y=0.0
if x>=5:
     y=f1(x)
elif -0.5<x<5:
    y=f2(x)
elif x<=-0.5:
   y=f3(x)
print(y)
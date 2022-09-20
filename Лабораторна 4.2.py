import math
def func1(t,n,k):
        S=4,17*math.sqrt(t)-math.sin(math.pi*n+math.pi//7)+math.e**(k//t+n)
        return(S)
t1=float(input("Введіть значення t"))
n1=float(input("Введіть значення n"))
k1=float(input("Введіть значення k"))
f=func1(t1,n1,k1)
print(f)
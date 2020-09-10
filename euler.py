import math

def e_cuadratica(n):
    i=0
    result = 0
    while i<=n:
    	result += 1/fact(i)
    	i+=1
    return result

def e_lineal(n):
    i=0
    result = 0
    while i<=n:
    	result += 1/fact(i)
    	i+=1
    return result

def fact(n):
    res=1
    while n>0:
    	res*=n
    	n-=1
    return res

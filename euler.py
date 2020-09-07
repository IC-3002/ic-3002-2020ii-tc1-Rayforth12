import math


def e_cuadratica(n):
    i=0
    result = 0
    while i<=n:
    	factorial = math.factorial(i)
    	result += 1/factorial
    	i+=1
    return result


def e_lineal(n):
    i=0
    result = 0
    while i<=n:
    	result += 1/math.factorial(i)
    	i+=1
    return result
    	

"""
this finction return the nth value in the fibonacci series.(using recursion)
"""
def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1    
    return  fibonacci(n-1)+fibonacci(n-2)

"""
this finction return the nth value in the lucas series.(using recursion)
"""
def lucas(n):
       if n==0:
        return 2
       if n==1:
        return 1    
       return  lucas(n-1)+lucas(n-2)


"""
this function take three params 
the first one  will determine which element in the series to print
the other params will have default values of 0 and 1 and will determine the first two values for the series to be produced.

"""
def sum_series(n,para2=0,para3=1):
     if n==0:
        return para2
     if n==1:
        return para3   
     return  sum_series(n-1,para2,para3)+sum_series(n-2,para2,para3)

"""
outputs
"""
print(fibonacci(7))
print(lucas(7))
print(sum_series(7,2,1))


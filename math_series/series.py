def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1    
    return  fibonacci(n-1)+fibonacci(n-2)


def lucas(n):
       if n==0:
        return 2
       if n==1:
        return 1    
       return  lucas(n-1)+lucas(n-2)



def sum_series(n,para2,para3):
     if n==0:
        return para2
     if n==1:
        return para3   
     return  sum_series(n-1,para2,para3)+sum_series(n-2,para2,para3)

print(fibonacci(7))
print(lucas(7))
print(sum_series(7,0,1))

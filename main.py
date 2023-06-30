def factorial_of_n(n):
    factorial = 1
    for i in range(1,n+1):

     factorial = factorial * i

    return factorial
n = int(input("n=:"))


factorial = factorial_of_n(n)


print ("factorial of " + str(n) + " is :" + str(factorial))

from matplotlib import pyplot as plt

numMods = 0

def fibo(number):
    if number < 2:
        return number

    return fibo(number-1) + fibo(number-2)

def euclidgcd(m, n):
    numMods = 0
    while n != 0:
        r = m % n
        numMods += 1
        m = n
        n = r
    return numMods, n

while True:
    userInp = int(input("1 for User Mode, 2 for Stats Mode: "))

    if userInp == 1:
        selectMode = int(input("1. Fibonacci and Euclid's GCD "))
        if selectMode == 1:

            fibInput = int(input("enter a number to get the fibonacci term and Euclid modulo operations for:"))
            print("Fibonacci of " + str(fibInput) + " is: " + str(fibo(fibInput)))
            print("Number of Euclid modulo operations is: " + str(euclidgcd(fibo(fibInput+1), fibo(fibInput))[0]))

        else:
            break



    if userInp == 5:
        break
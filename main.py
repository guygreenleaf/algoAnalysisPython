from matplotlib import pyplot as plt


numAdditions = 0

def fibo(number):
    global numAdditions
    if number < 2:
        return number
    numAdditions += 1
    return fibo(number-1) + fibo(number-2)

def euclidgcd(m, n):
    numMods = 0
    while n != 0:
        r = m % n
        numMods += 1
        m = n
        n = r
    return numMods, n

def expoOne(a, n):
    if n == 0:
        return 1
    return a * expoOne(a, n-1)

def expoThree(a, n):
    if n == 0:
        return 1
    if n % 2 != 0:
        return a * expoThree(a, (n-1)/2) * expoThree(a, (n-1)/2)
    else:
        return a * expoThree(a, n/2) * expoThree(a, n/2)

def expoTwo(a, n):
    if n == 0:
        return 1
    if n % 2 != 0:
        return a * expoTwo(a, (n-1)/2)**2
    else:
        return expoTwo(a, n/2)**2

def selectionSort(A):
    for i in range(len(A)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

                # Swap the found minimum element with
        # the first element
        A[i], A[min_idx] = A[min_idx], A[i]

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

while True:
    userInp = int(input("1 for User Mode, 2 for Stats Mode: "))

    if userInp == 1:
        selectMode = int(input("Please choose from one of the following options:\n1. Fibonacci and Euclid's GCD\n2. Exponentials\n3.Sorting\n"))
        if selectMode == 1:

            fibInput = int(input("Enter a number to get the fibonacci term and Euclid modulo operations for:"))
            print("Fibonacci of " + str(fibInput) + " is: " + str(fibo(fibInput)) + " and took " + str(numAdditions) + " number of additions to calculate!" )
            print("Number of Euclid modulo operations to find the gcd of fib(k+1) and fib(k) was: " + str(euclidgcd(fibo(fibInput+1), fibo(fibInput))[0]))
            continue

        if selectMode == 2:
            print("Please enter two numbers, to calculate a raised to the n power \n")
            expoInput = int(input("Please enter a number to represent a:"))
            expoTwoInput = int(input("Please enter a number to represent n:\n"))
            print("\nFirst exponential algorithm: " + str(expoOne(expoInput, expoTwoInput)) + "\n")
            print("Second exponential algorithm: " + str(expoTwo(expoInput, expoTwoInput)) + "\n")
            print("Third exponential algorithm: " + str(expoThree(expoInput, expoTwoInput)) + "\n")
            continue

        if selectMode == 3:
            chooseNum = int(input("Please enter the number of elements to sort from 10-100 in increments of 10: "))
            if chooseNum % 10 != 0 or chooseNum < 10 or chooseNum > 100:
                print("Please enter a value from 10-100, in increments of 10 only...")
                continue
            else:
                with open('data/smallSet/data' + str(chooseNum) +'.txt', 'r') as fileStream:
                    sorterList = [int(n) for n in fileStream]

                selectionSort(sorterList)
                print("Selection Sort:")
                print(sorterList)
                with open('data/smallSet/data' + str(chooseNum) +'.txt', 'r') as fileStream:
                    sorterList = [int(n) for n in fileStream]
                insertionSort(sorterList)
                print("Insertion Sort:")
                print(sorterList)
                continue



        else:
            break

    if userInp == 2:
        selectStats = int(input ("1. Fibonacci Statistics "))
        if selectStats == 1:
            plt.style.use('seaborn')
            x = [10, 12, 14, 16, 18, 20]
            y = []
            # y = [fibo(10), fibo(15), fibo(20), fibo(25), fibo(30), fibo(35)]
            fibo(10)
            y.append(numAdditions)
            numAdditions = 0
            fibo(12)
            y.append(numAdditions)
            numAdditions = 0
            fibo(14)
            y.append(numAdditions)
            numAdditions = 0
            fibo(16)
            y.append(numAdditions)
            numAdditions = 0
            fibo(18)
            y.append(numAdditions)
            numAdditions = 0
            fibo(20)
            y.append(numAdditions)

            plt.scatter(x, y, s=100, edgecolor='black', linewidth=1, alpha=0.75)
            plt.title("A(k) for fibonacci(k)")
            plt.xlabel("k")
            plt.ylabel("Number of Additions")
            # plt.tight_layout()
            plt.show()



    if userInp == 5:
        break
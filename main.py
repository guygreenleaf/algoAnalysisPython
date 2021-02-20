from matplotlib import pyplot as plt


numAdditions = 0
numMults = 0

numIterations = 0
def fibo(number):
    global numAdditions
    if number < 2:
        return number
    numAdditions += 1
    return fibo(number-1) + fibo(number-2)

def fiboFaster(n):
    arr = [0, 1]
    i = 2
    while i != n:
        arr.append(arr[i-1] + arr[i-2])
        i += 1
    return int(arr[n-1])


def fiboFasterFullArray(n):
    arr = [0, 1]
    i = 2
    while i != n:
        arr.append(arr[i-1] + arr[i-2])
        i += 1
    return arr

def euclidgcd(m, n):
    nummods = 0
    while n != 0:
        r = m % n
        nummods = nummods + 1
        m = n
        n = r
    return nummods, m

def expoOne(a, n):
    global numMults
    if n == 0:
        return 1
    numMults += 1
    return a * expoOne(a, n-1)

def expoThree(a, n):
    global numMults
    if n == 0:
        return 1
    if n % 2 != 0:
        numMults += 1
        return a * expoThree(a, (n-1)/2) * expoThree(a, (n-1)/2)
    else:
        numMults += 1
        return a * expoThree(a, n/2) * expoThree(a, n/2)

def expoTwo(a, n):
    global numMults
    if n == 0:
        return 1
    if n % 2 != 0:
        numMults += 1
        return a * expoTwo(a, (n-1)/2)**2
    else:
        numMults += 1
        return expoTwo(a, n/2)**2

def selectionSort(A):
    global numIterations
    for i in range(len(A)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(A)):
            numIterations += 1
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
        selectMode = int(input("Please choose from one of the following options:\n1. Fibonacci and Euclid's GCD\n2. "
                               "Exponentials\n3.Sorting\n"))
        if selectMode == 1:

            fibInput = int(input("Enter a number to get the fibonacci term and Euclid modulo operations for:"))
            print("Fibonacci of " + str(fibInput) + " is: " + str(fibo(fibInput)) + " and took " + str(numAdditions) + " number of additions to calculate!" )
            print("Number of Euclid modulo operations to find the gcd of fib(k+1) and fib(k) was: " + str(euclidgcd(fibo(fibInput+1), fibo(fibInput))[0]))
            numAdditions = 0

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
            continue

    if userInp == 2:
        selectStats = int(input ("1. Fibonacci Statistics\n2. Exponential Statistics\n3. Selection Sort\n4. Insertion Sort"))
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


            # a = [fiboFaster(10), fiboFaster(20), fiboFaster(30), fiboFaster(40), fiboFaster(100), 150, 200, 500, 800, 1000, 1200]
            #
            i = 0
            j = 1
            a = []
            b = []
            for x in range(2, 30):
                a.append(fiboFaster(x))

            for y in range(0, 27):
                b.append(euclidgcd(a[y+1], a[y])[0])
            b.append(euclidgcd(fiboFaster(30), fiboFaster(29))[0])
            plt.scatter(a, b, edgecolor='black', linewidth=1, alpha=0.75)
            plt.title("Number of modulo divisions done by EuclidGCD(fib(k+1),fib(k))")
            plt.xlabel("n")
            plt.ylabel("Number of modulo divisions")
            plt.show()

        if selectStats == 2:
            a = 2
            x = [2, 4, 6, 8, 10, 12, 14]
            y = []
            i = 0
            for nums in x:
                expoOne(a, x[i])
                i += 1
                y.append(numMults)
                numMults = 0

            plt.scatter(x, y, edgecolor='black', linewidth=1, alpha=0.75)
            plt.title("Number of multiplications done by exponential algorithm 1")
            plt.xlabel("n")
            plt.ylabel("Multiplications")
            plt.show()
            numMults = 0

            a = 2
            x = []
            for i in range(2, 10000, 2):
                x.append(i)
            y = []
            i = 0
            for nums in x:
                expoTwo(a, x[i])
                i += 1
                y.append(numMults)
                numMults = 0

            plt.scatter(x, y, edgecolor='black', linewidth=1, alpha=0.75)
            plt.title("Number of multiplications done by exponential algorithm 2")
            plt.xlabel("n")
            plt.ylabel("Multiplications")
            plt.show()

            a = 2
            x = []
            for i in range(2, 10000, 2):
                x.append(i)
            y = []
            i = 0
            for nums in x:
                expoThree(a, x[i])
                i += 1
                y.append(numMults)
                numMults = 0

            plt.scatter(x, y, edgecolor='black', linewidth=1, alpha=0.75)
            plt.title("Number of multiplications done by exponential algorithm 3")
            plt.xlabel("n")
            plt.ylabel("Multiplications")
            plt.show()

        if selectStats == 3:
            selectionRandom = []
            selectionNums = []
            selectionSorted = []
            selectionReverseSorted = []
            insertionRandom = []
            insertionSorted = []
            insertionReverseSorted = []





            for a in range(100, 2500, 100):
                selectionNums.append(a)
                with open('data/testSet/data' + str(a) + '.txt', 'r') as fileStream:
                    sorterList = [int(n) for n in fileStream]
                selectionSort(sorterList)
                selectionRandom.append(numIterations)
                numIterations = 0

            plt.scatter(selectionNums, selectionRandom,edgecolor='black', linewidth=1, alpha=0.75 )
            plt.title("Selection Sort, random input")
            plt.xlabel("n")
            plt.ylabel("Comparisons")
            plt.show()
            numIterations = 0

            for a in range(100, 2500, 100):

                with open('data/testSet/data' + str(a) + '_sorted.txt', 'r') as fileStream:
                    sorterList = [int(n) for n in fileStream]
                selectionSort(sorterList)
                selectionSorted.append(numIterations)
                numIterations = 0

            plt.scatter(selectionNums, selectionSorted, edgecolor='black', linewidth=1, alpha=0.75 )
            plt.title("Selection Sort, sorted input")
            plt.xlabel("n")
            plt.ylabel("Comparisons")
            plt.show()

            # need to do reverse sorted selection and all 3 insertions:P


    if userInp == 5:
        break
from matplotlib import pyplot as plt


numAdditions = 0
numMults = 0

numIterations = 0
numIterationsInsertion = 0


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

#Decrase by one
def expoOne(a, n):
    global numMults
    if n == 0:
        return 1
    numMults += 1
    return a * expoOne(a, n-1)

#Divide and conquer
def expoThree(a, n):
    global numMults
    if n == 0:
        return 1
    if n % 2 != 0:
        numMults += 2
        return a * expoThree(a, (n-1)/2) * expoThree(a, (n-1)/2)
    else:
        numMults += 1
        return expoThree(a, n/2) * expoThree(a, n/2)

#Decrease by constant factor
def expoTwo(a, n):
    global numMults
    if n == 0:
        return 1
    if n % 2 != 0:
        numMults += 2
        return a * expoTwo(a, (n-1)/2)**2
    else:
        numMults += 1
        return expoTwo(a, n/2)**2


def selectionSort(Arr, n):
    global numIterations
    for i in range(0, n-1):
        bigIndex = 0
        for j in range(1, n-i):
            numIterations += 1
            if(Arr[j] > Arr[bigIndex]):
                bigIndex = j
        Arr[bigIndex], Arr[n-i-1] = Arr[n-i-1], Arr[bigIndex]


def insertionSort(arr):
    global numIterationsInsertion
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # TWO MORE comparisons in the while statement
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            numIterationsInsertion += 2
        # had to compare two more times to break out the while loop
        numIterationsInsertion += 2
        arr[j + 1] = key


while True:
    userInp = int(input("1. User Input Mode\n2. Stats Mode\n3. Quit: \n"))

    if userInp == 1:
        selectMode = int(input("Please choose from one of the following options:\n1. Fibonacci and Euclid's GCD\n2. "
                               "Exponentials\n3.Sorting\n"))
        if selectMode == 1:

            fibInput = int(input("Enter a number (K) to get the K'th Fibonacci term and Euclid GCD for the next consecutive fibonacci term, fib(k+1) and fib(k):\n"))
            fibOutput = str(fibo(fibInput))
            print("Fibonacci of " + str(fibInput) + " is: " + fibOutput + ". This took " + str(numAdditions) + " number of additions to calculate!" )
            euclGCD = str(euclidgcd(fibo(fibInput+1), fibo(fibInput)))
            print("The GCD of fib(" + str(fibInput+1) + ") and fib(" + str(fibInput) + ") is: " +  "The gcd of Number of Euclid modulo operations to find the gcd of fib(k+1) and fib(k) was: " + euclGCD[0])
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

                selectionSort(sorterList, len(sorterList))
                print(sorterList)
                with open('data/smallSet/data' + str(chooseNum) +'.txt', 'r') as fileStream:
                    sorterList = [int(n) for n in fileStream]
                insertionSort(sorterList)
                print(sorterList)
                numIterations = 0
                numIterationsInsertion = 0
                continue

        else:
            continue

    if userInp == 2:

        selectStats = int(input ("1. Fibonacci Statistics\n2. Exponential Statistics\n3. Sorting Statistics\n"))
        #fibonacci stats
        if selectStats == 1:
            plt.style.use('seaborn')
            x = [10, 12, 14, 16, 18, 20]
            y = []
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
            plt.title("A(k) for fibonacci(k): Θ(n²)")
            plt.xlabel("k")
            plt.ylabel("Number of Additions")
            plt.show()

            i = 0
            j = 1
            #Store consecutive fibonacci terms
            a = []
            #Store number of modulo divisions performed on consecutive fibonacci terms
            b = []
            for x in range(2, 30):
                a.append(fiboFaster(x))

            for y in range(0, 27):
                b.append(euclidgcd(a[y+1], a[y])[0])
            b.append(euclidgcd(fiboFaster(30), fiboFaster(29))[0])
            plt.scatter(a, b, edgecolor='black', linewidth=1, alpha=0.75)
            plt.title("Number of modulo divisions done by EuclidGCD(fib(k+1),fib(k)): Θ(log(n))")
            plt.xlabel("n")
            plt.ylabel("Number of modulo divisions")
            plt.show()

        # exponential statistics
        if selectStats == 2:
            expoGraph = plt.figure()

            expoAx = expoGraph.add_subplot(111)
            print("Please wait, exponential statistics being generated....")
            a = 2
            x = []
            for i in range(3, 995, 3):
                x.append(i)
            y = []
            i = 0
            for nums in x:
                expoOne(a, x[i])
                i += 1
                y.append(numMults)
                numMults = 0

            expoAx.scatter(x, y, s=10, c='b', label='Decrease-by-one: Θ(n)')
            i=0
            # plt.scatter(x, y, edgecolor='black', linewidth=1, alpha=0.75)
            # plt.title("Decrease by 1: Θ(n)")
            # plt.xlabel("n")
            # plt.ylabel("Multiplications")
            # plt.show()
            numMults = 0

            x = []
            for i in range(3, 995, 3):
                x.append(i)
            y = []
            i = 0
            for nums in x:
                expoTwo(a, x[i])
                i += 1
                y.append(numMults)
                numMults = 0

            expoAx.scatter(x, y, s=10, c='r', label='Decrease-by-constant-factor: Θ(log(n))')
            i = 0
            # plt.scatter(x, y, edgecolor='black', linewidth=1, alpha=0.75)
            # plt.title("Decrease-by-constant-factor: Θ(log(n)) ")
            # plt.xlabel("n")
            # plt.ylabel("Multiplications")
            # plt.show()

            x = []
            for i in range(3, 995, 3):
                x.append(i)
            y = []
            i = 0
            for nums in x:
                expoThree(a, x[i])
                i += 1
                y.append(numMults)
                numMults = 0
            expoAx.scatter(x, y, s=10, c='g', label='Divide-and-conquer: Θ(nLog(n))')
            plt.xlabel("n in 2ⁿ")
            plt.ylabel("Number of multiplications")
            expoAx.legend()
            expoGraph.suptitle('Comparison of exponential algorithms')
            i = 0
            plt.show()


        #Sorting statistics
        if selectStats == 3:
            print("Please wait, sorting statistics being generated....")
            selectionRandom = []
            selectionNums = []
            selectionSorted = []
            selectionReverseSorted = []

            insertionRandom = []
            insertionSorted = []
            insertionReverseSorted = []
            # Graph 1
            expoGraph1 = plt.figure()

            expoAx = expoGraph1.add_subplot(111)
            plt.xlabel("Number of elements sorted")
            plt.ylabel("Number of comparisons")
            # Graph 2
            expoGraph2 = plt.figure()

            expoAx2 = expoGraph2.add_subplot(111)
            plt.xlabel("Number of elements sorted")
            plt.ylabel("Number of comparisons")
            # Graph 3
            expoGraph3 = plt.figure()

            expoAx3 = expoGraph3.add_subplot(111)
            plt.xlabel("Number of elements sorted")
            plt.ylabel("Number of comparisons")

            for a in range(500, 10000, 500):
                selectionNums.append(a)

                with open('data/testSet/data' + str(a) + '.txt', 'r') as fileStream:
                    sorterList = [int(n) for n in fileStream]
                selectionSort(sorterList, len(sorterList))
                selectionRandom.append(numIterations)
                numIterations = 0
            expoAx.scatter(selectionNums, selectionRandom, s=10, c='b', label='Selection Sort: Θ(n²)')
            expoGraph1.suptitle("Random Input: ")
            expoAx.legend()


            # plt.scatter(selectionNums, selectionRandom, edgecolor='black', linewidth=1, alpha=0.75)
            # plt.title("Selection Sort, random input")
            # plt.xlabel("n")
            # plt.ylabel("Comparisons")

            numIterations = 0

            for a in range(500, 10000, 500):
                with open('data/testSet/data' + str(a) + '_sorted.txt', 'r') as fileStream:
                    sorterList = [int(n) for n in fileStream]
                selectionSort(sorterList, len(sorterList))
                selectionSorted.append(numIterations)
                numIterations = 0
            expoAx2.scatter(selectionNums, selectionSorted, s=10, c='b', label="Selection Sort Θ(n²)")
            expoGraph2.suptitle("Sorted Input: ")
            expoAx2.legend()
            # plt.scatter(selectionNums, selectionSorted, edgecolor='black', linewidth=1, alpha=0.75)
            # plt.title("Selection Sort, sorted input")
            # plt.xlabel("n")
            # plt.ylabel("Comparisons")
            # plt.show()
            numIterations = 0

            for a in range(500, 10000, 500):
                with open('data/testSet/data' + str(a) + '_rSorted.txt', 'r') as fileStream:
                    sorterList = [int(n) for n in fileStream]
                selectionSort(sorterList, len(sorterList))
                selectionReverseSorted.append(numIterations)
                print("Selection Sort reverse input # comparisons:" + str(numIterations))
                numIterations = 0
            expoAx3.scatter(selectionNums, selectionReverseSorted, s=10, c='b', label='Selection Sort: Θ(n²)')
            expoGraph3.suptitle("Reverse sorted input: ")
            expoAx3.legend()
            # plt.scatter(selectionNums, selectionReverseSorted, edgecolor='black', linewidth=1, alpha=0.75)
            # plt.title("Selection Sort, reverse sorted input")
            # plt.xlabel("n")
            # plt.ylabel("Comparisons")
            # plt.show()
            numIterations = 0

            for a in range(500, 10000, 500):
                with open('data/testSet/data' + str(a) + '.txt', 'r') as fileStream:
                    sorterList = [int(n) for n in fileStream]
                insertionSort(sorterList)
                insertionRandom.append(numIterationsInsertion)
                numIterationsInsertion = 0
            expoAx.scatter(selectionNums, insertionRandom, s=10, c='r', label='Insertion Sort: Θ(n²)')
            expoAx.legend()
            # plt.scatter(selectionNums, insertionRandom, edgecolor='black', linewidth=1, alpha=0.75)
            # plt.title("Insertion Sort, random order")
            # plt.xlabel("n")
            # plt.ylabel("Comparisons")
            # plt.show()
            numIterationsInsertion = 0

            for a in range(500, 10000, 500):
                with open('data/testSet/data' + str(a) + '_sorted.txt', 'r') as fileStream:
                    sorterList = [int(n) for n in fileStream]
                insertionSort(sorterList)
                insertionSorted.append(numIterationsInsertion)
                numIterationsInsertion = 0
            expoAx2.scatter(selectionNums, insertionSorted, s=10, c='r', label='Insertion Sort: Θ(n)')
            expoAx2.legend()
            # plt.scatter(selectionNums, insertionSorted, edgecolor='black', linewidth=1, alpha=0.75)
            # plt.title("Insertion Sort, sorted order")
            # plt.xlabel("n")
            # plt.ylabel("Comparisons")
            # plt.show()
            numIterationsInsertion = 0

            for a in range(500, 10000, 500):
                with open('data/testSet/data' + str(a) + '_rSorted.txt', 'r') as fileStream:
                    sorterList = [int(n) for n in fileStream]
                insertionSort(sorterList)
                insertionReverseSorted.append(numIterationsInsertion)
                print("Insertion Sort rand input # comparisons:" + str(numIterationsInsertion))
                numIterationsInsertion = 0
            expoAx3.scatter(selectionNums, insertionReverseSorted, s=10, c='r', label='Insertion Sort: Θ(n²)')
            expoAx3.legend()
            # plt.scatter(selectionNums, insertionReverseSorted, edgecolor='black', linewidth=1, alpha=0.75)
            # plt.title("Insertion Sort, reverse sorted order")
            # plt.xlabel("n")
            # plt.ylabel("Comparisons")
            plt.show()
            numIterationsInsertion = 0
            # need to do insertion sorts

    if userInp == 3:
        break
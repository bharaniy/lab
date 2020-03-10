a = []
b = int(input("Enter number of elements : "))

for i in range(0, b):
    numbers = int(input())

    a.append(numbers)

print(a)
def printPowerSet(a, b):

    l = []

    for i in range(2 ** b):
        subset = ""
        for j in range(b):
            if (i & (1 << j)) != 0:
                subset += str(a[j]) + "|"
        if subset not in l and len(subset) > 0:
            l.append(subset)


    for subset in l:


        a = subset.split('|')
        for string in a:
            print(string, end=" ")

printPowerSet(a, b)
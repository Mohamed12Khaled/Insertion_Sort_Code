l = []
x = int(input("enter the number of elements in the list"))
for i in range(x):
    y = int(input("enter the number"))
    l.append(y)


def insertion_sort(l):
    for i in range(1, len(l)):
        j = i
        while l[j-1] > l[j] and j > 0:
            l[j], l[j -1] = l[j - 1], l[j]
            j -= 1
            print(l)

insertion_sort(l)
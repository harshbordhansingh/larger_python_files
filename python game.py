def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


alist = []
n = int(input("Enter numbers of elements:"))
for i in range(0, n):
    ele = int(input())
    alist.append(ele)

bubbleSort(alist)
print(alist)


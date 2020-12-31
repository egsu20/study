def selection_sort(aList):
    for i in range(len(aList)):
        least = i
        least_value = aList[i]

        for j in range(i+1, len(aList)):
            if aList[j] < least_value:
                least_value = aList[j]
                least = j

        tmp = aList[i]
        aList[i] = aList[least]
        aList[least] = tmp

list1 = [7,8,5, 1,6]
selection_sort(list1)
print(list1)

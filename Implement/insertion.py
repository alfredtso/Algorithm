#!/bin/python


def InsertionSort(L):
    n = len(L)
    for i in range(1, n):
        print("select {} element as key".format(i))
        key = L[i]  # keep track of the key by implementing a for loop
        j = i-1  # for keep track of the boundary of the sorted and unsorted

        """
        why we need to use while loop instead of reverse range
        because we need to keep track of the position which L[j] is smaller
        than key then we can put the key in the right position
        """

        while (j >= 0 and key < L[j]):
            L[j+1] = L[j]  # swap each element one step to the right
            j -= 1  # moving from right side to left side of the sorted side
            print(L)
        L[j+1] = key  # finally, when put the key in right pos
        print(L)
    return L


def InsertionSortOptimized(l):
    for i in range(1, len(l)):
        if l[i] > l[i-1]:  # only enter the swap loop if ith < i-1 th
            continue
        for j in range(i):
            if l[i] < l[j]:
                l[j], l[j+1:i+1] = l[i], l[j:i]
                break

    return l

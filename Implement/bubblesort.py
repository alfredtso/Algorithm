def BubbleSort(L):
    """
    input: list
    output: sorted list in ascending order
    """
    #traverse through all array elements
    for i in range(len(L)):
        
        #last i elements already inplace i.e the biggests on the right
        for j in range(len(L)-i-1):
            #will swap the biggest to the last
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]

    return L

def BubbleSortimp(L):
    """
    input: list
    output: sorted list in ascending order
    stop if the inner loop doesnt make any swap
    """
    for i in range(len(L)):
        swaped = False
        for j in range(len(L)-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
                swaped = True
        if (swaped == False):
            break
    return L

def BubbleSortRe(L):
    """
    recursiver version
    """

    for i, num in enumerate(L):
        try:
            if L[i+1] < num:
                L[i], L[i+1] = L[i+1], L[i]
                BubbleSortRe(L)
        except IndexError:
            pass
    return L

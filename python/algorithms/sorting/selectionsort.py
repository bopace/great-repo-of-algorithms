# Bo Pace, Sep 2016
# Selection sort
# This is a slight improvement over the bubble sort, because we reduce the
# number of swaps performed. However, the time complexity remains O(n^2).
# Selection sort usually performs better than bubble sort, but we can keep
# improving.

def selectionsort(arr):
    for insert_index in range(len(arr)-1,0,-1):
        max_index = 0
        for i in range(1, insert_index+1):
            if arr[i] > arr[max_index]:
                max_index = i

        arr[insert_index], arr[max_index] = arr[max_index], arr[insert_index]

    return arr

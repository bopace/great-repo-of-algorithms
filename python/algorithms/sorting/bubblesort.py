# Bo Pace, Sep 2016

# This implementation is optimized in the sense that the algorithm only
# checks items in the array that have not already been sorted. After the
# last sort of a round, the new ending index is adjusted accordingly.
# This allows us a best case scenario for a time complexity of O(n) IF
# the array is already sorted, as we simply check each of the items and
# then end. However, the average and worst case are still O(n^2). This
# is pretty bad.

def bubblesort(arr):

    sorted_count = len(arr)
    
    while sorted_count != 0:
        new_count = 0
        for i in range(1, sorted_count):

            if arr[i-1] > arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                new_count = i
        sorted_count = new_count

    return arr


# Vanilla implementation for kicks:

def vanilla_bubblesort(arr):

    for _ in range(len(arr)):
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]

    return arr

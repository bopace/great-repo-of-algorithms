# Bo Pace, Oct 2016
# Quicksort
# Quicksort has a similar divide-and-conquer strategy to that
# of merge sort, but has a space advantage of doing all of the
# sorting in place. The worst case complexity is worse than
# merge sort, however. Quicksort has a best and average case
# complexity of O(nlogn), with a worst case complexity of
# O(n^2). However, the space complexity is only O(logn),
# whereas merge sort has a space complexity of O(n).

def quicksort(arr, first=0, last=None):
    if last == None:
        last = len(arr) - 1
    if first < last:
        split_index = partition(arr, first, last)

        quicksort(arr, first, split_index-1)
        quicksort(arr, split_index+1, last)

    return arr

def partition(arr, first, last):
    pivot_val = arr[first]

    left_mark = first + 1
    right_mark = last

    done = False

    while not done:
        while left_mark <= right_mark and arr[left_mark] <= pivot_val:
            left_mark += 1

        while arr[right_mark] >= pivot_val and right_mark >= left_mark:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            arr[left_mark], arr[right_mark] = arr[right_mark], arr[left_mark]

    arr[first], arr[right_mark] = arr[right_mark], arr[first]

    return right_mark

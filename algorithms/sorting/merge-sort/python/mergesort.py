# Bo Pace, Sep 2016
# Merge sort
# Merge sort makes use of an algorithmic principle known as
# "divide and conquer." In any case (best, worst, average) the
# merge sort will take O(nlogn) time. This is pretty good! The
# O(logn) complexity comes from the fact that in each iteration
# of our merge, we're splitting the list in half. Therefore,
# we'll do logn splits of the array. The O(n) part of the
# complexity comes from adding the parts back together again.

def mergesort(alist):
    if len(alist) > 1:
        mid = len(alist) / 2
        left = mergesort(alist[:mid])
        right = mergesort(alist[mid:])

        new_list = []
        
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                new_list.append(left[i])
                i += 1
            else:
                new_list.append(right[j])
                j += 1

        while i < len(left):
            new_list.append(left[i])
            i += 1

        while j < len(right):
            new_list.append(right[j])
            j += 1

        return new_list
            
    else:
        return alist

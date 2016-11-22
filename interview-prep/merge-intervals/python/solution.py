def merge_intervals(intervals):
    
    # if the list is empty, there's nothing to merge.
    if len(intervals) == 0:
        return intervals
    
    # To make this a little easier on ourselves, let's first sort the
    # intervals by the first element in each interval ( O(logn) )
    intervals = sorted(intervals)
    
    # Keep track of which element we're looking at in the unmerged
    # and the merged list
    unmerged_index = 1
    merged_index = 0
    
    merged_intervals = [intervals[0]]
    
    while unmerged_index < len(intervals):
        # if the start time of the unmerged interval is less than or equal
        # to the end time of the merged interval, there's an overlap.
        if intervals[unmerged_index][0] <= merged_intervals[merged_index][1]:
            # if the end time of the unmerged interval is greater than the
            # end time of the merged interval, merge them by setting the
            # end time of the merged interval to the new end time. Otherwise,
            # it remains the same. Either way, we move the unmerged index up.
            merged_intervals[merged_index][1] = max(merged_intervals[merged_index][1], intervals[unmerged_index][1])
            unmerged_index += 1
        # if the start time of the unmerged interval is greater than the
        # end time of the merged interval, it's a new interval in our merged
        # list.
        else:
            merged_intervals.append(intervals[unmerged_index])
            unmerged_index += 1
            merged_index += 1
    
    # return the merged intervals
    return merged_intervals

# Test cases
# Empty list
print merge_intervals([])

# Our first example
print merge_intervals([[1,4],[2,5],[7,13],[9,12]])

# No overlap
print merge_intervals([[1,3],[4,6],[8,10]])

# One continuous interval
print merge_intervals([[3,6],[1,3],[9,12],[6,9]])

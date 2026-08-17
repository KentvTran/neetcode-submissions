class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        removed = 0
        prevEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            #check overlap: last interval ends after current one starts 
            if prevEnd > intervals[i][0]:
                removed += 1
                #keep one that ends earliest
                prevEnd = min(prevEnd, intervals[i][1])
            #else no overlap
            else:
                prevEnd = intervals[i][1]
        return removed
            
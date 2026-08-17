class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            #newInterval comes BEFORE current Interval
            if newInterval[1] < intervals[i][0]:
                #drop it in and attach rest of list
                res.append(newInterval)
                return res + intervals[i:]
            #newInterval comes AFTER current interval
            elif newInterval[0] > intervals[i][1]:
                #keep moving forward to find where new Interval belongs
                res.append(intervals[i])
            #intervals overlap -> merge
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        #if loop ends then newInterval belongs at the end of list
        res.append(newInterval)

        return res

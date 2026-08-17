class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
         
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            curr = intervals[i]

            #if curr starts before the last interval in res end
            if res[-1][1] >= curr[0]:
                #merge by updating end time
                res[-1][1] = max(res[-1][1], curr[1])
            #no overlap
            else:
                res.append(curr)

        return res
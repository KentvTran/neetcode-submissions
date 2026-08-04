class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, curr, total):
            #base case exact match
            if total == target:
                res.append(curr.copy())
                return
            
            #loop from i to end (prevents backward combinations)
            for j in range(i, len(nums)):
                #prune step: if current sum + next number is greater than target -> no need to continue branch
                if total + nums[j] > target:
                    return
                #else add current number to our path
                curr.append(nums[j])
                #recursive call; pass j not j+1, cause we can reuse same number
                dfs(j, curr, total + nums[j])

                #undo choice so we can go back up the tree
                curr.pop()

        dfs(0, [], 0)
        return res
        
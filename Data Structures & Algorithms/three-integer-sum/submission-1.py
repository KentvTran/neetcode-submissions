class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, anchor in enumerate(nums):
            #if anchor is positive everything to right is also positive so we can never sum to 0
            if anchor > 0:
                break
            
            # skip duplicate anchors
            if i > 0 and anchor == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                threeSum = anchor + nums[left] + nums[right]
                
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else: 
                    result.append([anchor, nums[left], nums[right]])
                    left +=1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return result

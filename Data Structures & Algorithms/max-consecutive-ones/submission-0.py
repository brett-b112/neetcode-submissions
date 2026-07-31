class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        output = 0
        curr_max = 0
        for i in range(len(nums)):

            if nums[i] == 1:
                curr_max += 1
            else:
                curr_max=0

            if curr_max > output:
                output = curr_max
                
        return output
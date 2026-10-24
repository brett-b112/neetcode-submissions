class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        counter = 0 
        for elem in nums:
            if elem == 1:
                counter += 1
                if counter >= max_len:
                    max_len = counter
                    
            elif elem == 0:
                if counter >= max_len:
                    max_len = counter
                counter = 0
        return max_len
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = -1
        nums.sort(reverse=True)
        
        counter = 0
        for elem in nums:
            if elem != -1:
                counter += 1
        
        return counter
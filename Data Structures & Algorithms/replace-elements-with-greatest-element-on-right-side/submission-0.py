class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_arr = []
        for i in range(len(arr) - 1):
            max_right = max(arr[i+1:len(arr)])
            new_arr.append(max_right)
        new_arr.append(-1)
        return new_arr
        
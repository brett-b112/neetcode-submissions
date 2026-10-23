import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    maxheap = []
    for num in nums:
        pair = (-num, num)
        heapq.heappush(maxheap, pair)
    
    res = []
    while maxheap:
        res.append(heapq.heappop(maxheap)[1])
    return res




# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))

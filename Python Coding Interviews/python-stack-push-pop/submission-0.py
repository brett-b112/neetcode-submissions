from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    mylist = []
    aLen = len(arr)
    for i in range(aLen): 
        mylist.append(arr.pop())
    return mylist


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))

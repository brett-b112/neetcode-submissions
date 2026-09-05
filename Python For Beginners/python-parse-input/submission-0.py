from typing import List

def read_integers() -> List[int]:
    num_list = input()
    num_list = num_list.split(",")

    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())

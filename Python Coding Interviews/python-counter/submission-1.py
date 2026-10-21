from collections import Counter
from typing import Counter as CounterType


def count_chars(s1: str, s2: str) -> CounterType:
    comb = s1 + s2
    counter = Counter(comb)
    return counter
    # count = defaultdict(int)
    # for char in comb:
    # count[char] += 1
  

# do not modify below this line
print(count_chars("hello", "world"))
print(count_chars("hello", "worldhello"))
print(count_chars("areallylongstring", "heyhowisitgoing"))

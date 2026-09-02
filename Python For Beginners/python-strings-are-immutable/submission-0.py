def remove_fourth_character(word: str) -> str:
    before_4 = word[:3]
    after_4 = word[4:]
    return before_4 + after_4

# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))

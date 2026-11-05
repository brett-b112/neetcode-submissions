class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        misses = 0
        while students and misses < len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                misses = 0
            else:
                misses += 1
                students.append(students.pop(0))
        return misses
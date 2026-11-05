class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        lengthStud = len(students)
        countStud = Counter(students)

        for sand in sandwiches:
            if countStud[sand] >= 1:
                countStud[sand] -= 1
                lengthStud -= 1
            else:
                break

        return lengthStud
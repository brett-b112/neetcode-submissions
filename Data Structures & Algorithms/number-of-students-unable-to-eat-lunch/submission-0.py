
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # 0 is circular sandwich
        # 1 is square sandwich
        circ = students.count(0)
        sqr = students.count(1)

        for sandwich in sandwiches:
            if sandwich == 0 and circ > 0:
                circ -=1
            elif sandwich == 1 and sqr > 0:
                sqr-=1
            else:
                return circ + sqr

        return 0

        
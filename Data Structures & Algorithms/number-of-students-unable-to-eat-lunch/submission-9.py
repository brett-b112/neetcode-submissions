class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sco = students.count(0)
        scn = students.count(1)

        for s in sandwiches:
            if s == 0 and sco > 0:
                sco -= 1
            elif s == 1 and scn > 0:
                scn -= 1
            else: 
                break
            
        return scn + sco
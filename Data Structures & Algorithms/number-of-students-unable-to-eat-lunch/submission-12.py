class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studQ = deque(students)
        studS = deque(sandwiches)
        misses = 0

        while studQ and misses < len(studQ):
            if studQ[0] == studS[0]:
                studQ.popleft()
                studS.popleft()
                misses = 0
            else:
                misses += 1
                studQ.append(studQ.popleft())
        return misses
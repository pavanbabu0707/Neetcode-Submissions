class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        count_0 = students.count(0)
        count_1 = students.count(1)

        for sandwich in sandwiches:
            if sandwich == 0:
                if count_0 > 0:
                    count_0 -= 1 
                else:
                    return count_1

            else:
                if sandwich == 1:
                    if count_1 > 0:
                        count_1 -= 1
                    else:
                        return count_0

        return 0
        
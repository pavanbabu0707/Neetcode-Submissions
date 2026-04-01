class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        n = len(operations)

        for i in range(n):
            if operations[i] == '+':
                score.append(score[-1] + score[-2])
            elif operations[i] == 'D':
                score.append(2 * score[-1])
            elif operations[i] == 'C':
                score.pop()
            else:
                score.append(int(operations[i]))

        return sum(score)

        
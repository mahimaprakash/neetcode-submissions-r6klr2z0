class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                prev = stack[-1]
                stack.append(2 * prev)
            elif op == "+":
                prev_1 = stack[-1]
                prev_2 = stack[-2]
                stack.append(prev_1 + prev_2)
            else:
                stack.append(int(op))
            print(stack)
        return sum(stack)
from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = []
        stack = [0] * len(temperatures)
        for idx, i in enumerate(temperatures):
            while temp_stack and (temp_stack[-1][1] < i):
                t_idx, temp = temp_stack.pop()
                stack[t_idx] = idx - t_idx            
            temp_stack.append((idx, i))

        return stack     

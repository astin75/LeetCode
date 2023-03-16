from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = list(Counter(tasks).values())
        max_count = max(task_count) 
        count_max_task = task_count.count(max_count) # A and B
        count_idle = max_count -1
        place = n + 1
        return max(len(tasks), (count_idle * place + count_max_task))
        
        
        
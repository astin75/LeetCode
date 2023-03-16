from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        n_place = n +1 # a__ A __
        task_count = list(Counter(tasks).values())
        max_count = max(task_count)
        max_count_task = task_count.count(max_count)
        count_idle = max_count - 1
        total_count = count_idle * n_place + max_count_task
        return max(len(tasks), total_count)
        
        
        
        
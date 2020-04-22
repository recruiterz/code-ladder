class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 가장 많은 task 띄엄띄엄 배치 
        # 가장 많은 task 사이에 n 개씩 idle 배치
        
        # idle의 자리를 줄여나가자.


        counter = dict()
        
        for t in tasks:
            count = counter.setdefault(t, 0)
            count += 1
            counter[t] = count
            
        largest_task_count = max(counter.values())
        
        
        for task, count in counter.items():
            if count == largest_task_count:
                del counter[task]
                break

            
        idle_time = n * (largest_task_count - 1)
        
        for count in counter.values():
            if idle_time <= 0:
                break
            idle_time = idle_time - min(count, largest_task_count - 1)
            
        idle_time = max(0, idle_time)
        return len(tasks) + idle_time
        

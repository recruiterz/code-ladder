class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        c1 = costs[0]
        c7 = costs[1]
        c30 = costs[2]
        
        last_day = days[-1]
        days_set = set(days)
        
        d = [0] * (last_day + 1)
        d[0] = 0
        
        for i in range(1, last_day + 1):
            
            if i not in days_set:
                d[i] = d[i - 1]
                continue
            
            d1 = d[i - 1] + c1
            d7 = d[max(i - 7, 0)] + c7
            d30 = d[max(i - 30, 0)] + c30
            
            d[i] = min(d1, d7, d30)
        return d[-1]

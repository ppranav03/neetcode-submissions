class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total = 0
        clock = customers[0][0]

        for arrival, prep_time in customers:
            if clock < arrival:
                clock = arrival
            clock += prep_time
            total += clock - arrival
        
        return float(total / len(customers))
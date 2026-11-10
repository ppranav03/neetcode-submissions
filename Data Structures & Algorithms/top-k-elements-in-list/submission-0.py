import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        
        my_heap = []
        for num, count in counts.items():
            heapq.heappush(my_heap, (count, num))
            if len(my_heap) > k:
                heapq.heappop(my_heap)
        

        values = [num for _ , num in my_heap]

        return values
import heapq

def solution(intervals):
    intervals = sorted(intervals, key = lambda x: x[0])
    min_heap = []
    heapq.heapify(min_heap) 
    heapq.heappush(min_heap, intervals[0][1])
    for interval in intervals[1::]:
        if min_heap[0] <= interval[0]:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, interval[1])
    return len(min_heap)

if __name__ == "__main__":
    intervals = [[0, 5], [5, 10], [15, 20], [20, 25]]
    print(solution(intervals))
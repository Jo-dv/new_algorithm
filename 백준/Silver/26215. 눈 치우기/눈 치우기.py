import heapq

class Main:
    def __init__(self):
        self.n = int(input())
        self.house = list(map(int, input().split()))
        self.answer = 0

    def solve(self):
        if self.n == 1:
            print(self.house[0] if self.house[0] <= 1440 else -1)
            return

        heap = [-h for h in self.house]
        heapq.heapify(heap)

        while len(heap) > 1:
            house1 = -heapq.heappop(heap)  # 가장 큰 값
            house2 = -heapq.heappop(heap)  # 두 번째 큰 값
            self.answer += house2
            new_house = house1 - house2

            if new_house > 0:
                heapq.heappush(heap, -new_house)

        if heap:
            self.answer += -heapq.heappop(heap)

        print(-1 if self.answer > 1440 else self.answer)


problem = Main()
problem.solve()

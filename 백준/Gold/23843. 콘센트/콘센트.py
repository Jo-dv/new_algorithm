from heapq import *


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.times = list(map(int, input().split()))
        self.answer = 0

    def solve(self):
        hq = []
        for time in self.times:
            heappush(hq, (-time, time))

        while len(hq) > self.m:
            min_num = 2**15 + 1
            temp = []
            for i in range(self.m):
                weight, num = heappop(hq)
                min_num = min(min_num, num)
                temp.append(num)

            for i in temp:
                new_num = i - min_num
                if new_num > 0:
                    heappush(hq, (-new_num, new_num))

            self.answer += min_num

        print(self.answer if not hq else self.answer + heappop(hq)[1])


problem = Main()
problem.solve()
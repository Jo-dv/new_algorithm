import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.t, self.n = map(int, input().split())
        self.process = [tuple(map(int, input().split())) for _ in range(self.n)]

    def solve(self):
        hq = []
        table = {}
        current_time = 0

        for process in self.process:
            pc_id, run_time, priority = process
            heapq.heappush(hq, (-priority, pc_id))
            table[pc_id] = run_time

        while current_time < self.t:
            if hq:
                priority, pc_id = heapq.heappop(hq)
                print(pc_id)
                if table[pc_id] - 1 > 0:
                    table[pc_id] -= 1
                    heapq.heappush(hq, (priority + 1, pc_id))  # 다른 프로세스 레벨을 높이지 말고 현재 프로세스 레벨을 낮춤
            else:
                break

            current_time += 1

problem = Main()
problem.solve()
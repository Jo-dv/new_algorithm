from heapq import *


class Main:
    def __init__(self):
        self.n = int(input())
        self.nodes = [tuple(map(int, input().split())) for _ in range(self.n)]

    def solve(self):
        in_degree = [0] * (self.n + 1)
        graph = [[] for _ in range(self.n + 1)]
        build_time = [0] * (self.n + 1)  # 각 건물의 건설 시간
        dp = [0] * (self.n + 1)  # 최소 시간
        hq = []

        for i, node in enumerate(self.nodes, 1):
            build_time[i] = node[0]  # 첫 번째 값이 건설 시간
            for pre in node[1:-1]:  # 마지막 -1 제외
                graph[pre].append(i)
                in_degree[i] += 1  # 진입 차수 증가

        for i in range(1, self.n + 1):
            if in_degree[i] == 0:
                heappush(hq, (build_time[i], i))  # (건설 완료 시간, 건물 번호)
                dp[i] = build_time[i]

        while hq:
            current_time, current = heappop(hq)  # 현재까지의 최소 시간, 현재 건물

            for nxt in graph[current]:
                in_degree[nxt] -= 1  # 선행 건물 제거
                dp[nxt] = max(dp[nxt], dp[current] + build_time[nxt])  # 최소 시간 갱신
                if in_degree[nxt] == 0:
                    heappush(hq, (dp[nxt], nxt))  # 다음 건물 삽입

        for i in range(1, self.n + 1):
            print(dp[i])


problem = Main()
problem.solve()

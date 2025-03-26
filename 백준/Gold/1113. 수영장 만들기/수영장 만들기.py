from collections import deque


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.pool = [list(map(int, list(input()))) for _ in range(self.n)]
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.answer = 0

    def search(self, y, x):
        visited = [[False] * self.m for _ in range(self.n)]
        visited[y][x] = True
        dq = deque([(y, x)])
        origin_pool = [(y, x)]
        current_height = self.pool[y][x]
        optimal_height = 10  # 최적의 높이 탐색

        while dq:
            ny, nx = dq.popleft()

            for dy, dx in self.directions:
                my, mx = ny + dy, nx + dx

                if 0 <= my < self.n and 0 <= mx < self.m:
                    if self.pool[my][mx] <= current_height:
                        if not visited[my][mx]:
                            dq.append((my, mx))
                            visited[my][mx] = True
                            origin_pool.append((my, mx))
                    else:  # 높이 갱신
                        optimal_height = min(optimal_height, self.pool[my][mx])
                else:  # 가장자리를 계산 범위에서 제외
                    return

        for y, x in origin_pool:
            self.answer += (optimal_height - self.pool[y][x])
            self.pool[y][x] = optimal_height  # 물 채워짐

    def solve(self):
        for i in range(1, self.n - 1):  # 가장자리는 물을 채울 수 없다
            for j in range(1, self.m - 1):
                self.search(i, j)

        print(self.answer)


problem = Main()
problem.solve()

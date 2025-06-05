from collections import deque, defaultdict


class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.light_info = [tuple(map(lambda i: int(i)-1, input().split())) for _ in range(self.m)]

    def is_valid(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n

    def solve(self):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        lights = defaultdict(list)
        for light in self.light_info:
            x, y, a, b = light
            lights[(x, y)].append((a, b))

        visited = [[False] * self.n for _ in range(self.n)]
        visited[0][0] = True
        check = [[False] * self.n for _ in range(self.n)]  # 불 확인
        check[0][0] = True
        dq = deque([(0, 0)])

        while dq:
            x, y = dq.popleft()

            for light in lights[(x, y)]:
                a, b = light
                if not check[a][b]:
                    check[a][b] = True
                    for dx, dy in directions:
                        mx, my = a + dx, b + dy
                        if self.is_valid(mx, my) and visited[mx][my]:
                            dq.append((a, b))
                            visited[a][b] = True
                            break

            for dx, dy in directions:
                mx, my = x + dx, y + dy
                if self.is_valid(mx, my) and not visited[mx][my] and check[mx][my]:
                    visited[mx][my] = True
                    dq.append((mx, my))

        print(sum(sum(i) for i in check))


problem = Main()
problem.solve()

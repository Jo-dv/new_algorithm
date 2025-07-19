class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())

    def solve(self):
        x, y = 0, 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 동, 남, 서, 북
        d = 0

        left, right = 0, self.n - 1
        top, bottom = 0, self.m - 1

        while True:
            nx = x + directions[d][0]
            ny = y + directions[d][1]

            if left <= nx <= right and top <= ny <= bottom:
                x, y = nx, ny
            else:
                if d == 0:
                    top += 1
                elif d == 1:
                    right -= 1
                elif d == 2:
                    bottom -= 1
                elif d == 3:
                    left += 1

                d = (d + 1) % 4  # 방향 전환

                nx = x + directions[d][0]
                ny = y + directions[d][1]

                if not (left <= nx <= right and top <= ny <= bottom):
                    break
                x, y = nx, ny

        print(x, y)


problem = Main()
problem.solve()

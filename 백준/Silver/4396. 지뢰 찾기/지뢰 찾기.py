class Main:
    def __init__(self):
        self.n = int(input())
        self.bombs = [list(input()) for _ in range(self.n)]
        self.pos = [list(input()) for _ in range(self.n)]

    def solve(self):
        answer = [["."] * self.n for _ in range(self.n)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        flag = False

        for i in range(self.n):
            for j in range(self.n):
                if self.pos[i][j] == "x":
                    if self.bombs[i][j] == "*":
                        if not flag:
                            flag = True
                    else:
                        answer[i][j] = "0"

        if flag:
            for i in range(self.n):
                for j in range(self.n):
                    if self.bombs[i][j] == "*":
                        answer[i][j] = "*"

        for i in range(self.n):
            for j in range(self.n):
                if self.bombs[i][j] == "*":
                    for dy, dx in directions:
                        my, mx = i + dy, j + dx
                        if 0 <= my < self.n and 0 <= mx < self.n and answer[my][mx].isdigit():
                            answer[my][mx] = str(int(answer[my][mx]) + 1)

        for i in answer:
            print("".join(i))


problem = Main()
problem.solve()

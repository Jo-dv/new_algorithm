import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n = int(input())
        self.students = [list(map(int, input().split())) for _ in range(self.n)]

    def solve(self):
        info = {i: 0 for i in range(1, self.n+1)}

        for standard in range(1, self.n+1):
            for other in range(1, self.n+1):
                if standard == other:
                    continue
                for i in range(5):
                    if self.students[standard-1][i] == self.students[other-1][i]:
                        info[standard] += 1
                        break

        result = sorted(list(info.items()), key=lambda i: (-i[1], i[0]))
        print(result[0][0])


problem = Main()
problem.solve()

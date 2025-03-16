class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.arr = [list(map(int, input().split())) for _ in range(self.n)]
        self.k = int(input())
        self.partition = [list(map(int, input().split())) for _ in range(self.k)]

    def solve(self):
        acc_arr = [[0] * (self.m + 1) for _ in range(self.n + 1)]
        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                acc_arr[i][j] = self.arr[i-1][j-1] + acc_arr[i][j - 1]

        for j in range(1, self.m + 1):
            for i in range(1, self.n + 1):
                acc_arr[i][j] += acc_arr[i-1][j]

        for cord in self.partition:
            i, j, x, y = cord
            print(acc_arr[x][y] - acc_arr[i-1][y] - acc_arr[x][j-1] + acc_arr[i-1][j-1])


problem = Main()
problem.solve()

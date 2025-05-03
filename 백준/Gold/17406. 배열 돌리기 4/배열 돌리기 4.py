class Main:
    def __init__(self):
        self.n, self.m, self.k = map(int, input().split())
        self.arr = [list(map(int, input().split())) for _ in range(self.n)]
        self.info = [list(map(int, input().split())) for _ in range(self.k)]
        self.answer = float('inf')

    def rotate(self, arr, idx):
        r, c, s = self.info[idx]
        temp = [row[:] for row in arr]

        for layer in range(1, s + 1):
            top = r - layer - 1
            left = c - layer - 1
            bottom = r + layer - 1
            right = c + layer - 1

            for j in range(left + 1, right + 1):  # 위쪽
                temp[top][j] = arr[top][j - 1]

            for i in range(top + 1, bottom + 1):  # 오른쪽
                temp[i][right] = arr[i - 1][right]

            for j in range(right - 1, left - 1, -1):  # 아래쪽
                temp[bottom][j] = arr[bottom][j + 1]

            for i in range(bottom - 1, top - 1, -1):  # 왼쪽
                temp[i][left] = arr[i + 1][left]

        return temp

    def search(self, used, arr, depth=0):
        if depth == self.k:
            self.answer = min(self.answer, min(sum(i) for i in arr))
            return

        for i in range(self.k):
            if used[i]:
                continue

            used[i] = True
            temp = self.rotate(arr, i)
            self.search(used, temp, depth+1)
            used[i] = False

    def solve(self):
        self.search([False for _ in range(self.k)], [row[:] for row in self.arr])
        print(self.answer)


problem = Main()
problem.solve()

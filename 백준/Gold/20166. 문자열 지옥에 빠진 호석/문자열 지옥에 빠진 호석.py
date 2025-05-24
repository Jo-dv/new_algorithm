import sys
sys.setrecursionlimit(1000000)
from collections import defaultdict

N, M, K = map(int, input().split())
grid = [input().strip() for _ in range(N)]
words = [input().strip() for _ in range(K)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)]

# dp[word][x][y][i] = number of ways to form word[i:] starting at (x, y)
answers = []

for word in words:
    dp = [[[-1] * len(word) for _ in range(M)] for _ in range(N)]

    def dfs(x, y, idx):
        if grid[x][y] != word[idx]:
            return 0
        if idx == len(word) - 1:
            return 1
        if dp[x][y][idx] != -1:
            return dp[x][y][idx]
        
        res = 0
        for dx, dy in dirs:
            nx = (x + dx + N) % N
            ny = (y + dy + M) % M
            res += dfs(nx, ny, idx + 1)
        
        dp[x][y][idx] = res
        return res

    total = 0
    for i in range(N):
        for j in range(M):
            total += dfs(i, j, 0)
    answers.append(total)

for ans in answers:
    print(ans)

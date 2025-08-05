class Main:
    def __init__(self):
        self.p = int(input())
        self.boards = []
        for _ in range(self.p):
            board = [list(input()) for _ in range(3)]
            self.boards.append(board)

    def toggle(self, board, y, x):
        for dy, dx in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < 3 and 0 <= nx < 3:
                board[ny][nx] = '*' if board[ny][nx] == '.' else '.'

    def solve_one(self, target):
        min_clicks = float('inf')
        for mask in range(512):  # 0~511
            board = [['.']*3 for _ in range(3)]
            clicks = 0
            for i in range(9):
                if (mask >> i) & 1:
                    y, x = divmod(i, 3)
                    self.toggle(board, y, x)
                    clicks += 1
            if board == target:
                min_clicks = min(min_clicks, clicks)
        return min_clicks

    def solve(self):
        for board in self.boards:
            print(self.solve_one(board))


problem = Main()
problem.solve()
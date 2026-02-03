import sys
sys.setrecursionlimit(10**6)

class Main:
    def __init__(self):
        self.n = int(input())
        self.papers = [list(map(int, input().split())) for _ in range(self.n)]
        self.answer = {-1: 0, 0: 0, 1: 0}
    
    def search(self, y, x, size):
        target = self.papers[y][x]
        same = True

        for i in range(y, y+size):
            for j in range(x, x+size):
                if target != self.papers[i][j]:
                    same = False
                    break
            if not same:
                break
        
        if same:
            self.answer[target] += 1
            return

        new_size = size // 3
        for dy in (0, new_size, 2*new_size):
            for dx in (0, new_size, 2*new_size):
                self.search(y + dy, x + dx, new_size)

    
    def solve(self):
        self.search(0, 0, self.n)
        for i in self.answer.values():
            print(i)
            
problem = Main()
problem.solve()
class Main:
    def __init__(self):
        self.n = int(input())
        self.info = [tuple(input().split()) for _ in range(self.n)]
        
    def solve(self):
        dance = {"ChongChong"}

        for i in self.info:
            a, b = i
            if a not in dance and b not in dance:
              continue
            dance.add(a)
            dance.add(b)
        
        print(len(dance))


problem = Main()
problem.solve()
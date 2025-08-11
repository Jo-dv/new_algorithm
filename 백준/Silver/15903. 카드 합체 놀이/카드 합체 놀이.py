class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.nums = list(map(int, input().split()))
        
    def solve(self):
        for _ in range(self.m):
            self.nums.sort()
            x, y = self.nums[0], self.nums[1]
            z = x + y
            self.nums[0] = self.nums[1] = z
            
        print(sum(self.nums))

        
problem = Main()
problem.solve()
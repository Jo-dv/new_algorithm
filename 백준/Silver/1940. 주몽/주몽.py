class Main:
    def __init__(self):
        self.n = int(input())
        self.m = int(input())
        self.nums = list(map(int, input().split()))
        self.answer = 0

    def solve(self):
        self.nums.sort()
        low = 0
        high = self.n-1

        while low < high:
            check = self.nums[low] + self.nums[high]
            if check == self.m:
                self.answer += 1
                low += 1
                high -= 1
            elif check < self.m:
                low += 1
            else:
                high -= 1

        print(self.answer)


problem = Main()
problem.solve()

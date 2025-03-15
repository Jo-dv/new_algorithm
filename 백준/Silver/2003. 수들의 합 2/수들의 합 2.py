class Main:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.arr = list(map(int, input().split()))
        self.answer = 0

    def solve(self):
        low, high = 0, 0
        temp = 0
        while high <= self.n:
            if temp == self.m:
                self.answer += 1
                temp -= self.arr[low]
                low += 1
            elif temp < self.m:
                if high < self.n:
                    temp += self.arr[high]
                high += 1
            else:
                temp -= self.arr[low]
                low += 1

        print(self.answer)


problem = Main()
problem.solve()

class Main:
    def __init__(self):
        self.d, self.n = map(int, input().split())
        self.oven = list(map(int, input().split()))
        self.pizzas = list(map(int, input().split()))  # 맨 앞이 먼저 들어간 피자
        self.answer = 0

    def solve(self):
        for i in range(1, self.d):
            self.oven[i] = min(self.oven[i], self.oven[i - 1])
        pos = self.d

        for pizza in self.pizzas:
            low, high = 0, pos - 1
            idx = -1

            while low <= high:
                mid = (low + high) // 2
                if self.oven[mid] >= pizza:
                    idx = mid
                    low = mid + 1
                else:
                    high = mid - 1

            if idx == -1:
                print(0)
                return
            pos = idx

        print(pos + 1)


problem = Main()
problem.solve()

class Main:
    def __init__(self):
        self.n = 123456 * 2
        self.prime = [True] * (self.n + 1)

    def solve(self):
        for i in range(2, int(self.n**0.5) + 1):
            if self.prime[i]:
                for j in range(i**2, int(self.n) + 1, i):
                    self.prime[j] = False

        while True:
            test_case = int(input())
            if test_case == 0:
                return
            cnt = 0
            for i in range(test_case + 1, test_case * 2 + 1):
                if self.prime[i]:
                    cnt += 1

            print(cnt)


problem = Main()
problem.solve()
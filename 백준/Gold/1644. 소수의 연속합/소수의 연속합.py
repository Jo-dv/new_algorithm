class Main:
    def __init__(self):
        self.n = int(input())
        self.answer = 0

    def make_prime(self):
        prime = [True] * (self.n + 1)

        for i in range(2, int(self.n ** 0.5) + 1):
            if prime[i]:
                for j in range(i ** 2, self.n + 1, i):
                    prime[j] = False

        return [i for i in range(2, self.n + 1) if prime[i]]

    def solve(self):
        if self.n == 1:
            print(0)
            return

        prime = self.make_prime()
        high = 0
        target = 0

        for low in range(len(prime)):
            while target < self.n and high < len(prime):
                target += prime[high]
                high += 1

            if target == self.n:
                self.answer += 1
            target -= prime[low]

        print(self.answer)


problem = Main()
problem.solve()
class Main:
    def __init__(self):
        self.tc = int(input())

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def solve(self):
        for _ in range(self.tc):
            n = int(input())
            while True:
                if self.is_prime(n):
                    print(n)
                    break
                n += 1


problem = Main()
problem.solve()

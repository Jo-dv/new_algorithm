class Main:
    def __init__(self):
        self.n = int(input())
        self.current_tap = list(map(int, input().split()))
        self.correct_tap = list(map(int, input().split()))
        self.answer = 0

    def solve(self):
        diff = [self.correct_tap[i] - self.current_tap[i] for i in range(self.n)]

        i = 0
        while i < self.n:
            if diff[i] == 0:
                i += 1
                continue

            sign = 1 if diff[i] > 0 else -1
            min_val = abs(diff[i])

            j = i
            while j < self.n and (diff[j] * sign) > 0:
                min_val = min(min_val, abs(diff[j]))
                j += 1

            self.answer += min_val

            for k in range(i, j):
                diff[k] -= sign * min_val

        print(self.answer)


problem = Main()
problem.solve()

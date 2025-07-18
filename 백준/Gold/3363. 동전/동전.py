class Main:
    def __init__(self):
        self.measurements = []
        while len(self.measurements) < 3:
            parts = input().split()
            if not parts:
                parts = input().split()
            left = list(map(int, parts[:4]))
            op = parts[4]
            right = list(map(int, parts[5:9]))
            self.measurements.append((left, op, right))

    def check(self, coin, weight):
        for left, op, right in self.measurements:
            left_sum = sum(weight if c == coin else 0 for c in left)
            right_sum = sum(weight if c == coin else 0 for c in right)

            if op == '=' and left_sum != right_sum:
                return False
            elif op == '<' and not (left_sum < right_sum):
                return False
            elif op == '>' and not (left_sum > right_sum):
                return False
        return True

    def solve(self):
        candidates = []
        for coin in range(1, 13):
            for weight in [1, -1]:
                if self.check(coin, weight):
                    candidates.append((coin, weight))

        if len(candidates) == 0:
            print("impossible")
        elif len(candidates) > 1:
            print("indefinite")
        else:
            coin, weight = candidates[0]
            print(f"{coin}{'+' if weight == 1 else '-'}")


problem = Main()
problem.solve()

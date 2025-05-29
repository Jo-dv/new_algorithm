from typing import List


class Main:
    def __init__(self):
        self.n = int(input())
        self.a = list(map(int, input().split()))
        self.m = int(input())
        self.b = list(map(int, input().split()))

    def search(self, a, b, result: List):
        if not a or not b:
            return result

        val1, val2 = max(a), max(b)
        idx1, idx2 = a.index(val1), b.index(val2)

        if val1 == val2:
            result.append(val1)
            return self.search(a[idx1 + 1:], b[idx2 + 1:], result)
        elif val1 > val2:
            a.pop(idx1)
            return self.search(a, b, result)
        else:
            b.pop(idx2)
            return self.search(a, b, result)

    def solve(self):
        answer = self.search(self.a, self.b, [])

        print(len(answer))
        if answer:
            print(*answer)


problem = Main()
problem.solve()

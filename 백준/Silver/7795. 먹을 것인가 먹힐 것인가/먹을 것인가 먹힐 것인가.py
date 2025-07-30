import sys
import bisect
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.t = int(input())
        self.answer = []

    def solve(self):
        for _ in range(self.t):
            a, b = map(int, input().split())
            a_arr = list(map(int, input().split()))
            b_arr = list(map(int, input().split()))
            cnt = 0
            b_arr.sort()

            for i in a_arr:
                cnt += bisect.bisect_left(b_arr, i)

            self.answer.append(cnt)

        for i in self.answer:
            print(i)


problem = Main()
problem.solve()
import sys


class Main:
    def solve(self):
        data = sys.stdin.read().split()
        n = int(data[0])
        nums = data[1:]

        reversed_nums = [int(s[::-1]) for s in nums]
        reversed_nums.sort()

        for num in reversed_nums:
            print(num)


problem = Main()
problem.solve()

class Main:
    def __init__(self):
        self.t = int(input())

    def solve(self):
        for _ in range(self.t):
            n = int(input())
            trace = {i: 0 for i in range(1, n+1)}
            targets = [int(input()) for _ in range(n)]
            for i in range(n):
                trace[i+1] = targets[i]

            call = 0
            current = 1
            while call < n:
                nxt = trace[current]
                if nxt == n:
                    print(call + 1)
                    break

                call += 1
                current = nxt
            else:
                print(0)


problem = Main()
problem.solve()
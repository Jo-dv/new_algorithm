class Main:
    def __init__(self):
        self.n = int(input())
        self.limit = list(map(int, input().split()))
        self.m = int(input())
        self.box = list(map(int, input().split()))

    def solve(self):
        self.limit.sort(reverse=True)
        self.box.sort(reverse=True)

        if self.limit[0] < self.box[0]:
            print(-1)
            return

        time = 0
        while self.box:
            idx = 0
            for crane in self.limit:
                if idx >= len(self.box):
                    break
                while idx < len(self.box):
                    if crane >= self.box[idx]:
                        self.box.pop(idx)
                        break
                    else:
                        idx += 1

            time += 1

        print(time)


problem = Main()
problem.solve()

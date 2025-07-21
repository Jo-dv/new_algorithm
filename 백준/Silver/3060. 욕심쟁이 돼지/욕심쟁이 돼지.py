class Main:
    def __init__(self):
        self.t = int(input())
        self.n = None
        self.feeds = None
        self.answer = []

    def solve(self):
        for _ in range(self.t):
            self.n = int(input())
            self.feeds = list(map(int, input().split()))
            day = 1

            while sum(self.feeds) <= self.n:
                new_feeds = [0] * 6
                for i in range(6):
                    new_feeds[i] = self.feeds[i] + self.feeds[i-1] + self.feeds[(i+1) % 6] + self.feeds[i+3 if i < 3 else i-3]
                self.feeds = new_feeds
                day += 1

            self.answer.append(day)

        for i in self.answer:
            print(i)


problem = Main()
problem.solve()
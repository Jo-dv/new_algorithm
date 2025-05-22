class Main:
    def __init__(self):
        self.n = int(input())
        self.emotions = list(map(int, input().split()))
        self.answer = 0

    def search_period(self):
        periods = []
        day = 0

        while day < self.n:
            if self.emotions[day] < 0:
                start = day
                while day < self.n and self.emotions[day] < 0:
                    day += 1
                end = day - 1
                t = end - start + 1
                periods.append((start, end, t))
            else:
                day += 1

        return periods

    def solve(self):
        periods = self.search_period()
        if not periods:
            print(0)
            return 
        
        max_t = max(periods, key=lambda p: p[2])[2]
        flowered = set()

        for start, end, t in periods:
            start_day = max(0, start - 2 * t)
            end_day = start - 1

            for day in range(start_day, end_day + 1):
                flowered.add(day)

        for start, end, t in periods:
            if t == max_t:
                start_day = max(0, start - 3 * t)
                end_day = start - 1

                cnt = 0
                for day in range(start_day, end_day + 1):
                    if day not in flowered:
                        cnt += 1

                self.answer = max(self.answer, cnt + len(flowered))

        print(self.answer)


problem = Main()
problem.solve()

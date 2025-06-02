class Main:
    def __init__(self):
        self.n, self.l = map(int, input().split())
        self.traffic_lights = [tuple(map(int, input().split())) for _ in range(self.n)]
        self.answer = 0

    def solve(self):
        distance = 0

        for d, r, g in self.traffic_lights:
            self.answer += (d - distance)
            distance = d

            term = r + g
            if self.answer % term < r:
                self.answer += (r - self.answer % term)

        self.answer += (self.l - distance)
        print(self.answer)


problem = Main()
problem.solve()
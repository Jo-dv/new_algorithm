class Main:
    def __init__(self):
        self.tc = int(input())

    def is_square(self, pts):
        def dist(p1, p2):
            return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
        dists = sorted([dist(pts[i], pts[j]) for i in range(4) for j in range(i + 1, 4)])
        return (
            dists[0] > 0 and
            dists[0] == dists[1] == dists[2] == dists[3] and
            dists[4] == dists[5] and
            dists[4] == 2 * dists[0]
        )

    def solve(self):
        for _ in range(self.tc):
            cord = [tuple(map(int, input().split())) for _ in range(4)]
            if self.is_square(cord):
                print(1)
            else:
                print(0)


problem = Main()
problem.solve()

from itertools import combinations as cb


class Main:
    def __init__(self):
        self.n, self.k = map(int, input().split())
        self.house = [tuple(map(int, input().split())) for _ in range(self.n)]
        self.answer = 200001

    def solve(self):
        shelters = set(cb(self.house, self.k))

        for shelter in shelters:
            current_optimal = 0  # 현대 대피소 조합중 최적의 답
            for i in self.house:
                distance = 200001
                for j in shelter:
                    temp = abs(i[0] - j[0]) + abs(i[1] - j[1])
                    distance = min(temp, distance)  # 가장 가까운 대피소와의 거리
                current_optimal = max(current_optimal, distance)  # 중 최대값
            self.answer = min(self.answer, current_optimal)  # 을 최소로

        print(self.answer)


problem = Main()
problem.solve()

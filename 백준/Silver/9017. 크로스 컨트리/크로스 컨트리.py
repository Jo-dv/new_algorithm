from collections import Counter


class Main:
    def __init__(self):
        self.t = int(input())

    def solve(self):
        for _ in range(self.t):
            n = int(input())
            teams = list(map(int, input().split()))
            check = Counter(teams)
            table = dict()

            score = 1
            for team in teams:
                if check[team] < 6:
                    continue
                if team not in table:
                    table[team] = [score]
                else:
                    table[team].append(score)
                score += 1

            for k, v in table.items():
                table[k] = [k, sum(v[:4]), v[4]]

            table = list(table.values())
            table.sort(key=lambda x: (x[1], x[2]))
            print(table[0][0])


problem = Main()
problem.solve()

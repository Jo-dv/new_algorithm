import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n = int(input())
        self.info = [input() for _ in range(self.n * 2)]

    def solve(self):
        in_car = {car: i for i, car in enumerate(self.info[:self.n])}
        out_car = {car: i for i, car in enumerate(self.info[self.n:])}

        correct = 0
        out_car_list = list(out_car.keys())
        for i in range(self.n-1):
            current = in_car[out_car_list[i]]
            for j in range(i+1, self.n):
                nxt = in_car[out_car_list[j]]
                if nxt < current:
                    correct += 1
                    break

        print(correct)


problem = Main()
problem.solve()
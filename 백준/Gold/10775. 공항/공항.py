import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.g = int(input())
        self.p = int(input())
        self.airplanes = [int(input()) for _ in range(self.p)]
        self.parents = [i for i in range(self.g + 1)]
        self.answer = 0

    def find(self, x):
        if x == self.parents[x]:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, gate, next_gate):
        gate = self.find(gate)
        next_gate = self.find(next_gate)
        if gate == next_gate:
            return 
        self.parents[gate] = next_gate

    def solve(self):
        for airplane in self.airplanes:
            target_gate = self.find(airplane)
            if target_gate == 0:
                break
            self.union(target_gate, target_gate - 1)
            self.answer += 1

        print(self.answer)


problem = Main()
problem.solve()
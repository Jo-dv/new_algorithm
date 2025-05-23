class Main:
    def __init__(self):
        self.s = input()
        self.t = input()

    def search(self, data):
        if data == self.s:
            return True
        if len(data) < len(self.s):
            return False
        if data[-1] == "A":
            if self.search(data[:-1]):
                return True
        if data[0] == "B":
            reversed_data = data[::-1][:-1]
            if self.search(reversed_data):
                return True
        return False

    def solve(self):
        answer = self.search(self.t)
        print(1 if answer else 0)


problem = Main()
problem.solve()
class Main:
    def __init__(self):
        self.string = input()
        self.visited = [False] * len(self.string)

    def search(self, left, right):
        if left > right:
            return

        idx = left

        for i in range(left, right+1):
            if self.string[i] < self.string[idx]:
                idx = i

        self.visited[idx] = True

        for i in range(len(self.string)):
            if self.visited[i]:
                print(self.string[i], end="")
        print()

        self.search(idx+1, right)
        self.search(left, idx-1)

    def solve(self):
        self.search(0, len(self.string)-1)


problem = Main()
problem.solve()

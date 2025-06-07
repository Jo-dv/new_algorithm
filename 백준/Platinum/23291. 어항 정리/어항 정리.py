class Main:
    def __init__(self):
        self.n, self.k = map(int, input().split())
        self.arr = list(map(int, input().split()))
        self.answer = 0

    def find(self):
        min_value = min(self.arr)

        for i in range(self.n):
            if self.arr[i] == min_value:
                self.arr[i] += 1

    def stack(self):
        self.arr = [[self.arr[0]], self.arr[1:]]

        while True:
            w = len(self.arr[-2])
            if len(self.arr) > len(self.arr[-1]) - w:
                break
            arr1 = [i[:w] for i in self.arr]
            arr2 = list(map(list, zip(*arr1[::-1])))
            self.arr = arr2 + [self.arr[-1][w:]]

    def adjust(self):
        self.arr: list[list]
        new_arr = [i[:] for i in self.arr]

        for row in range(len(self.arr)):
            for col in range(len(self.arr[row])):
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    mr, mc = row + dr, col + dc
                    if 0 <= mr < len(self.arr) and 0 <= mc < len(self.arr[mr]) and self.arr[row][col] > self.arr[mr][mc]:
                        d = abs(self.arr[row][col] - self.arr[mr][mc]) // 5
                        if d > 0:
                            new_arr[row][col] -= d
                            new_arr[mr][mc] += d

        self.arr = new_arr

    def flatten(self):
        self.arr: list[list]
        result = []

        for col in range(len(self.arr[-1])):
            for row in range(len(self.arr)-1, -1, -1):
                if col < len(self.arr[row]):
                    result.append(self.arr[row][col])

        self.arr = result

    def fly(self):
        half = len(self.arr) // 2
        new_arr = [self.arr[:half][::-1]] + [self.arr[half:]]

        half //= 2
        left = [i[:half] for i in new_arr]
        self.arr = [i[::-1] for i in left[::-1]]
        self.arr += [i[half:] for i in new_arr]

    def solve(self):
        while max(self.arr) - min(self.arr) > self.k:
            self.find()
            self.stack()
            self.adjust()
            self.flatten()
            self.fly()
            self.adjust()
            self.flatten()
            self.answer += 1

        print(self.answer)


problem = Main()
problem.solve()

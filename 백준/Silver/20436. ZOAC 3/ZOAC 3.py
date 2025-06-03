class Main:
    def __init__(self):
        self.l, self.r = input().split()
        self.target = input()
        self.answer = 0

    def cal_distance(self, x1, x2, y1, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def solve(self):
        keyboard = {
            "q": (0, 2), "w": (1, 2), "e": (2, 2), "r": (3, 2), "t": (4, 2), "y": (5, 2), "u": (6, 2), "i": (7, 2), "o": (8, 2), "p": (9, 2),
            "a": (0, 1), "s": (1, 1), "d": (2, 1), "f": (3, 1), "g": (4, 1), "h": (5, 1), "j": (6, 1), "k": (7, 1), "l": (8, 1),
            "z": (0, 0), "x": (1, 0), "c": (2, 0), "v": (3, 0), "b": (4, 0), "n": (5, 0), "m": (6, 0)
        }  # (x, y)

        left = keyboard[self.l]
        right = keyboard[self.r]

        for i in self.target:
            current = keyboard[i]
            if (current[0] <= 3 and current[1] == 0) or (current[0] <= 4 and current[1] >= 1):  # 왼손
                self.answer += self.cal_distance(left[0], current[0], left[1], current[1]) + 1
                left = current
            else:
                self.answer += self.cal_distance(right[0], current[0], right[1], current[1]) + 1
                right = current

        print(self.answer)


problem = Main()
problem.solve()
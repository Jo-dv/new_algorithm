class Main:
    def __init__(self):
        self.n = int(input())
        self.string = [input().strip() for _ in range(self.n)]
        self.answer = []

    def solve(self):
        left = 0
        right = self.n - 1

        while left <= right:
            l = left
            r = right
            take_left = False

            while l <= r:
                if self.string[l] < self.string[r]:
                    take_left = True
                    break
                elif self.string[l] > self.string[r]:
                    take_left = False
                    break
                else:
                    l += 1
                    r -= 1

            if take_left:
                self.answer.append(self.string[left])
                left += 1
            else:
                self.answer.append(self.string[right])
                right -= 1

        for i in range(0, len(self.answer), 80):
            print(''.join(self.answer[i:i + 80]))


problem = Main()
problem.solve()

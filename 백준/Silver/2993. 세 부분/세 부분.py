class Main:
    def __init__(self):
        self.word = input()
        self.answer = None

    def solve(self):
        for i in range(1, len(self.word) - 1):
            for j in range(i + 1, len(self.word)):
                part1 = self.word[:i][::-1]
                part2 = self.word[i:j][::-1]
                part3 = self.word[j:][::-1]
                new_word = part1 + part2 + part3
                if self.answer is None or new_word < self.answer:
                    self.answer = new_word

        print(self.answer)


problem = Main()
problem.solve()
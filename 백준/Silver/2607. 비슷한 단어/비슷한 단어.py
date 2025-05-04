from collections import Counter


class Main:
    def __init__(self):
        self.n = int(input())
        self.words = [input() for _ in range(self.n)]
        self.base = self.words[0]  # 첫 번째 단어 기준
        self.answer = 0

    def is_similar(self, word1, word2):
        c1 = Counter(word1)
        c2 = Counter(word2)

        if c1 == c2:
            return True

        if abs(len(word1) - len(word2)) > 1:
            return False

        diff = 0
        for char in set(c1.keys()).union(c2.keys()):  # 추가, 삭제, 변경 중 하나만 허용됨
            diff += abs(c1[char] - c2[char])

        return diff == 1 or diff == 2 and len(word1) == len(word2)

    def solve(self):
        for i in range(1, self.n):  # 첫 번째 단어와만 비교
            if self.is_similar(self.base, self.words[i]):
                self.answer += 1
        print(self.answer)


problem = Main()
problem.solve()
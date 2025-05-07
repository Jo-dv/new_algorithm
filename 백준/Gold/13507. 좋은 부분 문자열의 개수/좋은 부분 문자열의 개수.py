from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False


class Main:
    def __init__(self):
        self.s = input()
        self.bit = list(map(int, input()))
        self.k = int(input())
        self.answer = 0

    def solve(self):
        root = TrieNode()

        for i in range(len(self.s)):
            node = root
            bad_cnt = 0

            for j in range(i, len(self.s)):
                ch = self.s[j]
                idx = ord(ch) - ord('a')

                if self.bit[idx] == 0:
                    bad_cnt += 1
                if bad_cnt > self.k:
                    break

                if ch not in node.children:
                    self.answer += 1

                node = node.children[ch]

        print(self.answer)


problem = Main()
problem.solve()

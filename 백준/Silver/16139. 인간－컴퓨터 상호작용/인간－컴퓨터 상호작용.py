class Main:
    def __init__(self):
        self.s = input()
        self.q = int(input())
        self.queries = [list(input().split()) for _ in range(self.q)]

    def solve(self):
        acc_dict = {chr(i): [0] * (len(self.s) + 1) for i in range(97, 123)}

        for i in range(len(self.s)):
            for c in range(97, 123):  # 'a' ~ 'z'
                acc_dict[chr(c)][i + 1] = acc_dict[chr(c)][i]  # 이전 값 유지
            acc_dict[self.s[i]][i + 1] += 1  # 현재 문자를 증가

        for query in self.queries:
            c, s, e = query
            s, e = int(s), int(e)
            print(acc_dict[c][e + 1] - acc_dict[c][s])  # s ~ e 범위의 문자 개수 계산


problem = Main()
problem.solve()
class Main:
    def __init__(self):
        self.t = int(input())
        self.case = [input().zfill(4) for _ in range(self.t)]  # 4자리 보장
        self.answer = []
        self.cache = {}
        self.precompute()

    def kaprekar_steps(self, num_str):
        seen = set()
        cnt = 0
        while num_str != "6174":
            if num_str in self.cache:
                return cnt + self.cache[num_str]
            if num_str in seen:
                # infinite loop (only occurs if all digits same)
                return 0
            seen.add(num_str)
            max_num = "".join(sorted(num_str, reverse=True))
            min_num = "".join(sorted(num_str))
            num_str = str(int(max_num) - int(min_num)).zfill(4)
            cnt += 1
        return cnt

    def precompute(self):
        for i in range(10000):
            num_str = str(i).zfill(4)
            self.cache[num_str] = self.kaprekar_steps(num_str)

    def solve(self):
        for case in self.case:
            print(self.cache[case])

problem = Main()
problem.solve()

class Main:
    def __init__(self):
        self.data = [list(input().split()) for _ in range(5)]
        self.answer = []

    def solve(self):
        table = {
            0: ["###", "#.#", "#.#", "#.#", "###"],
            1: ["..#", "..#", "..#", "..#", "..#"],
            2: ["###", "..#", "###", "#..", "###"],
            3: ["###", "..#", "###", "..#", "###"],
            4: ["#.#", "#.#", "###", "..#", "..#"],
            5: ["###", "#..", "###", "..#", "###"],
            6: ["###", "#..", "###", "#.#", "###"],
            7: ["###", "..#", "..#", "..#", "..#"],
            8: ["###", "#.#", "###", "#.#", "###"],
            9: ["###", "#.#", "###", "..#", "###"]
        }

        nums = [[self.data[j][i] for j in range(5)] for i in range(4)]
        for num in nums:
            max_cnt = 0
            result = -1
            for i in table.items():
                cnt = 0
                target, code = i
                for row in range(5):
                    for col in range(3):
                        if num[row][col] == code[row][col] == "#":
                            cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
                    result = target

            self.answer.append(str(result))

        print(self.answer[0]+self.answer[1]+":"+self.answer[2]+self.answer[3])


problem = Main()
problem.solve()
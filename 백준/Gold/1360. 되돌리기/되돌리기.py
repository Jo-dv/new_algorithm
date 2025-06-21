class Main:
    def __init__(self):
        self.n = int(input())
        self.commands = [list(input().split()) for _ in range(self.n)]

    def preprocessing(self):
        for command in self.commands:
            if command[0] == "type":
                command[2] = int(command[2])
            else:
                command[1] = int(command[1])
                command[2] = int(command[2])

    def solve(self):
        self.preprocessing()
        valid = [True] * self.n

        for i in range(self.n-1, -1, -1):
            if not valid[i]:
                continue
            if self.commands[i][0] == "undo":
                _, duration, active_time = self.commands[i]
                for j in range(i-1, -1, -1):
                    if valid[j] and active_time - duration <= self.commands[j][2]:
                        valid[j] = False

        answer = ""
        for i in range(self.n):
            if valid[i] and self.commands[i][0] == "type":
                answer += self.commands[i][1]

        print(answer)


problem = Main()
problem.solve()
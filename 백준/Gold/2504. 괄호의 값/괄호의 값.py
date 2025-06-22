class Main:
    def __init__(self):
        self.string = list(input())
        self.answer = 0

    def solve(self):
        stack = []
        result = 1

        for i in range(len(self.string)):
            data = self.string[i]

            if data == "(":
                stack.append(data)
                result *= 2
            elif data == "[":
                stack.append(data)
                result *= 3
            elif data == ")":
                if not stack or stack[-1] == "[":
                    self.answer = 0
                    break
                if self.string[i-1] == "(":
                    self.answer += result
                result //= 2
                stack.pop()
            else:
                if not stack or stack[-1] == "(":
                    self.answer = 0
                    break
                if self.string[i-1] == "[":
                    self.answer += result
                result //= 3
                stack.pop()

        print(self.answer if not stack else 0)


problem = Main()
problem.solve()
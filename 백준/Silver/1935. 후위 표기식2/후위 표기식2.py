class Main:
    def __init__(self):
        self.n = int(input())
        self.expression = input()
        self.numbers = [int(input()) for _ in range(self.n)]

    def preprocess(self):
        number_table = {}
        i = 0
        for data in self.expression:
            if data.isalpha() and data not in number_table:
                number_table[data] = self.numbers[i]
                i += 1

        return number_table

    def solve(self):
        number_table = self.preprocess()
        stack = []
        for i in self.expression:
            if not i.isalpha():
                num2 = stack.pop()
                num1 = stack.pop()
                if i == "+":
                    stack.append(num1 + num2)
                elif i == "-":
                    stack.append(num1 - num2)
                elif i == "/":
                    stack.append(num1 / num2)
                else:
                    stack.append(num1 * num2)
            else:
                stack.append(number_table[i])

        print(f"{stack[-1]:.2f}")


problem = Main()
problem.solve()
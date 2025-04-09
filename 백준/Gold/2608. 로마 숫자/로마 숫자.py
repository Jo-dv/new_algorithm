class Main:
    def __init__(self):
        self.num1 = input().strip()
        self.num2 = input().strip()

    @staticmethod
    def transfer(dic, num):
        i = 0
        result = []

        while i < len(num) - 1:
            num1 = num[i]
            num2 = num[i:i + 2]
            if num1 in dic and num2 in dic:
                if dic[num2] > dic[num1]:  # 작은 값이 앞에 올 경우
                    result.append(dic[num2])
                    i += 2
                else:
                    result.append(dic[num1])
                    i += 1
            elif num1 in dic:
                result.append(dic[num1])
                i += 1
            elif num2 in dic:
                result.append(dic[num2])
                i += 2

        if i < len(num):
            result.append(dic[num[i]])
        return sum(result)

    @staticmethod
    def to_roman(num):
        roman_numerals = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        result = ""
        for value, symbol in roman_numerals:
            while num >= value:
                result += symbol
                num -= value
        return result

    def solve(self):
        dic = {
            "I": 1, "IV": 4, "V": 5, "IX": 9,
            "X": 10, "XL": 40, "L": 50, "XC": 90,
            "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000
        }

        # 로마 숫자를 아라비아 숫자로 변환
        result1 = self.transfer(dic, self.num1)
        result2 = self.transfer(dic, self.num2)

        # 두 수의 합
        total = result1 + result2

        # 아라비아 숫자를 로마 숫자로 변환
        roman_result = self.to_roman(total)

        # 결과 출력
        print(total)
        print(roman_result)


# 실행
problem = Main()
problem.solve()

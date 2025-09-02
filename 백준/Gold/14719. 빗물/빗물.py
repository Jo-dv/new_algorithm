class Main:
    def __init__(self):
        self.h, self.w = map(int, input().split())
        self.block = list(map(int, input().split()))
        self.idx = []  # stack
        self.answer = 0

    def solve(self):
        for i in range(self.w):
            while self.idx and self.block[self.idx[-1]] < self.block[i]:  # 최근 기록된 높이가 현재 높이보다 낮다면 계산 시작
                # 높이가 높아진 지점부터 시작해서 높이가 지금보다 낮은 부분들을 찾아 오른쪽에서 왼쪽으로 수평 계산 -> 물의 넓이
                previous_idx = self.idx.pop()

                if not self.idx:  # 기준 블록이 없어서 물을 담고 있을 수 없음
                    break

                distance = (i - 1) - self.idx[-1]  # 카운팅한 현재 자기 자신 제외(-1)
                min_height = min(self.block[self.idx[-1]], self.block[i])
                height = min_height - self.block[previous_idx]  
                # 가장 근소하게 높은 블록과의 차이만큼 계산 -> 근소하게 높은 블록이 그 아래의 블록들을 모두 채우기 때문
                # 무작정 높은 블록을 기준으로 계산하면 물이 찰 수 없는 영역에도 물이 차게 되므로 논리적으로 맞지 않게 됨

                self.answer += (distance * height)

            self.idx.append(i)

        print(self.answer)


problem = Main()
problem.solve()
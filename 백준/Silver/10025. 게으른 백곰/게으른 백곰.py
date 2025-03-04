import sys

class Main:
    def __init__(self):
        self.n, self.k = map(int, sys.stdin.readline().split())
        self.bottles = [list(map(int, sys.stdin.readline().split())) for _ in range(self.n)]
        self.answer = 0

    def solve(self):
        MAX_X = 1000000  # 최대 좌표값
        cage = [0] * (MAX_X + 1)  # 1차원 배열 생성 (초기화)

        # 얼음 정보를 해당 위치에 저장
        for g, x in self.bottles:
            cage[x] += g  # 같은 위치에 여러 개 있을 수 있으므로 +=

        # 초기 윈도우 설정 (0 ~ min(K, MAX_X))
        window_size = self.k * 2 + 1  # 왼쪽 K + 현재 위치 + 오른쪽 K
        ice = sum(cage[:min(window_size, MAX_X + 1)])  # 초기 윈도우 합

        self.answer = ice  # 초기 값 저장

        # 슬라이딩 윈도우 진행
        for i in range(window_size, MAX_X + 1):
            ice += cage[i]  # 오른쪽 값 추가
            ice -= cage[i - window_size]  # 왼쪽 값 제거
            self.answer = max(self.answer, ice)  # 최대값 갱신

        print(self.answer)


problem = Main()
problem.solve()

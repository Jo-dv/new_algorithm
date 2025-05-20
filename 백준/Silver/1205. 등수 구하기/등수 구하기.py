class Main:
    def __init__(self):
        self.n, self.new_score, self.p = map(int, input().split())
        self.score_board = list(map(int, input().split())) if self.n > 0 else []

    def solve(self):
        # 새 점수 추가
        self.score_board.append(self.new_score)
        self.score_board.sort(reverse=True)

        # 새 점수의 인덱스를 기준으로 등수 계산
        rank = 1
        for i in range(len(self.score_board)):
            if self.score_board[i] > self.new_score:
                rank += 1
            else:
                break

        # 리스트가 꽉 찼고, 새 점수가 끝자리보다 작거나 같으면 못 들어감
        if self.n == self.p and self.score_board[-1] >= self.new_score:
            print(-1)
        else:
            print(rank)

# 실행
problem = Main()
problem.solve()

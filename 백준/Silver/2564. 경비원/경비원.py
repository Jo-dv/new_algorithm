import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.w, self.h = map(int, input().split())  # 가로, 세로 크기
        self.n = int(input())  # 상점 개수
        self.stores = [tuple(map(int, input().split())) for _ in range(self.n)]  # 상점 위치
        self.guard = tuple(map(int, input().split()))  # 동근이 위치

    def convert_to_1d(self, direction, pos):
        if direction == 1:  # 북쪽 (0 ~ w)
            return pos
        elif direction == 2:  # 남쪽 (w+h ~ 2w+h)
            return self.w + self.h + (self.w - pos)
        elif direction == 3:  # 서쪽 (2w+h ~ 2w+2h)
            return 2 * self.w + self.h + (self.h - pos)
        else:  # 동쪽 (w ~ w+h)
            return self.w + pos

    def solve(self):
        total_distance = 0
        total_perimeter = 2 * (self.w + self.h)

        guard_pos = self.convert_to_1d(*self.guard)

        for store in self.stores:
            store_pos = self.convert_to_1d(*store)

            dist = min(abs(guard_pos - store_pos), total_perimeter - abs(guard_pos - store_pos))
            total_distance += dist

        print(total_distance)


problem = Main()
problem.solve()

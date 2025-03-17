from collections import deque

class Main:
    def __init__(self):
        self.n = int(input())
        self.k = int(input())
        self.apples = [tuple(map(int, input().split())) for _ in range(self.k)]
        self.l = int(input())
        self.cmd = [input().split() for _ in range(self.l)]

    def init_grid(self):
        grid = [[0] * self.n for _ in range(self.n)]
        for y, x in self.apples:
            grid[y - 1][x - 1] = 1  # 1은 사과
        return grid

    @staticmethod
    def turn(current_direction, direction):
        return (current_direction + 1) % 4 if direction == 'L' else (current_direction + 3) % 4

    def move_snake(self, y, x, direction, snake, grid):
        """뱀을 한 칸 이동시키고 종료 조건 체크"""
        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        my, mx = y + directions[direction][0], x + directions[direction][1]

        # 경계 체크 및 자기 자신과 충돌 체크
        if not (0 <= my < self.n and 0 <= mx < self.n) or (my, mx) in snake:
            return None, None  # 게임 종료 조건 충족

        # 사과가 있을 경우 사과를 먹고 길이 증가
        if grid[my][mx] == 1:
            grid[my][mx] = 0
        else:  # 사과가 없으면 꼬리 제거
            snake.popleft()

        # 머리 이동
        snake.append((my, mx))
        return my, mx

    def run(self):
        grid = self.init_grid()  # 맵 생성
        y, x = 0, 0  # 초기 뱀의 위치
        snake = deque([(0, 0)])  # 초기 뱀
        current_direction = 0  # 초기 뱀의 방향
        time = 0  # 정답

        for end_time, direction in self.cmd:
            while time < int(end_time):  # 방향 전환 시간 포함
                time += 1  # 뱀이 움직이기 시작한 시간
                y, x = self.move_snake(y, x, current_direction, snake, grid)
                if y is None:  # 게임 종료 조건이 충족됐을 때
                    return time  # 게임 종료

            current_direction = self.turn(current_direction, direction)  # 방향 전환

        while True:  # 아직 게임이 종료되지 않았다면
            time += 1
            y, x = self.move_snake(y, x, current_direction, snake, grid)
            if y is None:
                return time

    def solve(self):
        print(self.run())


problem = Main()
problem.solve()
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

class Main:
    def __init__(self):
        self.m, self.n, self.p = map(int, input().split())
        self.grid = [list(input()) for _ in range(self.m)]
        self.players = [input().split() for _ in range(self.p)]
        self.boss_hp = int(input())
        self.boss = None

    def find_boss(self):
        for y in range(self.m):
            for x in range(self.n):
                if self.grid[y][x] == "B":
                    return y, x

    def boss_bfs(self):
        visited = [[-1] * self.n for _ in range(self.m)]
        dq = deque()
        y, x = self.boss
        dq.append((y, x, 0))
        visited[y][x] = 0

        # 각 플레이어의 최소 도착 시간
        player_arrival = dict()

        while dq:
            cy, cx, time = dq.popleft()

            for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < self.m and 0 <= nx < self.n:
                    if self.grid[ny][nx] != "X" and visited[ny][nx] == -1:
                        visited[ny][nx] = time + 1
                        dq.append((ny, nx, time + 1))

                        if self.grid[ny][nx].islower():
                            player = self.grid[ny][nx]
                            player_arrival[player] = time + 1

        return [(player_id, player_arrival[player_id]) for player_id, _ in self.players if player_id in player_arrival]

    def attack(self, players_arrival):
        dps_table = {player: int(dps) for player, dps in self.players}
        players_arrival.sort(key=lambda x: x[1])

        cur_time = 0
        hp = self.boss_hp
        total_dps = 0
        idx = 0
        active_players = set()

        while True:
            while idx < len(players_arrival) and players_arrival[idx][1] == cur_time:
                player_id = players_arrival[idx][0]
                active_players.add(player_id)
                total_dps += dps_table[player_id]
                idx += 1

            if idx < len(players_arrival):
                next_time = players_arrival[idx][1]
            else:
                next_time = float('inf')

            time_interval = next_time - cur_time
            damage = time_interval * total_dps

            if damage >= hp:
                return len(active_players)
            else:
                hp -= damage
                cur_time = next_time

    def solve(self):
        self.boss = self.find_boss()
        players_arrival = self.boss_bfs()
        answer = self.attack(players_arrival)
        print(answer)

problem = Main()
problem.solve()

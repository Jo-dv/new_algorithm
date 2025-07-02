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

    def find_player(self):
        result = []
        for y in range(self.m):
            for x in range(self.n):
                if self.grid[y][x].islower():
                    result.append((self.grid[y][x], y, x))
        return result

    def move(self, info):
        visited = [[False] * self.n for _ in range(self.m)]
        player, y, x = info
        visited[y][x] = True
        dq = deque([(y, x, 0)])
        while dq:
            cy, cx, time = dq.popleft()
            if (cy, cx) == self.boss:
                return player, time
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                my, mx = cy + dy, cx + dx
                if 0 <= my < self.m and 0 <= mx < self.n and not visited[my][mx] and self.grid[my][mx] != "X":
                    dq.append((my, mx, time+1))
                    visited[my][mx] = True

    def attack(self, players_arrival):
        dps_table = {player: int(dps) for player, dps in self.players}
        players_arrival.sort(key=lambda x: x[1])

        cur_time = 0
        hp = self.boss_hp
        total_dps = 0
        idx = 0
        active_players = set()

        while True:
            # 플레이어들이 현재 시간에 도착 -> 참여 인원과 dps 증가
            while idx < len(players_arrival) and players_arrival[idx][1] == cur_time:
                player_id = players_arrival[idx][0]
                active_players.add(player_id)
                total_dps += dps_table[player_id]
                idx += 1

            # 다음 이벤트(다음 플레이어 도착) 시각
            if idx < len(players_arrival):
                next_time = players_arrival[idx][1]
            else:
                next_time = float('inf')

            # 이번 구간에서 줄어드는 hp 계산
            time_interval = next_time - cur_time
            damage = time_interval * total_dps

            if damage >= hp:
                return len(active_players)
            else:
                hp -= damage
                cur_time = next_time

    def solve(self):
        self.boss = self.find_boss()
        players_pos = self.find_player()
        players_arrival = []
        for player in players_pos:
            players_arrival.append(self.move(player))

        answer = self.attack(players_arrival)
        print(answer)


problem = Main()
problem.solve()

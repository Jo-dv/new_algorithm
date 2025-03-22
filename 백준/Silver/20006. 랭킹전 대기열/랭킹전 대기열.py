class Main:
    def __init__(self):
        self.p, self.m = map(int, input().split())
        self.players = [tuple(input().split()) for _ in range(self.p)]  # l, n = 레벨, 닉네임
        self.game_room = dict()
        self.room_info = dict()
        self.idx = 0

    def create_room(self, player):
        level, name = player
        level = int(level)
        self.game_room[self.idx] = [player]
        self.room_info[self.idx] = (level - 10, level + 10)
        self.idx += 1

    def solve(self):
        for player in self.players:
            if not self.game_room:
                self.create_room(player)
            else:
                for i in range(self.idx):
                    if len(self.game_room[i]) == self.m:
                        continue
                    if self.room_info[i][0] <= int(player[0]) <= self.room_info[i][1]:
                        self.game_room[i].append(player)
                        break
                else:  # 방을 찾지 못한 플레이어
                    self.create_room(player)

        for room in self.game_room.values():
            room.sort(key=lambda x: x[1])
            print("Started!" if len(room) == self.m else "Waiting!")
            for player in room:
                print(*player)


problem = Main()
problem.solve()

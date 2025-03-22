from collections import defaultdict


class Main:
    def __init__(self):
        self.p, self.m = map(int, input().split())
        self.players = [tuple(input().split()) for _ in range(self.p)]  # l, n = 레벨, 닉네임

    def solve(self):
        game_room = dict()
        room_info = dict()
        idx = 0
        for player in self.players:
            level, name = player
            level = int(level)
            if not game_room:
                game_room[idx] = [player]
                room_info[idx] = (level - 10, level + 10)
                idx += 1
            else:
                for i in range(idx):
                    if len(game_room[i]) == self.m:
                        continue
                    if room_info[i][0] <= level <= room_info[i][1]:
                        game_room[i].append(player)
                        break
                else:
                    game_room[idx] = [player]
                    room_info[idx] = (level - 10, level + 10)
                    idx += 1

        for room in game_room.values():
            room.sort(key=lambda x: x[1])
            print("Started!" if len(room) == self.m else "Waiting!")
            for player in room:
                print(*player)


problem = Main()
problem.solve()

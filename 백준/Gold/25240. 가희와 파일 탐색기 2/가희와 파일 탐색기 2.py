from collections import defaultdict
import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.u, self.f = map(int, input().split())
        self.users = [input() for _ in range(self.u)]
        self.files = [input() for _ in range(self.f)]
        self.q = int(input())
        self.queries = [input() for _ in range(self.q)]
        self.answer = []

    def solve(self):
        group_info = defaultdict(set)
        file_info = defaultdict(list)
        file_permission = dict()
        operator = {"R": 4, "W": 2, "X": 1}

        for info in self.users:
            user = info.split()
            name = user[0]
            group_info[name].add(name)  # 유저는 기본적으로 자기 이름과 동일한 그룹에 속함
            if len(user) > 1:
                group = user[1].split(",")
                for i in group:
                    group_info[name].add(i)

        for info in self.files:
            file = info.split()
            name, permission, owner, group = file
            file_info[name].append(owner)
            file_info[name].append(group)
            file_permission[name] = list(map(int, permission))

        for query in self.queries:
            user, file, operation = query.split()
            if file_info[file][0] == user:
                self.answer.append(1 if file_permission[file][0] & operator[operation] != 0 else 0)
            elif file_info[file][1] in group_info[user]:
                self.answer.append(1 if file_permission[file][1] & operator[operation] != 0 else 0)
            else:
                self.answer.append(1 if file_permission[file][2] & operator[operation] != 0 else 0)

        for i in self.answer:
            print(i)


problem = Main()
problem.solve()

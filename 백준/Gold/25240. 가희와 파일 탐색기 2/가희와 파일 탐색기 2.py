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

    def solve(self):
        group_info = defaultdict(set)
        file_info = dict()
        operator = {"R": 4, "W": 2, "X": 1}

        # 유저 정보
        for info in self.users:
            parts = info.split()
            name = parts[0]
            group_info[name].add(name)  # 자기 이름 그룹 자동 포함
            if len(parts) > 1:
                for g in parts[1].split(","):
                    group_info[name].add(g)

        # 파일 정보
        for info in self.files:
            name, permission, owner, group = info.split()
            perm_list = list(map(int, permission))
            file_info[name] = {
                "owner": owner,
                "group": group,
                "perm": perm_list
            }

        # 쿼리 처리
        result = []
        for query in self.queries:
            user, file, operation = query.split()
            owner = file_info[file]["owner"]
            group = file_info[file]["group"]
            perm = file_info[file]["perm"]
            op_bit = operator[operation]

            if user == owner:
                level = 0  # OWNER
            elif group in group_info[user]:
                level = 1  # GROUP
            else:
                level = 2  # OTHER

            result.append("1" if perm[level] & op_bit else "0")

        print("\n".join(result))


problem = Main()
problem.solve()

from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()


class Main:
    def __init__(self):
        self.n, self.t, self.w = map(int, input().split())
        self.customer1 = [list(map(int, input().split())) for _ in range(self.n)]
        self.m = int(input())
        self.customer2 = [list(map(int, input().split())) for _ in range(self.m)]
        self.answer = []

    def solve(self):
        waiting_queue = deque(self.customer1)
        current_time = 0
        idx = 0
        self.customer2.sort(key=lambda x: x[2])

        while current_time < self.w:
            if not waiting_queue:
                break

            px, tx = waiting_queue.popleft()
            
            process_time = min(tx, self.t)  # 처리할 수 있는 최대 시간 (tx와 T 중 작은 값)

            for _ in range(process_time):
                if current_time >= self.w:
                    break  # 업무 시간이 W를 넘어가면 종료
                self.answer.append(px)
                current_time += 1

                # 현재 시간에 맞는 새로운 고객 추가
                while idx < self.m and self.customer2[idx][2] == current_time:
                    waiting_queue.append(self.customer2[idx][:2])  # id, 업무시간만 추가
                    idx += 1

            # 업무가 끝나지 않았다면 다시 대기열에 추가
            tx -= process_time
            if tx > 0:
                waiting_queue.append([px, tx])

        for i in self.answer:
            print(i)


problem = Main()
problem.solve()

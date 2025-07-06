class Node:
    def __init__(self, val=None, nxt=None, prev=None):
        self.val = val
        self.nxt = nxt
        self.prev = prev


class Main:
    def __init__(self):
        self.tc = int(input())
        self.testcases = [list(input()) for _ in range(self.tc)]
        self.answer = []

    def solve(self):
        for testcase in self.testcases:
            linked_list = Node()
            head = linked_list
            cur = linked_list
            result = []

            for i in testcase:
                if i == "<":
                    if cur.prev is not None:
                        cur = cur.prev
                elif i == ">":
                    if cur.nxt is not None:
                        cur = cur.nxt
                elif i == "-":
                    if cur.prev is not None:
                        if cur.nxt is None:
                            cur.prev.nxt = None
                        else:
                            cur.prev.nxt = cur.nxt
                            cur.nxt.prev = cur.prev
                        cur = cur.prev
                else:
                    new_node = Node(i)
                    if cur.nxt is None:
                        cur.nxt = new_node
                        new_node.prev = cur
                    else:
                        cur.nxt.prev = new_node
                        new_node.nxt = cur.nxt
                        new_node.prev = cur
                        cur.nxt = new_node
                    cur = new_node

            cur = head
            while cur.nxt is not None:
                cur = cur.nxt
                result.append(cur.val)

            self.answer.append("".join(result))

        for i in self.answer:
            print(i)


problem = Main()
problem.solve()
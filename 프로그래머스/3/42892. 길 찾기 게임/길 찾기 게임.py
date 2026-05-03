import sys
sys.setrecursionlimit(10**5)

class Node:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num
        self.left = None
        self.right = None
        
def create(cur, new_x, new_y, num):
    new_Node = Node(new_x, new_y, num)
    if new_Node.y < cur.y:
        if new_Node.x < cur.x:
            if cur.left is None:
                cur.left = new_Node
            else:
                create(cur.left, new_x, new_y, num)
        elif new_Node.x > cur.x:
            if cur.right is None:
                cur.right = new_Node
            else:
                create(cur.right, new_x, new_y, num)
                
def preorder(node, result):
    if node is None:
        return result
    result.append(node.num)
    preorder(node.left, result)
    preorder(node.right, result)
    
    return result

def postorder(node, result):
    if node is None:
        return result
    
    postorder(node.left, result)
    postorder(node.right, result)
    result.append(node.num)
    
    return result

def solution(nodeinfo):
    answer = []
    
    nodeinfo = [(i[0], i[1], num) for num, i in enumerate(nodeinfo, 1)]
    nodeinfo.sort(key=lambda i: (-i[1], i[0]))
    root = Node(nodeinfo[0][0], nodeinfo[0][1], nodeinfo[0][2])

    for i in range(1, len(nodeinfo)):
        x, y, num = nodeinfo[i]
        create(root, x, y, num)
    
    answer.append(preorder(root, []))
    answer.append(postorder(root, []))

    return answer
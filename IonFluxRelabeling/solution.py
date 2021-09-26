class Node:
    def __init__(self, values, p, n):
        self.parent = p
        self.value = values[-1]
        self.children = []
        
        n[self.value] = self
        if len(values) > 1:
            if not values[(len(values)-1)//2-1] in n:
                self.children.append(Node(values[0:len(values)//2], self, n))
            if not values[-2] in n:
                self.children.append(Node(values[(len(values)-1)//2:-1], self, n))

def solution(h, q):
    m = max(q)
    root = 2 ** (len(bin(m)[2:]) if len(bin(m)[2:]) < 2 ** h - 1 else 2 ** h - 1)
    print(root)

    nodes = {}
    Node(list(range(1, root)), None, nodes)

    p = []
    for i in q:
        p.append(nodes[i].parent.value if not nodes[i].parent is None else -1)

    return p

print(solution(3, [7, 3, 5, 1]))

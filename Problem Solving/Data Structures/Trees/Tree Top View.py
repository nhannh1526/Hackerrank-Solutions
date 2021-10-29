class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def topView(root):
    # Write your code here
    if root:
        q = []  # Queue
        m = dict()  # Horizontal distance dictionary
        hd = 0  # Horizontal distance
        root.hd = hd

        q.append(root)

        while (len(q)):
            root = q[0]
            hd = root.hd

            if hd not in m:
                m[hd] = root.info
            if root.left:
                root.left.hd = hd - 1
                q.append(root.left)
            if root.right:
                root.right.hd = hd + 1
                q.append(root.right)
            q.pop(0)

        for key in sorted(m):
            print(m[key], end=' ')


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)

class Node:
    def __init__(self,val):
        self.value = val
        self.children = []
root = Node(1)
root.children.append(Node(2))
root.children.append(Node(3))
root.children[0].children.append(Node(4))
root.children[0].children.append(Node(5))
root.children[1].children.append(Node(6))
root.children[1].children.append(Node(7))

def dfs(node):
    print(node.value)
    for child in node.children:
        dfs(child)
dfs(root)

def bfs(node):
    queue = [node]
    while queue:
        current = queue.pop(0)
        print(current.value)
        for child in current.children:
            queue.append(child)
bfs(root)

def bfs_search(node, target):
    queue = [node]
    while queue:
        current = queue.pop(0)
        if current.value == target:
            return True
        for child in current.children:
            queue.append(child)
    return False
print(bfs_search(root, 7))

def dfs_search(node, target):
    if node.value == target:
        return True
    for child in node.children:
        if dfs_search(child, target):
            return True
    return False

print(dfs_search(root, 7))

def best_first_search(node, target):
    queue = [node]
    while queue:
        current = queue.pop(0)
        if current.value == target:
            return True
        current.children.sort(key=lambda x: x.value)
        for child in current.children:
            queue.append(child)
    return False
print(best_first_search(root, 7))
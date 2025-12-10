import uuid
from collections import deque

import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            left_x = x - 1 / 2 ** layer
            pos[node.left.id] = (left_x, y - 1)
            add_edges(graph, node.left, pos, x=left_x, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            right_x = x + 1 / 2 ** layer
            pos[node.right.id] = (right_x, y - 1)
            add_edges(graph, node.right, pos, x=right_x, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root: Node, title: str):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors,
    )
    plt.title(title)
    plt.show()


def generate_gradient_hex(
    n: int,
    start=(18, 50, 120),
    end=(190, 230, 255),
):
    if n <= 1:
        r, g, b = start
        return [f"#{r:02X}{g:02X}{b:02X}"]

    colors = []
    for i in range(n):
        t = i / (n - 1)
        r = int(start[0] + t * (end[0] - start[0]))
        g = int(start[1] + t * (end[1] - start[1]))
        b = int(start[2] + t * (end[2] - start[2]))
        colors.append(f"#{r:02X}{g:02X}{b:02X}")
    return colors


def dfs_order(root: Node):
    order = []
    stack = [root]
    visited = set()

    while stack:
        node = stack.pop()
        if node is None or node.id in visited:
            continue
        visited.add(node.id)
        order.append(node)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order


def bfs_order(root: Node):
    order = []
    queue = deque([root])
    visited = set()

    while queue:
        node = queue.popleft()
        if node is None or node.id in visited:
            continue
        visited.add(node.id)
        order.append(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order


def color_by_order(root: Node, order_func):
    order = order_func(root)
    palette = generate_gradient_hex(len(order))
    for node, color in zip(order, palette):
        node.color = color
    return order


def build_sample_tree() -> Node:
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    root.right.right = Node(7)
    return root


if __name__ == "__main__":
    tree_root = build_sample_tree()

    dfs_seq = color_by_order(tree_root, dfs_order)
    print("DFS порядок обходу:", [n.val for n in dfs_seq])
    draw_tree(tree_root, "DFS обхід (стек)")

    tree_root = build_sample_tree()
    bfs_seq = color_by_order(tree_root, bfs_order)
    print("BFS порядок обходу:", [n.val for n in bfs_seq])
    draw_tree(tree_root, "BFS обхід (черга)")
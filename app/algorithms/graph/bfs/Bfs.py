from collections import deque

class BFS:
    @staticmethod
    def node_exist(root, node):
        bfs_deque = deque()
        if root:
            bfs_deque.append(root)
        while(bfs_deque):
            current_node = bfs_deque.popleft()
            if current_node is node:
                return True
            for item in current_node.children:
                bfs_deque.append(item)
        return False
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors: Optional[List[Node]] = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        """
        Using DFS to traverse through the graph and copy the nodes
        Use a hash map to keep track of visited node
            Runtime Complexity: O(n) since we visit each node in the graph once
                The time to find if a node is already cloned using the hash map is O(1)
            Space Complexity: O(n)
                To store the cloned hashmap (each node is one entry) and
                the recursion stack (worst case linear graph)
        """
        cloned = {}

        if not node:  # edge case: empty graph
            return None

        def dfs(current_node: Node) -> Optional[Node]:
            if current_node is None:
                return

            if current_node in cloned:
                # if the current node is already cloned, return the cloned node
                return cloned[current_node]

            # clone the current node and mark it as visited
            cloned_node = Node(val=current_node.val, neighbors=[])
            cloned[current_node] = cloned_node

            # visit and clone the neighboring nodes
            for neighbor in current_node.neighbors:
                cloned_node.neighbors.append(dfs(neighbor))

            return cloned_node

        dfs(node)

        return list(cloned.values())[0]

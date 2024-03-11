class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def sum_of_depths(root, depth = 0) -> int:
    if root is None:
        return 0
    else:
         l_depth = sum_of_depths(root.left, depth + 1)
         r_depth = sum_of_depths(root.right, depth + 1)

    return depth + l_depth + r_depth



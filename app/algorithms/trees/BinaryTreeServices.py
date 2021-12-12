from collections import deque

def lowest_common_ancestor_iterative(root, node, node2):
    parents_dict = node_parents(root)
    validate_common_ancestor_nodes_exist_iterativly(parents_dict, node, node2)
    back_track_set = set()
    
    find_node = None
    while node:
        back_track_set.add(node)
        node = parents_dict[node]
    while node2:
        if node2 in back_track_set:
            find_node = node2
            break
        node2 = parents_dict[node2]
    return find_node

def node_parents(root):
    result = {root: None}
    items = deque()
    items.append(root)
    while items:
        item = items.pop()
        if item.right:
            result[item.right] = item
            items.append(item.right)
        if item.left:
            result[item.left] = item
            items.append(item.left)
    return result
        
def pre_order_node_exists(root, node):
    if root is None:
        return False
    if root is node:
        return True
    left = pre_order_node_exists(root.left, node)
    right = pre_order_node_exists(root.right, node)
    if left is True or right is True:
        return True
    return False
    
def lowest_common_ancestor_recursive(root, node, node2):
    validate_common_ancestor_nodes_exist_recursivly(root, node, node2)
    return _lowest_common_ancestor_recursive_helper(root, node, node2)

def _lowest_common_ancestor_recursive_helper(root, node, node2):
    if root is None:
        return None
    if root is node or root is node2:
        return root
    left = _lowest_common_ancestor_recursive_helper(root.left, node, node2)
    right = _lowest_common_ancestor_recursive_helper(root.right, node, node2)
    if left and right:
        return root
    return left if right is None else right

def validate_common_ancestor_nodes_exist_recursivly(root, node, node2):
    node_exists = pre_order_node_exists(root, node)
    node2_exists = pre_order_node_exists(root, node2)
    if not node_exists and not node2_exists:
        raise Exception("Could not find nodes {} {} in tree {}".format(vars(node), vars(node2)))
    node_check = node if not node_exists else node2 if not node2_exists else None
    if node_check:
        raise Exception("Could not find node {} in tree {}".format(vars(node_check)))

def validate_common_ancestor_nodes_exist_iterativly(parents, node, node2):
    if node not in parents and node2 not in parents:
        raise Exception("Could not find nodes {} {} in tree {}".format(vars(node), vars(node2)))
    node_check = node if node not in parents else node2 if node2 not in parents else None
    if node_check:
        raise Exception("Could not find node {} in tree {}".format(vars(node)))
    
def is_leaf_node(node):
    if node is None:
        return False
    return node.left is None and node.right is None

def is_half_lead_node(node):
    if node is None:
        return False
    return node.left is None or node.right is None

def calculate_node_height(root):
    if root is None:
        return -1
    left = calculate_node_height(root.left)
    right = calculate_node_height(root.right)
    if root.left is None and root.right is None:
        return 0
    current_count = max(left, right)
    if current_count != -1:
        return max(left, right) + 1
    return max(left,right)

def calculate_node_depth(root, node):
    if root is None:
        return -1
    if root is node:
        return 0
    left = calculate_node_depth(root.left, node)
    right = calculate_node_depth(root.right, node)
    if left != -1 or right != -1:
        return max(left, right) + 1
    return max(left, right)

def calculate_depth(root):
    if root is None:
        return -1
    left = calculate_depth(root.left)
    right = calculate_depth(root.right)
    return max(left, right) + 1
    

def find_first_half_leaf_node_recursivly(root):
    if root is None:
        return None
    find_first_half_leaf_node_recursivly(root.left)
    find_first_half_leaf_node_recursivly(root.right)
    if root and (root.left is None and root.right is not None) or (root.left is not None and root.right is None):
        return root
    return None

def find_first_leaf_node_recursivly(root):
    if root is None:
        return None
    find_first_leaf_node_recursivly(root.left)
    find_first_leaf_node_recursivly(root.right)
    if root and root.left is None and root.right is None:
        return root
    return None


def is_balanced_binary_tree_helper(root):
    if root is None:
        return 0
    left = is_balanced_binary_tree_helper(root.left)
    right = is_balanced_binary_tree_helper(root.right)
    if left == -1 or right == -1:
        return -1
    if abs(left - right) > 1:
        return -1
    return max(left, right) + 1
    
def is_balanced_binary_tree_recursive(root):
    return is_balanced_binary_tree_helper(root) != -1

def post_order_traverse(root):
    if(root is None):
        return []
    return post_order_traverse(root.left) + post_order_traverse(root.right) + [root.val]

def pre_order_traverse(root):
    if(root is None):
        return []
    return [root.val] + pre_order_traverse(root.left) + pre_order_traverse(root.right)

def in_order_traverse(root):
    if(root is None):
        return []
    return in_order_traverse(root.left) + [root.val] + in_order_traverse(root.right)

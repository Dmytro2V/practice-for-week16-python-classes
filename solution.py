# Write your class here.

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class Tree:
    def insert(self, current_node, new_node):
        if not current_node:
            return new_node
        
        if current_node.value == new_node.value:
            return
        
        else:
            if current_node.value < new_node.value:
                current_node.right = self.insert(current_node.right, new_node)
            
            else:
                current_node.left = self.insert(current_node.left, new_node)

            return current_node 



    def preorder_traversal(self, node):
        if node:
            print(node.value)
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value)
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value)

tree = Tree()
print (' 1. we have an empty tree', tree)

root = Node(4)
tree.insert(root, Node(1))
tree.insert(root, Node(2))
tree.insert(root, Node(3))

# print("** PRE ORDER: **")
# tree.preorder_traversal(root) # 4, 1, 2, 3

# print("** IN ORDER: **")
# tree.inorder_traversal(root) # 1, 2, 3, 4

# print("** POST ORDER: **")
# tree.postorder_traversal(root) # 3, 2, 1, 4
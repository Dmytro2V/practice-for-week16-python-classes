# Tree Traversal - Challenge

# In this practice, you will use classes to implement a binary search tree and perform pre-order, in-order, and post-order traversal of the tree.

# Implement a class Node with a constructor method that defines the following instance properties:


# The lefthand child of the node, initialized to None
# The righthand child of the node, initialized to None
# The value of the node, initialized to the value passed into the constructor


# Implement another class Tree with the following instance methods:

# insert() that takes in the root node and a new node and places the new node in the correct location in the binary search tree
# preorder_traversal() that traverses the tree and prints the value of each node in pre-order succession
# inorder_traversal() that traverses the tree and prints the value of each node in in-order succession
# postorder_traversal() that traverses the tree and prints the value of each node in post-order succession

# Write your class here.

class Node:
  def __init__(self, val):
    self.left = 0
    self.right = 0
    self.val = val 
    


class Tree:
  def __init__(self, root_node = {}):
    self.root=root_node
  
  def insert(self, current_node, new_node):
    if  not current_node: 
      return new_node
    if  new_node.val < current_node.val: # go left
      current_node.left = self.insert(current_node.left, new_node) 
    if  new_node.val >= current_node.val: # go right
      current_node.right = self.insert(current_node.right, new_node) 
  
  def __repr__(self):
        return f"<Tree val: {self.root.val}, left: {self.root_left}, right: {self.root_right})>"

tree = Tree()

root = Node(4)
tree.insert(root, Node(1))
tree.insert(root, Node(2))
tree.insert(root, Node(3))
print(tree)

print("** PRE ORDER: **")
tree.preorder_traversal(root) # 4, 1, 2, 3

print("** IN ORDER: **")
tree.inorder_traversal(root) # 1, 2, 3, 4

print("** POST ORDER: **")
tree.postorder_traversal(root) # 3, 2, 1, 4
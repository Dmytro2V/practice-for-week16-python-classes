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
    self.left = None
    self.right = None
    self.val = val 
  def __repr__(self):
    if not self:
      return {}
    return f"<Node: {self.val},{self.left},{self.right}>"


class Tree:  
  def insert(self, current_node, new_node):
    print('--', current_node, new_node)
    if  not current_node:
      return new_node
      print ('setted curr to new', current_node, new_node)
      return
   
    if  new_node.val < current_node.val: # go left      
      current_node.left = self.insert(current_node.left, new_node) 
    if  new_node.val >= current_node.val: # go right
      current_node.right = self.insert(current_node.right, new_node) 

      return current_node

  def preorder_traversal(self, node):
      if node:
          print(node.val)
          self.preorder_traversal(node.left)
          self.preorder_traversal(node.right)

  def inorder_traversal(self, node):
      if node:
          self.inorder_traversal(node.left)
          print(node.val)
          self.inorder_traversal(node.right)

  def postorder_traversal(self, node):
      if node:
          self.postorder_traversal(node.left)
          self.postorder_traversal(node.right)
          print(node.val)



tree = Tree()

root = Node(4)
tree.insert(root, Node(1))
tree.insert(root, Node(2))
tree.insert(root, Node(3))
print(root.val, root.left, root.right)

print("** PRE ORDER: **")
tree.preorder_traversal(root) # 4, 1, 2, 3

print("** IN ORDER: **")
tree.inorder_traversal(root) # 1, 2, 3, 4

print("** POST ORDER: **")
tree.postorder_traversal(root) # 3, 2, 1, 4
# A FloatRedBlackTree is one of
# None, or
# Node(color, RedBlackTree, float, RedBlackTree)
class Node:
    def __init__(self, color, left, val, right):
        self.color = color
        self.left = left
        self.val = val
        self.right = right

    def __eq__(self, other):
        return ((type(other) == Node)
          and self.color == other.color
          and self.left == other.left
          and self.val == other.val
          and self.right == other.right
        )

    def __repr__(self):
        return ("Node({!r}, {!r}, {!r}, {!r})".format(self.color, self.left, self.val, self.right))

# a color is one of
# - "R"
# - "B"

# RedBlackTree val -> RedblackTree
# Insert the value into the tree
def insert(t, v):
    n = insert2(t, v)
    return Node("B", n.left, n.val, n.right)

# RedBlackTree val -> RedBlackTree
# Insert the value into the tree
def insert2(t, v):
  if t == None:
    return Node("R", None, v, None)
  else:
    if v < t.val:
      return rebalance(Node(t.color, insert2(t.left, v), t.val, t.right))
    else:
      return rebalance(Node(t.color, t.left, t.val, insert2(t.right, v)))

# Node val -> Node
# rebalance a tree with a chain of two red nodes below a black root
def rebalance(t):
  if (t.color == "B" and t.left != None and t.left.color == "R"
      and t.left.left != None and t.left.left.color == "R"):
    return Node("R", Node("B", t.left.left.left, t.left.left.val, t.left.left.right),
                t.left.val,
                Node("B", t.left.right, t.val, t.right))
  elif (t.color == "B" and t.left != None and t.left.color == "R"
      and t.left.right != None and t.left.left.right == "R"):
    return Node("R", Node("B", t.left.left, t.left.val, t.left.right.left),
                t.left.right.val,
                Node("B", t.left.right.right, t.val, t.right))
  # ... (2 more clauses like this)
  else:
    return t

rb = None
rb= insert(rb, 40)
print(rb)
rb= insert(rb, 30)
print(rb)
rb= insert(rb, 20)
print(rb)
rb= insert(rb, 10)
print(rb)

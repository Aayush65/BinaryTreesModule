# This class is used to declare a Binary Tree
class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# This function prints Binary Tree nodes as their values
def nodePrint(lst: list) -> None:
    valList = []
    for i in lst:
        valList.append(i.val)
    print(valList)

# This function returns the maximum depth of the binary tree
def maxDepth(root: TreeNode) -> int:
    depth = 0
    if root:
        depth = 1 + max(maxDepth(root.left), maxDepth(root.right))
    return depth

# This function returns a list containing all the nodes of the binary tree in order of inorder traversal
def inorderTraversal(root: TreeNode) -> list[TreeNode]:
    iot = []
    if root:
        if root.left:
            iot += inorderTraversal(root.left)
        iot.append(root)
        if root.right:
            iot += inorderTraversal(root.right)
    return iot

# This function returns a list containing all the nodes of the binary tree in order of preorder traversal
def preorderTraversal(root: TreeNode) -> list[TreeNode]:
    pot = [root]
    if root.left:
        pot += preorderTraversal(root.left)
    if root.right:
        pot += preorderTraversal(root.right)
    return pot    


# This function returns a list containing all the nodes of the binary tree in order of postorder traversal
def postorderTraversal(root: TreeNode) -> list[TreeNode]:
    pot = []
    if root.left:
        pot += postorderTraversal(root.left)
    if root.right:
        pot += postorderTraversal(root.right)
    pot.append(root)
    return pot

# This function returns a list containing all the nodes of the binary tree in level order traversal (bfs)
def bfsTraversal(root: TreeNode) -> list[TreeNode]:
    bfs = []
    stack = [root] if root and root.val !=None else []
    while stack:
        temp_stack = []
        # bfs.append(stack)
        for curr in stack:
            if curr.left: temp_stack.append(curr.left)
            if curr.right: temp_stack.append(curr.right)
            bfs.append(curr)
        stack = temp_stack
    return bfs

# This function returns the root of the tree constructed from the values in the bfs (level order traversal) array
def bfsToTreeNode(bfs: list[str]) -> TreeNode:
    if not bfs or bfs[0] == None:
        return None
    root = TreeNode(bfs[0])
    lastNodes = [root]
    start = 1
    while start < len(bfs) and lastNodes:
        tempNodes = []
        for i in range(start,min(start + len(lastNodes)*2,len(bfs))):
            curr = lastNodes[int((i-start)//2)]
            if bfs[i] == None:
                continue
            node = TreeNode(bfs[i])
            if i % 2:
                curr.left = node
            else:
                curr.right = node
            tempNodes.append(node)
        start += len(lastNodes)*2
        lastNodes = tempNodes
    return root

# This function returns if both the passed Binary trees are congruent (even if node addresses are not the same)
def isSameTree(root1: TreeNode, root2: TreeNode) -> bool:
    res = True
    if not root1 and not root2:
        return res
    if (root1 and not root2) or (not root1 and root2):
        return False
    if root1.val == root2.val:
        if root1.left or root2.left:
            res &= isSameTree(root1.left, root2.left)
        if root1.right or root2.right:
            res &= isSameTree(root1.right, root2.right)
    else:
        return False
    return res

    
# practice dataset1

e = TreeNode('e')
f = TreeNode('f')
g = TreeNode('g')
d = TreeNode('d', None, g)
b = TreeNode('b', d, e)
c = TreeNode('c', None, f)
a = TreeNode('a', b, c)
n = TreeNode()

# practice dataset2

e1 = TreeNode(4)
f1 = TreeNode(7)
g1 = TreeNode(2)
d1 = TreeNode(1, None, g1)
b1 = TreeNode(3, d1, e1)
c1 = TreeNode(6, None, f1)
a1 = TreeNode(5, b1, c1)
n1 = TreeNode()

e2 = TreeNode(1)
d2 = TreeNode(1, None, e2)
c2 = TreeNode(4)
b2 = TreeNode(3, d2)
a2 = TreeNode(2, b2, c2)
n2 = TreeNode()

# calling functions

# print(maxDepth(a))
nodePrint(inorderTraversal(a))
nodePrint(inorderTraversal(n))
nodePrint(inorderTraversal(None))
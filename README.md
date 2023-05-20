# BinaryTreeModule

BinaryTreeModule is a Python module that provides useful functions for working with Binary Trees.

## Classes

### `TreeNode`

- This class is used to declare a node in a Binary Tree.
- Each node has a value (`val`) and references to its left child (`left`) and right child (`right`).

## Functions

1. `nodePrint(lst)`
   - Prints the values of the Binary Tree nodes.
   - Input: A list of `TreeNode` objects.
   - Time Complexity: O(n)
   - Space Complexity: O(n)

2. `maxDepth(root)`
   - Returns the maximum depth of the Binary Tree.
   - Input: The root `TreeNode` of the Binary Tree.
   - Time Complexity: O(n)
   - Space Complexity: O(h), where h is the height of the tree.

3. `inorderTraversal(root)`
   - Returns a list containing all the nodes of the Binary Tree in the order of inorder traversal.
   - Input: The root `TreeNode` of the Binary Tree.
   - Time Complexity: O(n)
   - Space Complexity: O(n)

4. `preorderTraversal(root)`
   - Returns a list containing all the nodes of the Binary Tree in the order of preorder traversal.
   - Input: The root `TreeNode` of the Binary Tree.
   - Time Complexity: O(n)
   - Space Complexity: O(n)
   
5. `postorderTraversal(root)`
   - Returns a list containing all the nodes of the Binary Tree in the order of postorder traversal.
   - Input: The root `TreeNode` of the Binary Tree.
   - Time Complexity: O(n)
   - Space Complexity: O(n)

6. `bfsTraversal(root)`
   - Returns a list containing all the nodes of the Binary Tree in the order of level-order traversal (BFS).
   - Input: The root `TreeNode` of the Binary Tree.
   - Time Complexity: O(n)
   - Space Complexity: O(n)

7. `bfsToTreeNode(bfs)`
   - Returns the root `TreeNode` of a Binary Tree constructed from the values in the level-order traversal array.
   - Input: A list of values representing the level-order traversal of a Binary Tree.
   - Time Complexity: O(n)
   - Space Complexity: O(n)

8. `isSameTree(root1, root2)`
   - Returns `True` if both Binary Trees are congruent (even if node addresses are not the same), and `False` otherwise.
   - Input: The root `TreeNode` of the first Binary Tree (`root1`) and the root `TreeNode` of the second Binary Tree (`root2`).
   - Time Complexity: O(n)
   - Space Complexity: O(h), where h is the height of the tree.

## Usage

You can use the BinaryTreeModule to perform various operations on Binary Trees in your Python projects. To use the module, import it into your Python script or interactive session:

```python
import BinaryTreeModule

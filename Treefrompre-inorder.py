# TC : O(n^2); n being no. of nodes
# SC : O(h); h being height of tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder)== 0:
            return
        
        idx = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:idx+1],inorder[0:idx])
        root.right = self.buildTree(preorder[idx+1:],inorder[idx+1:])
        return root

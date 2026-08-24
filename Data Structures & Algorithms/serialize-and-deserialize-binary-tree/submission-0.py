# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.s = ""

        def traverseTree(root, i=0):
            if not root: return
            self.s += "x" + str(i) + "y" + str(root.val)
            traverseTree(root.left, i*2+1)
            traverseTree(root.right, i*2+2)
            
        traverseTree(root)
        return self.s
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        ind, val = -1, -1
        self.d = {}
        for c in data:
            if c == 'x':
                self.d[int(ind)] = int(val)
                ind = ""
                readInd = True
            elif c == 'y':
                val = ""
                readInd = False
            else:
                if readInd: ind += c
                else: val += c
        self.d[int(ind)] = int(val)

        def buildDict(i):
            if i not in self.d: return None
            node = TreeNode(self.d[i], buildDict(i*2+1), buildDict(i*2+2))
            return node

        return buildDict(0)





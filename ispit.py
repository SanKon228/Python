class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild=None
        
def insert(root,newValue):
    if root is None:
        root=BinaryTreeNode(newValue)
        return root
    if newValue<root.data:
        root.leftChild=insert(root.leftChild,newValue)
    else:
        root.rightChild=insert(root.rightChild,newValue)
    return root
def minDepth(root):
    if root==None:
        return 0
    left = minDepth(root.leftChild)
    right = minDepth(root.rightChild)
    if left == 0 and right != 0:
        return right + 1
    if right == 0 and left != 0:
        return left + 1
    return min(left, right)+1
if __name__=="__main__":
    root= insert(None,14)
    insert(root,14)
    insert(root,9)
    insert(root,1)
    #print(root.leftChild.leftChild.data)
    print(minDepth(root))
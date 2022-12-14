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

def height(root):
        if root==None:
            return 0

        hleft=height(root.leftChild)

        hright=height(root.rightChild)  
        if hleft>hright:
            return hleft+1
        else:
            return hright+1
 
def CheckBalancedBinaryTree(root):

    if root==None:
        return True

    lheight= height(root.leftChild)
    rheight = height(root.rightChild)

    if(abs(lheight-rheight)>1):
        return False

    lcheck=CheckBalancedBinaryTree(root.leftChild)
    rcheck=CheckBalancedBinaryTree(root.rightChild)
    if lcheck==True and rcheck==True:
        return True
def exists(root,value):
    if root==None:
        print("False")
    elif root.data==value:
        print("True")
    elif root.data <value:
        return exists(root.rightChild,value)
    else:
        return exists(root.leftChild,value)
def delete(root,value):
    if root==None:
        return None
    elif root.data==value:
        return root==None
    elif root.data <value:
        return delete(root.rightChild,value)
    else:
        return delete(root.leftChild,value)
if __name__=="__main__":
    root= insert(None,2)
    insert(root,5)
    insert(root,3)
    exists(root,2)
    exists(root,4)
    delete(root,5)
    print(CheckBalancedBinaryTree(root))

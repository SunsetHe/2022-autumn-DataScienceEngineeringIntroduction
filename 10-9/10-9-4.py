class BinaryTree:
    def __init__(self,data=None,left=None,right=None):  # 如果创建节点对象时left或right参数为空，则默认该节点没有左或右子树
        self.data = data
        self.left = left
        self.right = right
    def print_leaf(self):  # 由前序遍历改编
        if self.left == None and self.right == None:
            print(self.data,end=' ')
        if self.left != None:
            self.left.print_leaf()
        if self.right != None:
            self.right.print_leaf()


layer3_2 = BinaryTree(2,BinaryTree(7),BinaryTree(4))
layer2_5 = BinaryTree(5,BinaryTree(6),layer3_2)
layer2_1 = BinaryTree(1,BinaryTree(0),BinaryTree(8))
layer1_3 = BinaryTree(3,layer2_5,layer2_1)

layer1_3.print_leaf()
class Queue:
    def __init__(self):
        self.__items = []
    def length(self):
        return len(self.__items)
    def isempty(self):
        if len(self.__items) == 0:
            return True
        else:
            return False
    def enqueue(self, element):
        self.__items.append(element)
    def dequeue(self):
        try:
            return self.__items.pop(0)
        except:
            print('ERROR:Queue is empty now!')
    def get_head(self):
        try:
            return self.__items[0]
        except:
            print('ERROR:Queue is empty now!')
    def get_tail(self):
        try:
            return self.__items[-1]
        except:
            print('ERROR:Queue is empty now!')


class BinaryTree:
    Q = Queue()  # 创建一个类属性，该队列为BinaryTree类派生的所有对象共有
    def __init__(self,data=None,left=None,right=None):  # 如果创建节点对象时left或right参数为空，则默认该节点没有左或右子树
        self.data = data
        self.left = left
        self.right = right
    def level_order(self):
        BinaryTree.Q.enqueue(self)  # 先将根节点加入队列
        while BinaryTree.Q.isempty() == False:
            node = BinaryTree.Q.dequeue()
            print(node.data,end=' ')
            if node.left != None:
                BinaryTree.Q.enqueue(node.left)
            if node.right != None:
                BinaryTree.Q.enqueue(node.right)


layer3_2 = BinaryTree(2,BinaryTree(7),BinaryTree(4))
layer2_5 = BinaryTree(5,BinaryTree(6),layer3_2)
layer2_1 = BinaryTree(1,BinaryTree(0),BinaryTree(8))
layer1_3 = BinaryTree(3,layer2_5,layer2_1)

layer1_3.level_order()
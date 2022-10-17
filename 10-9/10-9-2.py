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


q = Queue()
q.enqueue(7)
q.enqueue(5)
q.enqueue(8)
print(q.length())
print(q.isempty())
print(q.get_head())
print(q.get_tail())
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
print(q.isempty())
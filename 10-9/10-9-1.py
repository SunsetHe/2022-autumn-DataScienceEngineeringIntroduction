class Stack:
    def __init__(self):
        self.__items = []
    def isempty(self):  # 返回堆栈是否为空
        if len(self.__items) == 0:
            return True
        else:
            return False
    def length(self):
        return len(self.__items)
    def push(self,element):  # 压入堆栈
        self.__items.append(element)
    def pop(self):  # 弹出堆栈，注意需要处理堆栈为空的情况
        try:
            return self.__items.pop()
        except:
            print('ERROR: Stack is empty now!')


def dec2bin(num):
    s = Stack()
    while num != 0:
        s.push(num % 2)
        num = num // 2
    while s.length() != 8:
        s.push(0)
    result = ''
    while s.isempty() == False:
        result += str(s.pop())
    return result


ip_dec = '203.179.25.37'
ip_dec_list = ip_dec.split('.')
result = ''
for ip in ip_dec_list:
    result += dec2bin(int(ip))
print(result)
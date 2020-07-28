from collections import deque


class Stack:

    def __init__(self):
        self.stack_list = deque()
        pass

    def isEmpty(self) -> bool:
        for i in self.stack_list:
            if i:
                return True
        return False

    def push(self, add_data):
        self.stack_list.append(add_data)
        pass

    def pop(self):
        self.stack_list.pop()
        pass

    def peek(self):
        x = self.stack_list[-1]
        return x

    def size(self):
        return len(self.stack_list)


some = Stack()

if __name__ == "__main__":

    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]

    def smile(add_data):
        for i in add_data:
            if i in open_list:
                some.push(i)
            elif i in close_list:
                pos = close_list.index(i)
                if ((some.size() > 0) and (open_list[pos] == some.peek())):
                    some.pop()
                else:
                    return "Несбалансировано"
            if some.size() == 0:
                return "Сбалансированно"



print(smile('[([])((([[[]]])))]{()}'))

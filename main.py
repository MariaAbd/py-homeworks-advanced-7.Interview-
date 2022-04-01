
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def check_brackets(self, str_):
        is_right = True
        for i in str_:
            if i in '([{':
                self.push(i)
            elif i in ')]}':
                if self.isEmpty():
                    is_right = False
                    break
                open_bracket = self.pop()
                if open_bracket == '(' and i == ')':
                    continue
                if open_bracket == '[' and i == ']':
                    continue
                if open_bracket == '{' and i == '}':
                    continue
                is_right = False
                break
        if is_right and len(self.items) == 0:
            print('Сбалансированно')
        else:
            print('Несбалансированно')


stack = Stack()
s = input()
stack.check_brackets(s)


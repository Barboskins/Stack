"""Необходимо реализовать класс Stack со следующими методами:
isEmpty - проверка стека на пустоту. Метод возвращает True или False.
push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
size - возвращает количество элементов в стеке."""


class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)


"""Используя стек из задания 1 необходимо решить задачу на проверку сбалансированности скобок. 
Сбалансированность скобок означает, что каждый открывающий символ имеет соответствующий ему закрывающий, 
и пары скобок правильно вложены друг в друга."""
"""1 вариант"""
def balance(myStr):
    openBrackets = ["[","{","("]
    closeBrackets = ["]","}",")"]
    stack= Stack()
    for i in myStr:
        if i in openBrackets:
            stack.push(i)
        elif i in closeBrackets:
            pos = closeBrackets.index(i)
            if stack.size() > 0 and openBrackets[pos] == stack.peek():
                stack.pop()
            else:
                return "Несбалансированно"
    if stack.size() == 0:
        return "Сбалансированно"

if __name__ == '__main__':
    print(balance('(((([{}]))))'))
    print(balance('[([])((([[[]]])))]{()}'))
    print(balance('{{[()]}}'))
    print('===================================')
    print(balance('}{}'))
    print(balance('{{[(])]}}'))
    print(balance('[[{())}]'))

"""2 вариант"""
def check(myStr):
    Brakets = {'(': ')', '{': '}', '[': ']'}
    stack = Stack()
    for i in myStr:
        if i in Brakets:
            stack.push(i)
        elif i in Brakets.values():
            if stack.size() > 0 and i == Brakets.get(stack.peek()):
                stack.pop()
            else:
                return "Несбалансированно"
    if stack.size() == 0:
        return "Сбалансированно"

if __name__ == '__main__':
    print(check('(((([{}]))))'))
    print(check('[([])((([[[]]])))]{()}'))
    print(check('{{[()]}}'))
    print('===================================')
    print(check('}{}'))
    print(check('{{[(])]}}'))
    print(check('[[{())}]'))

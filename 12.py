class Stack:
    
    def __init__(self):
        self._array = []

    def push(self, item):
        self._array.append(item)
        return "ok"

    def pop(self):
        if len(self._array)!=0:
            return self._array.pop()
        else:
            return "error"

    def back(self):
        if len(self._array) != 0:
            return self._array[-1]
        else:
            return "error"
    def size(self):
        return len(self._array)

    def clear(self):
        self._array.clear()
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


with open("12.txt") as f:
    stack = Stack()
    for line in f:
        result = stack.execute(line)
        print(result)
        if result == "bye":
            break
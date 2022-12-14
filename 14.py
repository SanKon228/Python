class Queue:
    def __init__(self):
        self._array = []

    def push(self, item):
        self._array.append(item)
        return "ok"

    def pop(self):
        if len(self._array)!=0:
            return self._array.pop(0)
        else:
            return "error"

    def front(self):
        if len(self._array) != 0:
            return self._array[0]
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


with open("14.txt") as f:
    que = Queue()
    for line in f:
        result = que.execute(line)
        print(result)
        if result == "bye":
            break
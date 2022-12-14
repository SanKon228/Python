class Queue:
    def __init__(self):
        self.q = [0] * 200
        self.b = 0
        self.e = 0

    def enque(self, item):
        self.q[self.e] = item
        self.e += 1

    def deque(self):
        item = self.q[self.b]
        self.b += 1
        return item

    def empty(self):
        return self.b == self.e


def bfs(g, s, f):
    n = len(g)

    q = Queue()
    q.enque(s)

    distances = [-1] * n
    distances[s] = 0

    while not q.empty():
        cur = q.deque()
        for i in range(n):
            if g[cur][i] == 1 and distances[i] == -1:
                q.enque(i)
                distances[i] = distances[cur] + 1

    return distances[f]

n, s, f = 4,4,3
g = [[0, 1, 1, 1],[1, 0, 1, 0],[1, 1, 0, 0],[1, 0, 0, 0]]
res = bfs(g, s - 1, f - 1)
if res == -1:
    print(0)
else:
    print(res)
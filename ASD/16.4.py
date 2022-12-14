class Tree:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.children = []
    def add(self, key):
        self.children.append(key)

    def childrenCount(self):
        return len(self.children)

    def str(self):
        return str(self.key) + ", " + str(self.value) + ": " + str(self.children)
aparat = [Tree(0, 0)]


def main():
    global aparat
    with open("input.txt") as file:
        clerksNum = int(file.readline())
        
        for i in range(1, clerksNum + 1):
            properties = list(map(int, file.readline().split()))
            value = properties[0]
            clerk = Tree(i, value)
            aparat.append(clerk)

            children_count = properties[1]
            childrens = properties[2:]
            for child in childrens:
                clerk.add(child)


def corr(key, current_pay):
    global record, aparat

    clerk: Tree = aparat[key]
    new_pay = current_pay + clerk.value
    if new_pay > record:
        return

    if clerk.childrenCount() == 0:
        if new_pay < record:
            record = new_pay
    else:
        for child in clerk.children:
            corr(child, new_pay)


if __name__ == "__main__":
    record = 105001
    main()
    corr(1, 0)
    print(record)

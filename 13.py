def convert_base(num, to_base, from_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)

    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]
class Node:
    def __init__(self, item):
        self.item = item 
        self.next = None 
class Stack:
    def __init__(self):
        self.top_node = None
    def empty(self):
        return self.top_node is None
    def push(self, item):
        new_node = Node(item) 
        if not self.empty(): 
            new_node.next = self.top_node 
        self.top_node = new_node
    def pop(self):

        if self.empty(): 
            raise Exception("Stack: 'pop' applied to empty container")
        current_top = self.top_node
        item = current_top.item 
        self.top_node = self.top_node.next
        del current_top 
        return item

    def top(self):
        if self.empty():
            raise Exception("Stack: 'top' applied to empty container")
        return self.top_node.item
def get_char_digit(digit):
    if digit <= 9:
        str_digit = str(digit)
    else:
        str_digit = chr(ord("A") + digit - 10)
    return str_digit
def convert(dec_number, base):

    stack = Stack() 
    while dec_number > 0:
        stack.push(dec_number % base)
        dec_number //= base
    converted = ""
    while not stack.empty():
        converted = converted + get_char_digit(stack.pop())
    return converted
if __name__ == "__main__":
    print(convert(123,21))
    print(convert_base(123,21))
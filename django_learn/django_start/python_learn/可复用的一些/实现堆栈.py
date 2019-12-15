

class Stack(object):
    def __init__(self,size):
        self.items = []
        self.size = size

    def is_empty(self):
        return self.items ==[]

    # def stackofsize(self):
    #     return len(self.items)
    def is_full(self):
        if len(self.items) ==self.size:
            print("It is full")

    def in_stack(self,a):
        if len(self.items) ==self.size:
            print("It is full")
        else:
            return self.items.append(a)

    def out_stack(self):
        return self.items.pop()
    def max(self):
        max_int = []
        if self.items >max_int:
            self.items =max_int
s = Stack(5)
s.in_stack(1)
s.in_stack(6)
s.in_stack(10)
s.in_stack(12)
s.in_stack(12)
s.in_stack(32)
s.in_stack(223)
s.in_stack(6)
print(s.items)
s.out_stack()
print(s.items)
s.out_stack()
print(s.items)
# print(s.items)
print(s.size)
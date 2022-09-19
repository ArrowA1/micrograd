class Value:


    def __init__(self, data, _children = None, _op = '', label = ''):

        self.data = data
        self._children = (_children)
        self._op = _op
        self.label = label


    def __repr__(self):

        output = f"Value(data={self.data} | {self.label})"
        return output


    def __add__(self, other):

        sum = Value(self.data + other.data, (self, other), _op = '+')
        return sum


    def __mul__(self, other):

        product = Value(self.data * other.data, (self, other), _op = '*')
        return product


a = Value(data = 2, label = 'a')
b = Value(data = -4, label = 'b')
c = a + b;  c.label = 'c'
d = a * b;  d.label = 'd'
print(a)
print(b)
print(c)
print(c._children)
print(c._op)
print(d)
print(d._children)
print(d._op)

class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2


p = Point(2, 8)

# PRINT THE X&Y-VALUES OF THE POINT
print(p.x)
print(p.y)

# CREATED A CLASS (Flight which takes capacity as input)


class FLight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
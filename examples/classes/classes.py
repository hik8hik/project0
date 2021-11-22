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
    # FUNCTION FOR CAPACITY
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    # FUNCTION TO APPEND PASSENGERS WITH NAME
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    # FUNCTION TO GET EMPTY SEATS
    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = FLight(3)
print(flight)

people = ["HIK HIK", "HIKAL LAKIH", "LAKIH HIKAL", "OTHER USER"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person}, ")
        # PRINT: Added.....
    else:
        print(f"No available seats for {person} ")
        # PRINT: No available seats for OTHER USER

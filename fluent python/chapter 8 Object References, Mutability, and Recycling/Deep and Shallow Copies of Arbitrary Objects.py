# coding = utf-8

# Example 8-8. Bus picks up and drops off passengers

class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


# Example 8-9. Effects of using copy versus deepcopy

import copy

bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
print(id(bus1), id(bus2), id(bus3))  # they are all different
bus1.drop('Bill')
print(bus2.passengers)
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
print(bus3.passengers)  # The deep copy in Python is really so easy...

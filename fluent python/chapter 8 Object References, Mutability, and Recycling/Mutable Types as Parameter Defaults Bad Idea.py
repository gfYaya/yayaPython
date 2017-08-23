# coding = utf-8

# Example 8-12. A simple class to illustrate the danger of a mutable default

class HauntedBus:
    """A bus model haunted by ghost passengers"""

    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


# Example 8-13. Buses haunted by ghost passengers

bus1 = HauntedBus(['Alice', 'Bill'])
bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers)  # ['Bill', 'Charlie']
print('dir : ', dir(HauntedBus.__init__))
print('init default : ', HauntedBus.__init__.__defaults__)
# warning:there is no arguments here
bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers)  # ['Carrie']
print('dir : ', dir(HauntedBus.__init__))
print('init default : ', HauntedBus.__init__.__defaults__)
# warning:there is no arguments here
bus3 = HauntedBus()
print(bus3.passengers)  # ['Carrie']
print('dir : ', dir(HauntedBus.__init__))
print('init default : ', HauntedBus.__init__.__defaults__)
bus3.pick('Dave')
print('dir : ', dir(HauntedBus.__init__))
print('init default : ', HauntedBus.__init__.__defaults__)
# warning:here is bus2
print(bus2.passengers)  # ['Carrie', 'Dave']
print(bus2.passengers is bus3.passengers)  # True
print(bus1.passengers)  # ['Bill', 'Charlie']

# result: When a module is loaded,the keyword arguments which store the default values become attributes of the
#  functinon object.If a default value is a mutable object,and you change it,the change will affect every future
#  call of the function.

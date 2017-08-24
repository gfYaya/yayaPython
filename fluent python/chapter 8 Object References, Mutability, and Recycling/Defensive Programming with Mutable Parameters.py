# coding = utf-8

# Example 8-15. A simple class to show the perils of mutating received arguments

class TwilightBus:
    """A bus model that makes passengers vanish"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)  # shallow copy
            # self.passengers = passengers # we could mutate the original list which the arguments constructor received

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


# Example 8-14. Passengers disappear when dropped by a TwilightBus

basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
bus = TwilightBus(basketball_team)
bus.drop('Tina')
bus.drop('Pat')
print(basketball_team)

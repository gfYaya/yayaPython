# coding = utf-8

# Example 7-8. average_oo.py: A class to calculate a running average

class Averager:
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


avg = Averager()
print(avg(10))
print(avg(11))
print(avg(12))


# Example 7-9. average.py: A higher-order function to calculate a running average

def make_average():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


# Example 7-10. Testing Example 7-9

avg = make_average()
print(avg(10))
print(avg(11))
print(avg(12))

# Example 7-11. Inspecting the function created by make_averager in Example 7-9

print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)

# Example 7-12. Continuing from Example 7-10
print(avg.__closure__)
print(avg.__closure__[0].cell_contents)

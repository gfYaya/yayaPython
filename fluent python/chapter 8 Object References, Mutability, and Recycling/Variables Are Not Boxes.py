# coding = utf-8

# Example 8-1. Variables a and b hold references to the same list, not copies of the list
#  This demonstration is a simple interaction shows that the "variables as boxes" idea in Java cannot explain in Python.
# But I have test just now,Java is really not 'variables as boxes' apart from String and primitive value type.It means
# that, it's the same with Java on the reference variables.

a = [1, 2, 3]
b = a
a.append(4)
print(b)  # [1, 2, 3, 4]

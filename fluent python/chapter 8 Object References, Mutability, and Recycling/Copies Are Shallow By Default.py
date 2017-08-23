# coding = utf-8

# a simple demo

l1 = [3, [55, 44], (7, 8, 9)]
#   An object's identity never changed once it has been created.'list(l1)' is created here and variable l2
# is pointed to this new object,In the variable stack , l2 stored the reference of this new object which is created
# by the 'list(l1)' operation.So l2 stores a separate list container,not the same as l1 stores.A new identity.
l2 = list(l1)
# The easiest way to copy a list (or most built-in mutable collections) is to use the builtin
#   constructor for the type itself like this.
print(l2)
print(l1 == l2)
print(id(l1) == id(l2))
print(l1 is l2)  # False

print('--------------------')
l3 = l1[:]  # It's a copy too.But both are shallow copy.
print(l3 == l1)
print(l3 is l1)

# Example 8-6. Making a shallow copy of a list containing another list; copy and paste
#   this code to see it animated at the Online Python Tutor.
# http://www.pythontutor.com

l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)
l1.append(100)
l1[1].remove(55)
print('l1:', l1)
print('l2:', l2)
l2[1] += [33, 22]
l2[2] += (10, 11)
print('l1:', l1)
print('l2:', l2)

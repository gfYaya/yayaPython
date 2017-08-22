# coding = utf-8

# Example 8-3. charles and lewis refer to the same object

charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles
# The operators is and is not test for object identity: x is y is true if and only if x and y are the same object.
#  x is not y yields the inverse truth value.
print(lewis is charles)
print(id(charles), id(lewis))
lewis['balance'] = 950
print(charles)  # 'balance': 950}

# Example 8-4. alex and charles compare equal, but alex is not charles

alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
print(alex == charles)  # Is it means that '==' operation compares the values in momery(or the data objects hold),
# 'is' compares the reference?
print(alex is charles)
# They have the same value,but not the same identity.

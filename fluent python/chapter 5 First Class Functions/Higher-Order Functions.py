# coding = utf-8

# Example 5-3. Sorting a list of words by length

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))  # Any one-argument function can be used as the key


# Example 5-4. Sorting a list of words by their reversed spelling

def reverse(word):
    return word[::-1]


print(reverse('testing'))
print(sorted(fruits, key=reverse))  # ['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']
# sorting first,then start to execute the  function key?
print(reverse(fruits))  # ['banana', 'raspberry', 'cherry', 'apple', 'fig', 'strawberry']

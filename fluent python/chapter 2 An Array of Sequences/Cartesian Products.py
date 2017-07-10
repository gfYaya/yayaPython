# coding = utf-8

# Example 2-4. Cartesian product using a list comprehension

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

tshirts = [(color, size) for size in sizes for color in colors]
print(tshirts)

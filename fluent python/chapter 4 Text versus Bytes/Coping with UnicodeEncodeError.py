# coding = utf-8

# Example 4-6. Encoding to bytes: success and error handling
city = 'São Paulo'
city.encode('utf-8')  # 该函数并没有是city本身发生修改
print(city)
print(city.encode('utf-8'))
print(city.encode('utf-16'))
print(city.encode('iso8859_1'))
# print(city.encode('cp437'))
#  UnicodeEncodeError: 'charmap' codec can't encode character '\xe3' in position 1: character maps to <undefined>
#  'ã' can't be converted

print(city.encode('cp437', errors='ignore'))
print(city.encode('cp437', errors='replace'))
print(city.encode('cp437', errors='xmlcharrefreplace'))

# coding = utf-8

# Example 4-9. A platform encoding issue (if you try this on your machine, you may or may not see the problem)

open('cafe.txt', 'w', encoding='utf-8').write('café')
print(open('cafe.txt').read())  # caf茅  =>but in cafe.txt,the content is café

# Example 4-10. Closer inspection of Example 4-9 running on Windows reveals the bug and how to fix it
print('华丽的分割线:~~~~~~~~~~~~~~~~~~~')

fp = open('cafe.txt', 'w', encoding='utf-8')
print(fp)
fp.write('café')
fp.close()
import os

print(os.stat('cafe.txt').st_size)

print('fp2')
fp2 = open('cafe.txt')
print(fp2)
print(fp2.encoding)  # cp936
print(fp2.read())  # caf茅

print('fp3')
fp3 = open('cafe.txt', encoding='utf-8')
print(fp3)
print(fp3.read())  # café  =>now ,it's right

print('fp4')
fp4 = open('cafe.txt', 'rb')
print(fp4)
print(fp4.read())

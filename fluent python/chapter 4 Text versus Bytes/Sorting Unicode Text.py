# coding = utf-8

# Example 4-19. Using the locale.strxfrm function as sort key

import locale  # locale 包依赖的是POXIS协议

# locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')
locale.setlocale(locale.LC_COLLATE, 'C.UTF-8')
# 上两个 尤其后者 执行 locale cmd命令,得到的是LC_COLLATE是存在的,值也为C.UTF-8 ,为何还会报错?在Linux上再试试?
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=locale.strxfrm)
print(sorted_fruits)

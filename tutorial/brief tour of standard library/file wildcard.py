# coding=utf-8
import glob

print(glob.glob('*.py'))
print(glob.glob('*.py', recursive=True))

# as shown in the following code was reinforced by myself
import os

os.chdir('E:\\yaya\\yayaPython\\tutorial\\classes')
print(os.getcwd())
print(glob.glob('*.py'))

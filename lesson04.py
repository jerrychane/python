import sys
print('line 1st')
print('line 2nd')
print()
print('line 4th')
print('Hello', 'jack', 'mike', '...', 'all you guys!')
name = 'Ann'
age = '22'
print(f'{name} is {age} years old')
print('Hello', 'world!')  # 下一行输出的内容和这一行相同
print('Hello', 'world!', sep=' ', end='\n', file=sys.stdout, flush=False)
print('Hello', 'world!', sep='-', end='\t')
print('Hello', 'world!', sep='~')  # 上一行的末尾是 \t，所以，这一行并没有换行显示
print('Hello', 'world!', sep='\n')  # 参数之间用换行符 \n 分隔

print(sorted('abdc'))
print(sorted('abdc', reverse=True))

print(divmod(11, 3))
a, b = divmod(11, 3)
print(a)
print(b)

print(divmod(3, 11))
a, b = divmod(3, 11)
print(a)
print(b)

print(pow(2, 3))
print(pow(2, 3, 4))

print(bool())
print(bool(3.1415926))
print(bool(-3.1415926))
print(bool(1 == 2))
print(bool(None))

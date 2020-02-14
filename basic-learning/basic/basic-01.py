##########################
# author:     banbao     #
# language:   python     #
# encoding:   utf-8      #
##########################

# 基础语法, 列表(list)

# 单行注释

'''
    多行注释
'''

# 强制类型转化, 当作函数

a = '1'
b = int(a)
c = str(a)
d = float(a)

# print函数输出

name = 'banbao'
print('1: ' + name)
print('2: my name is %s' %name)

# 格式化输出: %d %f %s

money = 2.21
print('3: I have %.1f yuan' %money)

# 多个变量输出
# 元组
print('4: my name is %s,I have %f yuan' %(name,money))

# 其他方式
print('5: my name is', name)
print('6: I have %s yuan' %money)
print('7: my ' + 'name is ' + name)
print('8: 6 a: ' + 'a'*6)

# 算数:
    # + - * / //(整除) % **(幂)

# 分支语句
    # if else
    # if elif else
# True, False
# pass 关键字
judge = False
if judge:
    print('8: success')
else:
    pass
    
# 与(and), 或(or), 非(not)

# while

# break, continue

# for
print('9: ')
for x in name:
    if(not (x == 'b')):
        print(x)
        
# 'string'/"string"
    # str, 是unicode字符串
    # bytes, 就是经过编码后的字符串, 一种字节码
output = ('my name is %s' %name)
print('10: ' + output)

# 字符串格式化
    # %s,%d,%f
    # format
output = 'my name is {}, I have {} yuan'.format(name, money)
print('11: ' + output)
output = 'my name is {arg1}, I have {arg2} yuan'.format(arg1 = name,arg2 = money)
print('12: ' + output)

# 下标
# 负数表示从后往前
print('13: ' + name[0] + name[-1])

# 切片操作
# [start:end:step] 
    # 左开右闭 [start)
print('14: ' + name[0:-1:1])
print('\t' + name[-1::-1])

# 字符串操作
print('15: 字符串操作')
print(name.find('ba'))                              # find/rfind 找不到返回-1
print(name.rfind('ba'))
print(name.index('ba'))                             # index/rindex 找不到抛出异常
print(name.rindex('ba'))
print(len(name))                                    # len
print(name.count('b'))                              # count
print(name.replace('b', 'B'))                       # replace
print(name.split('a', 2))                           # split(分隔符, 分割次数(默认-1,溢出取最多))
print(name.startswith('b'))                         # startswith/endswith
print(name.endswith('b'))
print(name.lower())                                 # lower/upper
print(name.upper())
print(('|' + ' ' + name + ' ').strip() + '|')       # strip/lstrip/rstrip 去掉空格
print(('|' + ' ' + name + ' ').lstrip() + '|')
print(('|' + ' ' + name + ' ').rstrip() + '|')
print(name.partition('nb'))                         # partition 切分
print(name.partition('bn'))
print((name + '\t').isalnum())                      # isalnum 是否由字符+数字组成
print(name.isalnum())
print(('1' + name).isalpha())                       # isalpha 是否由字符组成
print(name.isalpha())
print(name.isdigit())                               # isdigit 是否由数字组成
print(name.isspace())                               # isspace 是否由空白符组成
print('\t'.isspace())
print('my name is %s' %name)                        # format 格式化

# 转义符
# '\' 出现在行尾是作为续行符
print('16: 第一行'\
'第二行')

# 原生字符串 r'xxx', 不会进行转义
print(r'17: \t')

# 字符串的编码与解码
# python 默认 unicode
# utf-8 是 unicode 的一种实现方式 
# encode('utf-8'): 将unicode编码成bytes类型, 编码方式为utf-8
# decode('utf-8'): 将bytes解码成unicode类型, 解码方式为utf-8

# list 定义
# list 等号赋值为指针
print('18: 列表list')
fruits_1 = ['apple', '香蕉']
print(fruits_1)

# list 遍历
for fruit in fruits_1:
    print(fruit)

fruit_num = len(fruits_1)
index = 0
while index < fruit_num:
    print(fruits_1[index])
    index += 1

# list 嵌套
fruits_2 = ['火龙果', '葡萄', ['橘子', 'orange']]
for fruit in fruits_2:
    print(fruit)

# list 加法
print(fruits_1 + fruits_2)

# list 切片(与字符串类似)

# list 常用操作
fruits_3 = fruits_1.copy()      # = 为指针(浅拷贝), copy9(深拷贝)
fruits_3.append('watermelon')   # append
print(fruits_3)

fruits_3 = fruits_1.copy()
fruits_3.append(fruits_2)       # append, 将 list 作为一个元素加在最后
print(fruits_3)

fruits_3 = fruits_1.copy()
fruits_3.extend(fruits_2)       # extend, 将 list 拆解开附加在最后
print(fruits_3)

print(fruits_1.count('apple'))  # count
print(fruits_1.index('apple'))  # index, 找不到则抛出异常

fruits_3 = fruits_1.copy()
fruits_3.insert(0, 'grapes')    # insert
print(fruits_3)

fruits_3 = fruits_1.copy()
print(fruits_3.pop())           # pop, 删除最后一个元素并返回这个元素 
print(fruits_3)

fruits_3 = ['a', 'a', 'a']
fruits_3.remove('a')            # remove, 移除第一个匹配的
print(fruits_3)

fruits_3 = fruits_1.copy()
fruits_3.reverse()              # reverse, 改变原来顺序
print(fruits_3)

fruits_3 = ['b', 'a']
fruits_3.sort()                 # sort, 改变原来顺序
print(fruits_3)

fruits_3 = ['b', 'a']
print(sorted(fruits_3))         # sorted, 不改变原来顺序
print(fruits_3)

fruits_3 = fruits_1.copy()
del fruits_3[0]                 # del, 按下标删除元素
print(fruits_3)

print('apple' in fruits_1)      # in 判断是否存在于list中

# list() 强制类型转换

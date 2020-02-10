##########################
# author:     banbao     #
# language:   python     #
# encoding:   utf-8      #
##########################

# 元组(tuple), 字典(dictionary)

# 元组
    # 使用括号(), 不可修改
num = (1, 2, 3, 4)
print('1:元组, num:{}'.format(num))

num1  = 1, 2, 3
print(num1)

num2 = (1, 2, 3)
print(num2)

# tuple 函数
num3 = [1, 2, 3]
print(tuple(num3))

num4 = 1,           # 逗号','隔开
print(num4)

print(num[1])       # 下标操作

# 切片操作(与str/list类似)

# 解组
a, b, c, d = num
print(a, b, c, d)

a, _, b, c = num       # _ 跳过
print(a,b,c)

# count / index

print('2: dictionary')
# 字典(key, value), 字典是无顺序的
    # 创建字典 1
person1 = {'name':'banbao', 'age':20}
print(person1)

    # 创建字典 2
person2 = dict(name = 'SMJB', age = 18)      # dict 函数

    # 函数
print(len(person1))                          # len

print(person1['name'])                       # [], 不存在时抛出异常

print(person1.get('hobby'))                  # 找不到时返回 None
print(person1.get('hobby', 'ping-pong'))     # 找不到时返回 ping-pong

person1['hobby'] = 'chess'                   # 设置 key-value 对
print(person1)

print('hobby' in person1)                    # in 判断是否存在

print(person1)
person1.clear()                              # clear
print(person1)

person1 = dict(name = 'banbao', age = 18)
print(person1)
person1.pop('age')                           # pop
print(person1)

person1 = person2.copy()                     # = 是浅拷贝
print(person1)
person1.popitem()                            # LIFO(stack), 最末尾
print(person1)
print(person2)

person1 = {'name':'banbao', 'age':20, 'hobby':'chess'}
person2 = dict(name = 'SMJB', age = 18, food = 'carrot')
# update, 用一个字典更新另外一个字典, 覆盖相同key的value
person2.update(person1)     # 用 1 更新 2
print(person1)
print(person2)

person2 = dict(name = 'SMJB', age = 18, food = 'carrot')
# setdefault, 若有值返回值, 没有则返回设定值
print(person2.setdefault('name', 'Lily'))
print(person2.setdefault('weapon', 'wand'))

# in

# 字典的遍历
person2 = dict(name = 'SMJB', age = 18, food = 'carrot')

# keys(), 转换成一个list
for x in person2.keys():
    print('{} : {}'.format(x,person2[x]))

# iterkeys(), 遍历keys, 不转换, 省内存
# 已经废除
'''
for x in person2.iterkeys():
    print(x)
'''

# values()
# itervalues()
    # 已经废除

# items()
for x, y in person2.items():
    print('{}:{}'.format(x, y))

# iteritems()
    # 已经废除



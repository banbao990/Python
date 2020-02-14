##########################
# author:     banbao     #
# language:   python     #
# encoding:   utf-8      #
##########################

from functools import reduce # reduce

# 附加内容

# map 函数
def main01():
    print('*'*5 + 'map' + '*'*5)
    a = [1,2,3,4]
    b = map(lambda x: x ** 2, a)
    for x in b:
        print(x)

# filter 函数
def main02():
    print('*'*5 + 'filter' + '*'*5)
    a = [1,2,3,4]
    b = filter(lambda x : x % 2 == 0, a)
    for x in b:
        print(x)

# reduce 函数
def main03():
    print('*'*5 + 'reduce' + '*'*5)
    a = [1,2,3,4]
    print(reduce(lambda x , y:x * y, a, 10))

# 类三目运算符
def main04():
    print('*'*5 + '..if..else..' + '*'*5)
    print(1 if True else 0)

# 列表生成式
def main05():
    print('*'*5 + '.list.' + '*'*5)
    value = [x for x in range(1, 10) if x % 2 == 0]
    print(value)

if __name__ == '__main__':
    main01()
    main02()
    main03()
    main04()
    main05()

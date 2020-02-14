##########################
# author:     banbao     #
# language:   python     #
# encoding:   utf-8      #
##########################

# 函数(function)

def hello():
    print('hello world!')

hello()

def sub(a, b):
    print(a - b)

# 按照顺序给定参数值, 顺序相关(位置参数)
sub(1, 2)
sub(2, 1)

# 按照参数名称给定参数值, 顺序无关(关键字参数)
sub(a = 1, b = 2)
sub(b = 2, a = 1)

# *a 表示位置参数(元组)
# **b 表示关键字参数(字典)
def show(*a, **b):
    print(a)
    print(b)

show(1, 2, a = 3, b = 4)

a = (1, 2, 3)
b = dict(a=1, b=2, c=3)
show(*a, **b)

# 默认参数
    # 默认参数一定要放在其他参数的后面
def show2(name, age = 18):
    print('my name is {}, I am {} years old.'.format(name, age))

show2('banbao')
show2('SMJB', 20)

# 函数返回值, 可以为元组/字典
    # 返回一个值
def show3(a, b):
    return (a + b)

print(show3(1, 2))

    # 返回元组
def show4(a, b):
    return (a, b)

print(show4(1, 2))

    # 返回字典
def show5(a, b):
    global sh5
    sh5 = 1
    print('sh5\'id(1):{}'.format(id(sh5)))
    return {'name':a, 'age':b}

s5 = show5(1, 2)
print('---show5---to---show6---')
print(s5)
print(s5['name'])
print('sh5\'id(2):{}'.format(id(sh5)))

# 全局变量与局部变量
# 全局变量:在函数/代码块之外定义的变量
# global关键字: 在函数/代码块中修改全局变量, 应使用global关键字
def show6():
    hh = 1
    # sh5 = 10 # 加上这一句之后 id(sh5) 就会变
    # 一个函数内定义的全局变量不能在另一个函数内修改
    print('sh5\'id(3):{}'.format(id(sh5)))
    s5['name'] = 10

show6()
print(s5)

# sh5 = 10 一个函数内定义的全局变量在函数外面也不能直接修改, 否则 id 会变
print('sh5\'id(4){}, sh5:{}'.format(id(sh5), sh5))
'''
局部变量报错
print(hh)
'''
# global关键字: 如果想在函数或者某个代码块中修改全局变量, 那么应该使用global关键字
    # 测试实际上的修改十重新申请一个值, 换了个id
    # 似乎所有的都是这么做的
'''
# code 
a = 1
print(id(a))
a = 2
print(id(a))
# output
140731697579680
140731697579712
'''
# 列表和字典当作全局变量:列表和字典当作全局变量,
    # 在函数或者代码块中使用的时候,可以任意的增删改查列表和字典的值
    # 但是如果要修改这个全局变量指向的值，则必须加global关键字
# 一些例子

########## 1
'''
# code:
s = {'name':10}

def test():
    s['name'] = 11
    print(id(s))

test()
print(s)
print(id(s))

# output:
1739676169408
{'name':11}
1739676169408
'''

########## 2
'''
# code:
s = 10
def test():
    s = 11
    print(id(s))

test()
print(s)
print(id(s))

# output:
140731376125920
{'name':11}
140731376125888
'''

########## 3
'''
# code:
s = 10
def test():
    global s
    s = 11
    print(id(s))

test()
print(s)
print(id(s))

# output:
140731376125920
{'name':11}
140731376125920
'''

########## 4
'''
# code
def test():
    global s
    s = 11
    print(id(s))

def test2():
    print(s)
    print(id(s))

test()
test2()

# output:
140731373897696
11
140731373897696
'''

# 匿名函数
# 字典的排序
def sort_key(x):
    return x['age']
    
l = [{'username':'banbao','age':20},{"username":'SMJB','age':18}]
l.sort(key = sort_key)
print(l)

# lambda
l = [{'username':'banbao','age':20},{"username":'SMJB','age':18}]
l.sort(key = (lambda x:x['age']))
print(l)


##########################
# author:     banbao     #
# language:   python     #
# encoding:   utf-8      #
##########################

import sys

# 类和对象, 封装是·/继承/多态
# 所有类都必须继承自 object 类

class Person(object):
    # 所有函数都必须有参数 self
    def eat(self, food):
        print('Eating %s.' %food)
    
    # 构造函数
    def __init__(self):
        self.__name = 'banbao'      # 私有变量(方法类似)
        self._nickname = 'SMJB'     # 保护变量
        self.nick = 'JinDan'        # 公有变量
    
    # 析构函数
    def __del__(self):
        pass

# 继承
# 私有属性和方法是不能被子类继承的
# 同名方法测试

# 如何查看一个类式新式类还是旧式类：
    # print(type(Person))
        # 如果以下打印出来的是type，那么是新式类(Python3后)
        # 如果以下打印出来的是classobj，那么是旧式类
# 新式类多继承顺序使用C3算法
# 旧式类不能使用super关键字(使用父类名)

class A(object):
    def have(self):
        print('A have')
    def eat(self):
        print('A eat')

class a(A):
    def eat(self):
        super(a, self).eat()
        print('a eat')
    
class B(object):
    def eat(self):
        print('B eat')
        
class b(B):
    def eat(self):
        super(b, self).eat()
        print('b eat')

class ab(a, b):
    def eat(self):
        super(ab, self).eat()

class Student(Person):
    # 重写父类方法
    def eat(self, food):
        super(Student, self).eat(food)      # 调用父类同名函数
        print('%s is delicious.' %food)
    # 静态方法
    def study(cls):
        print('Studying...')

# 继承顺序测试 C3算法(merge)
#         1
#      /     \
#      2     3
#     / \   / \
#    4   5 6   7
#               84526731(object)

#         1
#      /     \
#      2     3
#      |    / \
#      4   5   6
#      |
#      7
#               87425631(object)
class a1(object):
    pass

class a2(a1):
    pass

class a3(a1):
    pass

class a4(a2):
    pass

class a5(a2):
    pass

class a6(a3):
    pass

class a7(a3):
    pass

class a8(a4, a5, a6, a7):
    pass

# 多态, 不同的对象, 都实现了同一个接口

# 执行顺序: __new__/__init__/__del__

class Picture(object):
    def __new__(cls, *args, **kwargs):
        print('new')
        # 不返回对象则不生成对象
        return super(Picture, cls).__new__(cls, *args, **kwargs)
    
    def __init__(self):
        print('init')
    
    def __del__(self):
        print('del')

def main01():
    print('*****main01*****')
    a = Person()
    a.eat('apple')
    a.age = 20          # 绑定变量
    print(sys.getrefcount(a))      # 获取引用计数(调用该函数时多了一次引用)
    b = Student()
    b.eat('banana')
    print(type(Person))
    ab().eat()
    # 类的继承执行顺序, C3算法(merge)
    print(ab.__mro__)
    se_a8 = a8.__mro__ # 84526731(object)
    print('a8-sequence:')
    for x in se_a8:
        print('    ' + str(x)) 

def main02():
    print('*****main02*****')
    p1 = Picture()
    p2 = Picture()
    print('p1:%s,p2:%s' %(id(p1), id(p2)))

# 单例对象d的一种实现(节省内存)
class Configue(object):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Configue, cls).__new__(cls, *args, **kwargs)
        return cls.__instance
        
def main03():
    print('*****main03*****')
    c1 = Configue()
    c2 = Configue()
    print('p1:%s,p2:%s' %(id(c1), id(c2)))

if __name__ == '__main__':
    main01()
    main02()
    main03()

    
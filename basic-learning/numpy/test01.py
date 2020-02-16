##########################
# author:     banbao     #
# language:   python     #
# encoding:   utf-8      #
##########################

# numpy, ndarray

import numpy as np # 引入 numpy 库(使用别名 np )

# ndarray
# retrun a**pa + b**pb
def test01(len, a, pa, b, pb):
    na = np.array(a)
    nb = np.array(b)
    return na**pa + nb**pb

# ndarray 属性
    # axis(轴) ：保存数据的维度
    # rank(秩) ：轴的数量
def test02():
    a = np.array([[1,2,3,4,5], [5,4,3,2,1]])
    print('a.ndim:', a.ndim)             # ndim(秩)
    print('a.shape', a.shape)            # shape(尺度)
    print('a.size:', a.size)             # size(元素个数)
    print('a.dtype:', a.dtype)           # dtype(元素类型)
    print('a.itemsize:', a.itemsize)     # itemsize(每个元素大小)
    # output
    '''
    a.ndim: 2
    a.shape (2, 5)
    a.size: 10
    a.dtype: int32
    a.itemsize: 4
    '''

def test03():
    a = np.array([[1,2,3,4,5], [5,4,3,2]])
    print('a.ndim:', a.ndim)             # ndim(秩)
    print('a.shape', a.shape)            # shape(尺度)
    print('a.size:', a.size)             # size(元素个数)
    print('a.dtype:', a.dtype)           # dtype(元素类型)
    print('a.itemsize:', a.itemsize)     # itemsize(每个元素大小)
    # output
    '''
    a.ndim: 1
    a.shape (2,)
    a.size: 2
    a.dtype: object
    a.itemsize: 8
    '''

# ndarray 数组的创建
def test04():
    # tuple/list
    a = np.array((1, 2), dtype = np.complex64)
    b = np.array([1, 2])
    print('a:tuple:', a)
    print('b:list:', b)
    #函数
    c = np.arange(10)                 # np.arange(n)
    print('c:arange(10):', c)
    d = np.ones((1, 2))               # np.ones(shape)
    print('d:np.ones(10):', d)
    # zeros()
    e = np.full((2,3), 10)            # np.full(shape, val)
    print('e:np.full((2, 3), 10):\n', e)
    f = np.eye(10)                    # np.eye(n)
    print('f:np.eye(10):\n', f)         # n*n 0-1矩阵, 只有对角元为1

    # 根据给定数组的形状生成一个其他数组
    g = np.ones_like(f)               # np.ones_like(array)
    print('g:np.ones_like(f):\n', g)
    # np.zeros_like(array)
    # np.full_like(array, val)

    # 其他函数
    h = np.linspace(1, 100, 4, endpoint = False)         # np.linspace(start, end, num)
    print('np.linspace(1, 100, 4):', h)

# 对ndarray数组的变换
# 维度变换/类型转换
def test05():
    # 维度变换
    a = np.array([[0,1,2],[3,4,5]], dtype=int)
    print(a)
    
    # reshape/resize, 变换维度
    # reshape(shape):不修改原数组,返回修改后的数组
    b = a.reshape((3,2)) # 元素个数要相同
    print('reshape:\na:\n{}\nb:\n{}'.format(a, b))
    
    # resize(shape):修改原数组, 返回None
    c = a.resize((3,2)) # 元素个数要相同
    print('resize:\na:\n{}\nc:\n{}'.format(a, c))
    a.resize((2,3))
    
    # swapaxes(ax1, ax2), 将n个维度中的两个维度进行调换(不修改原数组)
    d = a.swapaxes(0, 1)
    print('swapaxes:\na:\n', a, '\nc:\n', d)
    
    # fllatten(), 降成1维, 不修改原数组
    e = a.flatten()
    print('fllaten:e:\n',e)
    
    # 类型转换
    # astype, 不修改原数组, 可以用来做拷贝
    f = a.astype(complex)
    print('astype:a\n', a, '\nf:\n', f)

# tolist()
def test06():
    a = np.ones((2, 3))
    print(a.tolist())
    pass

# 一维数组索引与切片
def test07():
    # 一维数组的索引与切片与list类似
    la = [0,1,2,3,4]
    a = np.array(la)
        # [] 下标索引
    for i in range(1, len(a)):
        print(a[i])
        # 切片
    print(a[1:4:2]) #[start,end,step]
    
# 多维数组的索引和切片
def test08():
    # 多维度
    a = np.arange(24).reshape((2,3,4))
    print(a)
    # 索引
    print(a[1,1,2]) #类似于C数组
    print(a[-1,-1,-1])
    # 切片
    print(a[0:1,1:3:1,-1:-2:-1]) # ,
 
# ndarray数组的运算(一元函数)
def test09():
    a = np.arange(0,10)
    # 平均值
    print(np.mean(a))
    # 乘一个标量
    print(a*8)
    print(a-5)
    
    # 一元数学函数
    print(np.abs(a-5))
    # abs()/fabs()
    # sqrt()
    # square()
    # log(), log10(), log2()
    # ceil(), floor()
    # rint()    # 四舍五入
    # modf()    # 整数部分和小数部分分为两个数组返回
    print(np.modf(a/7))
    # cos(), sin(), tan()       # 三角函数
    # cosh(), sinh(), tanh()    # 双曲函数
    # exp()
    # sign()    # 符号
    print(np.sign(a-5))

# ndarray数组的运算(二元/多元函数)
def test10():
    # 二元函数
    a = np.arange(10)
    b = np.full(10, 7)
    print('a:',a,'\nb:',b)
    # +,-,/,*,**
    print('a*b:',a*b)
    
    # 其他函数
    # mod
    print('a mod b:', np.mod(a, b))
    # maximun(), fmax()
    # minimun(), fmin()
    # copysign(x, y), 复制符号y到x
    print('np.copysign(b,a-5):' ,np.copysign(b,a-5))
    # <,>,<=,>=,==,!= ,产生bool数组
    
    
def main01():
    # python 本身支持复数类型
    ai = 1 + 2j
    bi = 3.1 + 6j
    print(ai + bi)
    # output : (4.1+8j)

    ## 从 list 构造 ndarray
    a = [1, 2, 3, 4]
    b = [0, 1, 2, 3]
    print(test01(len(a), a, 2, b, 3))
    # output : [ 1  5 17 43]

    # ndarray 元素类型
        # bool
        # intc(c:int)
        # intp(c:ssize_t)
        # 有符号 : int8, int16, int32, int64
        # 无符号 : uint8, uint16, uint32, uint64
        # float(16,32,64)
        # 复数形式 : complex(64,128)
    # 复数形式
    b = np.array([1,2], dtype = complex)
    print(b)
    # output : [1.+0.j 2.+0.j]

def main02():
    # test02()
    # test03()
    # test04()
    # test05()
    # test06()
    # test07()
    # test08()
    # test09()
    test10()
    pass


if __name__ == '__main__':
    # main01()
    main02()

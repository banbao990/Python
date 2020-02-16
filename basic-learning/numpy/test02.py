##########################
# author:     banbao     #
# language:   python     #
# encoding:   utf-8      #
##########################

# numpy(csv, )
import numpy as np

# csv 只能有效存储一维和二维数组
# csv 文件的存储
def test01():
    a = np.arange(100).reshape(5, 20)
    np.savetxt('./a.gz', a, fmt='%d', delimiter=',')

# csv 文件的读取
def test02():
    # np.loadtxt(frame(file), dtype = np.float, delimiter = None, unpack = False)
    a = np.loadtxt('./a.gz', dtype = np.int, delimiter = ',')
    print(a)

# 多维数据的存取
def test03():
    # nparray.tofile(frame, sep='', forat='%s')
    

def main01():
    # test01()
    # test02()

if __name__ == '__main__':
    main01()

 
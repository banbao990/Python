##########################
# author:     banbao     #
# language:   python     #
# encoding:   utf-8      #
##########################

# 文件操作

# 文件操作
    # 打开文件
    # r/w/a
    # rb/wb/ab      二进制方式
    # 读写
        # r+(覆盖内容)
            # 直接写覆盖, 先读后写append
        # w+(覆盖文件)
        # a+
    # rb+/wb+/ab+
f1 = open('./test.txt', 'r+')
# line = f1.read()          # 读取所有的数据
# line = f1.read(5)         # 读取 5 个字节
# line = f1.readline()      # 读一行
#######
'''
lines = f1.readlines()      # 一行一行全读出来
for line in lines:
    print(line, end = '')   # 不换行输出
'''
#######
'''
for line in f1:             # 一行一行全读出来
    print(line, end = '')   # 不换行输出
'''

# f1.write('hello')         # 不换行
# f1.writelines(['hello', 'world']) # 不换行
# f1.tell()                 # 输出当前指针位置

# 定位到某个位置
# f1.seek(from, offset)
    # from:     0(开头), 1(当前位置), 2(最后)
    # offset:   偏移量

    # 关闭文件
f1.close()


# 异常形式
f1 = open('./test.txt', 'r+')
try:
    # code
finally:
    f1.close()

# with, 上下文管理器
with open('./test.txt', 'r+') as f1:
    # code





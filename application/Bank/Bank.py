##########################
# author:     banbao     #
# language:   python     #
# encoding:   utf-8      #
##########################

# 简易银行

from pathlib import Path    # 文件
import random               # 随机数
import re                   # 正则表达式匹配

# 账户(Account)类
class Account(object):
    # 受保护的属性或者方法, 使用一个下划线开头(外界能够调用)
    # 私有属性或者方法使用两个下划线开头(外界不能调用)

    # 构造函数
    def __init__(self, name, password, money = 0):
        self.username = name
        self.__money = int(money)   # 输入全部都是字符串
        # 有密码则无需设置密码
        if password != None:
            # 如果不加这一句, 则没有属性 __password, 区别于 C++
            self.__password = password
            return
        # 设置密码
        self.setPassword()
        print('Your password has been set successfully!')

    # 获取余额
    def getMoney(self):
        return self.__money

    # 获取密码
    def getPassword(self):
        return self.__password

    # 设置密码
    def setPassword(self, isReset = 0):
        while True:
            # 输入密码两次
            pwd1 = input('Please set your password!\n')
            # 输入密码不能含有空白字符
            if re.match('.*\s.*', pwd1) != None:
                print('Illegal password with white space characters, try again.')
                continue
            # 修改后的密码不能与之前的相同
            if isReset == 1 and pwd1 == self.__password:
                print('The new password is the same as the old one, try another password.')
                continue
            pwd2 = input('Please input again!\n')
            if pwd1 == pwd2:
                self.__password = pwd1
                break
            else:
                print('The second input is not same as the first on, please set your password again!')

    # 修改密码
    def resetPassword(self):
        self.setPassword(1)
        print('Your password has been reset successfully!')

    # 显示余额
    def showMoneyLeft(self):
        print('\'{}\' has {} yuan in the Bank!'.format(self.username, self.__money))

    # 存款
    def saveMoney(self, money):
        self.__money += money
        print('Save {} yuan successfully!\nYou have {} yuan in the Bank!'.format(money, self.username, self.__money))

    # 取款
    def withdrawalMoney(self, money):
        if(money > self.__money):
            print('you only have {} yuan left. Failed to withdraw money.'.format(self.__money))
        else:
            self.__money -= money
            print('Withdraw {} yuan successfully! you have {} yuan left.'.format(money, self.__money))

    # 进入账户
    def work(self):
        while True:
            print('Choose your request(number is ok):')
            print('    1.Check balance.')
            print('    2.Save money.')
            print('    3.Withdrawal money')
            print('    4.Reset password')
            print('    5.Exit')
            s = input()
            if(s.isdigit() and int(s) <= 5 and int(s) >= 1):
                cmd = int(s)
                if cmd == 1:
                    self.showMoneyLeft()
                elif cmd == 4:
                    self.resetPassword()
                elif cmd == 5:
                    return
                else:
                    money = 0
                    s = input('How much?\n')
                    if(s.isdigit()):
                        money = int(s)
                        if cmd == 2:
                            self.saveMoney(money)
                        elif cmd == 3:
                            self.withdrawalMoney(money)
                    else:
                        print('Input is not a number')

    # 析构函数
    def __del__(self):
        pass

# 银行类(Bank)
class Bank(object):
    # 构造函数
    def __init__(self, name):
        self.name = name
        print('Welcome to %s!' %name)
        # 账户存档, 存在一个文件'account'里
        self.account = {}
        # 判断文件是否存在
        my_file = Path('./account')
        if my_file.is_file():
            # 触发异常, 文件会自己关闭
            with open('./account', 'r') as f:
                for line in f:
                    (username, password, money) = line.strip().split()
                    self.account[username] = Account(username, password, money)
        else:
            pass

    # 银行开工
    def open(self):
        # 死循环, 一直执行
        while True:
            print('please input your request(number is ok):')
            print('    1.open an account')
            print('    2.sign in')
            print('    3.close an account')
            print('    4.leave')
            s = input()
            if(s.isdigit() and int(s) <= 4 and int(s) >= 1):
                cmd = int(s)
                if cmd == 1:
                    self.openAccount()
                elif cmd == 2:
                    self.signIn()
                elif cmd == 3:
                    self.closeAccount()
                else:
                    return
            else:
                print('bad input, try again.')

    # 开户
    def openAccount(self):
        username = ''
        # 判断用户名是否合法(一个新账户+不含空白字符)
        while True:
            username = input('Please input your username:\n')
            if(username in self.account.keys()):
                # 推荐加上随机数后缀
                # zfill 是 str 的函数
                tail = str(random.randint(0,999)).zfill(3)
                print('\'{}\' is already in the Bank, try \'{}\'?'.format(username, username + tail))
            elif re.match('.*\s.*', username) != None:
                print('illegel username with white space characters, try again.')
            else:
                break
        self.account[username] = Account(username, None, 0)

    # 辅助函数
    def help01(self, msg, isSignIn = True):
        username = input('Please input your username.\n')
        if username in self.account.keys():
            password = (self.account[username]).getPassword()
            # 3 次输密码的机会
            left = 3
            while left > 0:
                pwd = input('Input your password(You have {} chances left).\n'.format(left))
                if pwd == password:
                    if isSignIn:
                        self.account[username].work()
                    else:
                        self.account.pop(username)
                        print('Your account \'%s\' has been closed successfully!' %username)
                    return
                else:
                    left -= 1
            print('Your have lost all 3 chances, failing to {}.'.format(msg))
        else:
            print('There is no account named %s' %username)

    # 登录 # 调用辅助函数(help01)
    def signIn(self):
        self.help01('sign in', True)

    # 销户 # 调用辅助函数(help01)
    def closeAccount(self):
        self.help01('close account', False)

    # 析构函数
    def __del__(self):
        print('Thanks and look farwad your coming next time!')
        # 账户存档
        with open('./account', 'w') as f:
            for account in self.account.values():
                f.write('%s %s %s\n' %(account.username, account.getPassword(), account.getMoney()))

# main 函数
def main():
    bank = Bank('BANBAO\' BANK')
    bank.open()

# main 函数入口
if __name__ == '__main__':
    main()
# 使用%*格式化
def format_str():
    # 格式化字符串方法一
    name = 'amosniu'
    print('欢迎您：%s' %name)
    # 格式化字符串方法二
    print('欢迎您：%(name)s' %{'name':name})

    # 格式化整型
    number = 888
    print('您打印的整数是：%d' %number)

    # 格式化浮点数
    number2 = 3.1415926
    print('您打印的浮点数是：%.7f' %number2)

    # 格式化数组
    t = (1,3,5,7,9)
    print('您打印的数组是：%s' %str(t))

# 使用.format()格式化
def format_str2():
    # 用法一
    print('欢迎您，{0},{1},---{0}说'.format('amosniu','祝你学习Python顺利！'))
    # 用法二
    print('您好：{username},您的性别是：{six}'.format(username = 'amosniu',six = '男'))
    # 使用字典存储数据
    data = {
        'username':'amosniu',
        'six':'男',
        'age':24
    }
    print('您好：{username},您的性别是：{six},您的年龄是：{age}'.format(**data))
    # 格式化坐标位置(即数组)
    point = (1,0)
    print('您的坐标位置是：{0[0]}:{0[1]}'.format(point))

    # 格式化类
    user = User('amosniu',24)
    # print(user.show())
    print(user)

class User(object):
    def __init__(self,username,age):
       self.username = username
       self.age = age
    def show(self):
       return '您的名字是：{self.username},您的年龄是：{self.age}'.format(self = self)
    #通过__str__函数直接将其格式化为字符串
    def __str__(self):
        return self.show()

if __name__ == '__main__':
    format_str()
    format_str2()

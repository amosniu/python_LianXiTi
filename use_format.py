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
    print('欢迎您，{0},{1}'.format('amosniu','祝你学习Python顺利！'))

if __name__ == '__main__':
    format_str()
    format_str2()

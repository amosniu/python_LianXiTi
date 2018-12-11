# 迭代（非递归版本）求阶乘
def factorial(number):
    result = number
    for i in range(1,number):
        result *= i
    return result

number = int(input('请输入一个正整数：'))
result = factorial(number)
print('%d的阶乘是:%d' %(number,result))


# 递归版本求阶乘
def factorial2(number2):
    if number2 == 1:
        return 1
    else:
        return number2 * factorial2(number2 - 1)
number2 = int(input('请输入一个正整数：'))
result2 = factorial2(number2)
print('%d的阶乘是：%d' %(number2,result2))

# 迭代（非递归版本）（这帮小兔崽子）
def factorial3(number3):
    n1 = 1
    n2 = 1
    n3 = 1

    if number3 < 1:
        print('请输入正整数！')

    while(number3 - 2) > 0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        number3 -= 1

    return n3

number3 = int(input("请输入一个正整数："))
result3 = factorial3(number3)
if result3 != -1:
    print('%d个月时共有兔子%d对' %(number3,result3))

# 递归版本（这帮小兔崽子）
def factorial4(number4):
    if number4 < 1:
        return -1
    if number4 == 1 or number4 == 2:
        return 1
    else:
        return factorial4(number4-1)+factorial4(number4-2)

number4 = int(input("请输入一个正整数："))
result4 = factorial4(number4)
if result4 != -1:
    print('%d个月时共有兔子%d对' %(number4,result4))
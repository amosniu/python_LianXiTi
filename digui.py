# 非递归版本求阶乘
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
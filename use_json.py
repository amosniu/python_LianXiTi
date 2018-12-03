import json

def pythonToJson():
    ''' 将python数据转化成json数据 '''
    d = {
        'name': 'python书籍',
        'price': 62.3
    }
    jsonData = json.dumps(d)
    print(jsonData)

if __name__ == '__main__':
    pythonToJson()
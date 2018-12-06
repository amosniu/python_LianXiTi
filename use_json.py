import json

def pythonToJson():
    ''' 将python数据转化成json数据 '''
    d = {
        'name': 'python书籍',
        'price': 62.3
    }
    # indent参数用来给输出结果缩进
    jsonData = json.dumps(d,indent = 4)
    print(jsonData)

def jsonToPython():
    ''' 将json数据转化成python数据 '''
    jsonData = '''
    {
    "name": "Python书籍",
    "origin_price": 66,
    "pub_date": "2018-4-14 17:00:00",
    "store": ["京东", "淘宝"],
    "author": ["张三", "李四", "Jhone"],
    "is_valid": true,
    "is_sale": false,
    "meta": {
        "isbn": "abc-123",
        "pages": 300
    },
    "desc": null
    }
    '''
    pythonData = json.loads(jsonData)
    print(type(pythonData))
    print(pythonData)

def jsonToPythonFromFile():
    ''' 从文件中读取json数据，并转化成Python数据 '''
    f = open('./static/book.json','r',encoding = 'utf-8')
    s = f.read()
    pythonData = json.loads(s)
    print(type(pythonData))
    print(pythonData)
    print(pythonData['name'])

if __name__ == '__main__':
    pythonToJson()
    print('---------------------------')
    jsonToPython()
    print('---------------------------')
    jsonToPythonFromFile()
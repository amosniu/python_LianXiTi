import json

def pythonToJson():
    ''' 将python数据转化成json数据 '''
    d = {
        'name': 'python书籍',
        'price': 62.3
    }
    jsonData = json.dumps(d)
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
    print(pythonData)

if __name__ == '__main__':
    pythonToJson()
    print('---------------------------')
    jsonToPython()
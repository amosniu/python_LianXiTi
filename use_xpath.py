from lxml import html

def parse():
    ''' 将html文件中的内容，使用xpath进行读取 '''
    # 读取文件中的内容
    f = open('./static/index.html','r',encoding = 'utf-8')
    s= f.read()

    #将读取出的内容输出为字符串
    selector = html.fromstring(s)

    # 解析H3标题
    h3 = selector.xpath('/html/body/h3/text()')
    print(h3[0])

    # 解析ul下的内容
    ul = selector.xpath('/html/body/ul/li')
    print(len(ul))
    for li in ul:
        print(li.xpath('text()'))

    # 解析ul下指定的属性值
    ul2 = selector.xpath('/html/body/ul/li[@class = "important"]/text()')
    print(ul2[0])

    # 解析a标签的内容
    a = selector.xpath('//div[@id = "container"]/a/text()')
    print(a)
    # 解析a标签下的helf值
    href = selector.xpath('//div[@id = "container"]/a/@href')
    print(href)

    f.close()

if __name__ == '__main__':
    parse()
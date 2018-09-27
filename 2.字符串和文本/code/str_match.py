import re
from urllib.request import urlopen


# 字符串开头形式判断
url = 'http://www.python.org'
print(url.startswith('http'))       # True
print(url.startswith('www', 7), url[7:])     # True www.python.org
print(url.startswith('/', 5, 6), url[5:6])   # True /

# 字符串结尾形式判断
filename = 'spam.txt'
print(filename.endswith('.txt'))    # True
print(filename.endswith('.txt', 0, 10), filename[:10])     # True spam.txt
print(filename.endswith('.t', 0, 6), filename[:6])     # True spam.t

filename = 'test.py'    # 允许元组形式作为匹配参数
print(filename.endswith(('.txt, ', '.py')))     # True


def exist_py_script(filenames):
    """ 文件名列表中，存在python脚本文件，返回True，否则，返回False """
    if any(file_name.endswith('.py') for file_name in filenames):
        return True
    return False


def read_data(name):
    """ 访问正确格式的url链接 """
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


# re模块匹配开头或结尾
s = 'abc.py'
result = re.match(r'^abc', s)
print(result.group() if result is not None else result)     # abc

s = 'test.py'
result = re.match(r'^abc', s)       # 没有匹配到指定格式的开头
print(result.group() if result is not None else result)     # None

s = 'abc.py'
result = re.search(r'\.py$', s)
print(result.group() if result is not None else result)     # .py

s = 'abc.txt'
result = re.search(r'\.py$', s)     # 没有查找到指定格式的结尾
print(result.group() if result is not None else result)     # None

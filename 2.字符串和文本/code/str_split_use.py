import re


s = 'a b; c, d,e, f'

# 字符串空格分割
print(s.split(' '))         # ['a', 'b;', 'c,', 'd,e,', 'f']
print(s.split(' ', maxsplit=3))     # ['a', 'b;', 'c,', 'd,e, f']，最大分割3次

# 正则匹配模式分割
result = re.split(r'[\s|,|;]\s*', s)    # 正则模式：一个 (空字符串/逗号/分号) + 0或多个 (空字符串)
print(result)       # ['a', 'b', 'c', 'd', 'e', 'f']

result = re.split(r'(\s|,|;)\s*', s)    # 带子组捕获，结果列表中包含捕获到的子组 分割符
print(result)       # ['a', ' ', 'b', ';', 'c', ',', 'd', ',', 'e', ',', 'f']

# 从结果中分分离出分割结果字符和它们之间的分割符
print(result[::2])      # ['a', 'b', 'c', 'd', 'e', 'f']
print(result[1::2])     # [' ', ';', ',', ',', ',']

# 重新组合，使用捕获到的子组字符串作为分隔符，即修改分隔符为单个分割字符
print(''.join(k+v for k,v in zip(result[::2], result[1::2])))   # a b;c,d,e,

result = re.split(r'(?:\s|,|;)\s*', s)  # 非捕获分组，形如(?:...)，不会被作为子组捕获
print(result)       # ['a', 'b', 'c', 'd', 'e', 'f']


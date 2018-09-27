import re


# 1. str.replace 返回一个等同于原字符串的新字符串，并替换对应的子字符串
text = 'yeah, but no, but yeah, but no, but yeah'
print(text)     # yeah, but no, but yeah, but no, but yeah
print(text.replace('yeah', 'yep'))  # yep, but no, but yep, but no, but yep
print(text.replace('yeah', 'yep', 1))  # yep, but no, but yeah, but no, but yeah
print(20*'* ')

# 2. re.sub 和 re.subn
text1 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
regex_pat = re.compile(r'(\d+)/(\d+)/(\d+)')
# 第二个参数 repl 是一个字符串
result = regex_pat.sub(r'(\1)-(\2)-(\3)', text1)
print(result)       # Today is (11)-(27)-(2012). PyCon starts (3)-(13)-(2013).

result = regex_pat.subn(r'(\1)-(\2)-(\3)', text1)
print(result)       # ('Today is (11)-(27)-(2012). PyCon starts (3)-(13)-(2013).', 2)

# 第二个参数 repl 是一个 callable
change_date = lambda m: '({})-({})-({})'.format(m.group(1), m.group(2), m.group(3))
result = regex_pat.sub(change_date, text1)
print(result)       # Today is (11)-(27)-(2012). PyCon starts (3)-(13)-(2013).



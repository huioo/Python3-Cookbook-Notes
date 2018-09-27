import re


text = 'yeah, but no, but yeah, but no, but yeah'
# 1. 字符串字面处理
print('[text]', text)
print("text == 'yeah'", text == 'yeah')     # False
print("text.startswith('yeah')", text.startswith('yeah'))     # True
print("text.endswith('no')", text.endswith('no'))     # False
print("text.find('no')", text.find('no'))     # 10
print(20*'* ')


text1 = '11/27/2012 CST 12/01/2012 CST'
text2 = 'Nov 27, 2012'
# 2. re.match / pat.match
match_result = re.match(r'(\d+)/(\d+)/(\d+)', text1)
print("[text1]", text1)
print("re.match(r'(\d+)/(\d+)/(\d+)', text1).group()", match_result.group())    # 11/27/2012
print("re.match(r'(\d+)/(\d+)/(\d+)', text1).group(0)", match_result.group(0))    # 11/27/2012
print("re.match(r'(\d+)/(\d+)/(\d+)', text1).group(1)", match_result.group(1))    # 11
print("re.match(r'(\d+)/(\d+)/(\d+)', text1).group(2)", match_result.group(2))    # 27
print("re.match(r'(\d+)/(\d+)/(\d+)', text1).group(3)", match_result.group(3))    # 2012
print("re.match(r'(\d+)/(\d+)/(\d+)', text1).groups()", match_result.groups())    # ('11', '27', '2012')
print()


# 3. re.compile
print("[text2]", text2)
# 使用同一个模式去做多次匹配，你应该先将模式字符串预编译为模式对象。
regex_pat = re.compile(r'\d+/\d+/\d+')  # re.compile('\\d+/\\d+/\\d+')
print("[regex_pat]", regex_pat)
match_result = regex_pat.match(text2)
print("regex_pat.match(text2)", match_result)    # None
print(20*'* ')


# 3. re.findall / pat.findall
text3 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# findall() 方法会搜索文本并以列表形式返回所有的匹配
regex_pat = re.compile(r'(\d+)/(\d+)/(\d+)')  # re.compile('\\d+/\\d+/\\d+')
result = regex_pat.findall(text3)
print("[text3]", text3)
print("[regex_pat]", regex_pat)     # re.compile('(\\d+)/(\\d+)/(\\d+)')
print("regex_pat.findall(text3)", result)     # [('11', '27', '2012'), ('3', '13', '2013')]
comment = "带子组的pattern，列表的元素是捕获的子组内容，其形式为 tuple"
print(comment)
print()

regex_pat = re.compile(r'\d+/\d+/\d+')  # re.compile('\\d+/\\d+/\\d+')
result = regex_pat.findall(text3)
print("[regex_pat]", regex_pat)
print("regex_pat.findall(text3)", result)     # ['11/27/2012', '3/13/2013']
print(20*'* ')


# 4. re.finditer / pat.finditer
# 以迭代方式返回匹配结果，返回多个匹配对象
regex_pat = re.compile(r'(\d+)/(\d+)/(\d+)')  # re.compile('\\d+/\\d+/\\d+')
result = regex_pat.finditer(text3)
print("[regex_pat]", regex_pat)
print("regex_pat.finditer(text3)", result)     # <callable_iterator object at 0x0000021D88E9A550>
for match_obj in result:
    print('  ', match_obj)
    print('  ', match_obj.group())
    print('  ', match_obj.groups())
    print()
"""
   <_sre.SRE_Match object; span=(9, 19), match='11/27/2012'>
   11/27/2012
   ('11', '27', '2012')

   <_sre.SRE_Match object; span=(34, 43), match='3/13/2013'>
   3/13/2013
   ('3', '13', '2013')
"""

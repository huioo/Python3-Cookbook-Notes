# 1. 使用多个界定符分割字符串

分割字符串，返回结果为`list`形式：
- `string`对象的`split()`方法：适用简单的字符分割，不允许多个分隔符或者分隔符周围有不确定的空格。  
  > `str.split(self, sep=None, maxsplit=-1)`：  
  `sep`为固定的分隔字符串，`maxsplit`指最大分割次数。

- `re`模块的`split()`方法：按照正则模式的分隔符进行分割。  
  > `re.split(pattern, string, maxsplit=0, flags=0)`：  
  `pattern`指正则匹配的分割字符串的正则表达式，`string`指需要分割字符串

参考示例 [code/str_split_use.py](#code/str_split_use.py)


# 2. 字符串开头或结尾匹配

匹配字符串的开头或结尾，判断是否为某种形式。
- `string`对象的`startswith()`和`endswith()`方法：  
  > `str.startswith(self, prefix, start=None, end=None)`：   
  > `prefix`指匹配的特定前缀，`start`和`end`指匹配范围
  >
  > `str.endswith(self, suffix, start=None, end=None)`：  
  > `suffix`指匹配的特定后缀  
  > 
  > `prefix`和`suffix`可以是单个匹配字符串或多个匹配字符串的元组形式。
  
- `re`模块的`match()`或`search()`方法：
  > `match(pattern, string, flags=0)`：  
    """Try to apply the pattern at the start of the string, returning a match object, or None if no match was found."""  
  > 从字符串的开头开始，应用`pattern`进行正则匹配
  > 
  > `search(pattern, string, flags=0)`： 
    """Scan through string looking for a match to the pattern, returning a match object, or None if no match was found."""  
  > 扫描字符串查找符合`pattern`的匹配字符串

参考示例[`code/str_match.py`](#code/str_match.py)。

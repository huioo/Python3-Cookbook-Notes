# 1. 使用多个界定符分割字符串

分割字符串，返回结果为`list`形式：
- `string`对象的`split()`方法：适用简单的字符分割，不允许多个分隔符或者分隔符周围有不确定的空格。  
  > `str.split(self, sep=None, maxsplit=-1)`：  
  `sep`为固定的分隔字符串，`maxsplit`指最大分割次数。

- `re`模块的`split()`方法：按照正则模式的分隔符进行分割。  
  > `re.split(pattern, string, maxsplit=0, flags=0)`：  
  `pattern`指正则匹配的分割字符串的正则表达式，`string`指需要分割字符串

参考示例 [code/str_split_use.py](code/str_split_use.py)


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

参考示例[`code/str_match.py`](code/str_match.py)。

# 3. 用Shell通配符匹配字符串

Unix Shell 通配符：比如 `*.py` , `Dat[0-9]*.csv` 。

 通配符  | 含义
 ---:   | :---
 *      | matches everything
 ?      | matches any single character
 [seq]  | matches any character in seq
 [!seq] | matches any char not in seq

`fnmatch`模块的`fnmatch()`和`fnmatchcase()`方法:  
- `fnmatch(name, pat)`：
  > 字符串匹配，忽略大小写
- `fnmatchcase(name, pat)`：
  > 字符串匹配，按照大小写
- `filter(names, pat)`：
  > 过滤符合匹配条件的元素
- `translate(pat)`:
  > 将shell通配符匹配字符串转转化为正则形式

参考示例[`code/fnmatch_use.py`](code/fnmatch_use.py)。

# 4. 字符串匹配和搜索

匹配字面字符串，使用`str`的`find()`、`startswith()`和`endswith()`方法：  
- `str.startswith(self, prefix, start=None, end=None)`  
- `str.endswith(self, suffix, start=None, end=None)`  
- `str.find(self, sub, start=None, end=None)`  
  > `sub`表示查找的子字符串，返回第一个查找到的子字符串位置，如果没找到，返回 -1 

匹配或者搜索特定模式的文本，使用正则表达式和 `re` 模块。
- 原始字符串：
  > 比如 `r'(\d+)/(\d+)/(\d+)'` 。  
    这种字符串将不去解析反斜杠，这在正则表达式中是很有用的。  
    如果不这样做的话，你必须使用两个反斜杠，类似 `(\\d+)/(\\d+)/(\\d+)`。

- `re.match(pattern, string, flags=0)`  
  > 从头开始应用 `pattern` 进行匹配，如果没有发现匹配，返回`None`，否则返回一个`match`对象。  
    
  - `match_obj.group()`  
    > 返回正则匹配成功的第一个字符串

  - `match_obj.groups()`
    > 返回正则匹配成功的第一个字符串中对应捕获的子组内容，以`tuple`的形式返回

- `re.compile(pattern, flags=0)`
  > 使用 re.compile() 编译正则表达式字符串， 然后使用 match() , findall() 或者 finditer() 等方法。  
    如果你打算做大量的匹配和搜索操作的话，最好先编译正则表达式，然后再重复使用它。  
    模块级别的函数会将最近编译过的模式缓存起来，因此并不会消耗太多的性能， 但是如果使用预编译模式的话，你将会减少查找和一些额外的处理损耗。  

- `re.findall(pattern, string, flags=0)`:
  > 搜索文本并以列表形式返回所有的匹配。 

参考示例[`code/re_match.py`](code/re_match.py)。

# 5. 字符串搜索和替换 

替换字面字符串，使用`str.replace()`直接替换特定字符串。
- `str.replace(self, old, new, count=None)`
  > 复制原字符串，并将其存在的`old`子字符串替换为`new`子字符串。  
    `count`表示替换的个数

复杂的字符串替换，使用`re`模块的`sub()`和`subn()`方法。
- `re.sub(pattern, repl, string, count=0, flags=0)`
  - `pattern`指被匹配的模式。
  - `repl`是替换模式，可以是一个字符串或一个调用对象（callable）。如果是字符串，它里面的反斜杠转义会被处理，比如`\3`指向前面模式的捕获组号。如果`repl`是一个可调用对象（callable），传给它一个`match`对象，且必须返回一个用来替换的字符串。
  - `string`是替换的字符串。
  - 结果以字符串的形式返回，其值为替换之后的新字符串。

- `re.subn(pattern, repl, string, count=0, flags=0)`
  - 等同于`re.sub()`方法，但是结果以**二元素元组**的形式（替换的新字符串, 替换的次数）返回。

参考示例[`code/re_replace.py`](code/re_replace.py)。





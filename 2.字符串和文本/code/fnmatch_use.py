from fnmatch import fnmatch, fnmatchcase, filter as _filter, translate
from functools import partial


def fnmatch_use(iterable, pat):
    """ 忽略大小写 """
    # for item in iterable:
    #     print(item, fnmatch(item, pat))
    print(list(filter(partial(fnmatch, pat=pat), iterable)))


def fnmatchcase_use(iterable, pat):
    """ 大小写匹配 """
    # for item in iterable:
    #     print(item, fnmatchcase(item, pat))
    print(list(filter(partial(fnmatchcase, pat=pat), iterable)))


def filter_use(iterable, pat):
    """ 过滤出符合 pattern 的元素 """
    print(_filter(iterable, pat))


def translate_use(pat):
    """ 将 pattern 翻译成正则表达式 """
    print(translate(pat))


if __name__ == '__main__':
    examples = ['abc.py', 'abc.txt', 'abc.js', 'ABC.py']
    pattern = '*[a-z].py'
    fnmatch_use(examples, pattern)  # ['abc.py', 'ABC.py']

    fnmatchcase_use(examples, pattern)  # ['abc.py']

    filter_use(examples, pattern)   # ['abc.py', 'ABC.py']

    translate_use(pattern)  # (?s:.*[a-z]\.py)\Z


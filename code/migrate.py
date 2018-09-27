# 文件名排序问题
"""

GitHub上文件夹及文件名顺序排列问题，'1.aaa'与'13.aaa'都在'2.aaa'之前

换文件夹及文件名字 ==》 '.' 变为 '_'
"""

import os
import re

from os.path import join, dirname, abspath


def project_location():
    """
    os.path.splitdrive(current_location)
        # ('F:', '/WorkSpace/PyCharm/Python3-Cookbook-Notes/code')
        
    os.path.split(current_location)
        # ('F:/WorkSpace/PyCharm/Python3-Cookbook-Notes', 'code')
        
    os.path.splitext(__file__)
        # ('F:/WorkSpace/PyCharm/Python3-Cookbook-Notes/code/migrate', '.py')
    :return:
    """
    current_location = dirname(abspath(__file__))
    return os.path.split(current_location)[0]
    

def findfile(start, name):
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = join(start, relpath, name)
            print(os.path.normpath(os.path.abspath(full_path)))


def func1(root):
    need_change = []
    for dir_path, dir_names, file_names in os.walk(root):
        if any(path.startswith('.') for path in dir_path.split('\\')):
            continue
        print(dir_path, dir_names)
        # if '.' in dirpath:
        #     need_change.append(dirname)
        #     os.rename(dirpath.replace('.', '_'))
        # if '.' in dirpath:
        #     os.rename(dirpath.replace('.', '_'))


if __name__ == '__main__':
    root = project_location()
    print(root)
    print(os.listdir(root))
    for path in os.listdir(root):
        if re.match(r'^\d+\.', path) is None:
            continue
        print(path)
        os.rename(join(root, path), join(root, path.replace('.', '_')))






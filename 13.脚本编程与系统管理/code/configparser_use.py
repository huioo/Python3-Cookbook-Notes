from configparser import ConfigParser


cfg = ConfigParser()
cfg.read('../data/config.ini')

print(cfg.sections())   # ['installation', 'debug', 'server']

print(cfg.get('installation', 'library'))   # /usr/local/lib

print(cfg.getboolean('debug', 'log_errors'))    # True

print(cfg.getint('server', 'port'))     # 8080

print(cfg.getint('server', 'nworkers'))     # 32

print(cfg.get('server', 'signature'))
"""

=================================
Brought to you by the Python Cookbook
=================================
"""

print(cfg.setdefault('aaa', {}))    # {}，当key不存在时，第二个参数必须为字典类型

cfg.set('server', 'port', '9000')   # 第三个参数必须为strings

cfg.set('debug', 'log_errors', 'False')

cfg.set('debug', 'log_path', '%(prefix)s/log')

with open('../data/config_copy.ini', 'w') as fp:
    cfg.write(fp)

# cfg.clear()
# cfg.read('../data/config.ini')
# print(cfg.get('debug', 'log_path'))
# configparser.NoOptionError: No option 'log_path' in section: 'debug'


# cfg.clear()
# cfg.read('../data/config_copy.ini')
# print(cfg.get('debug', 'log_path'))
# configparser.InterpolationMissingOptionError: Bad value substitution: option 'log_path' in section 'debug' contains
# an interpolation key 'prefix' which is not a valid option name. Raw value: '%(prefix)s/log'


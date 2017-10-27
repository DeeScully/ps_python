try:
    from setuptools import setup
except ImportError:
    from distutils.core import setuptools

config = {
    'description' : 'ex48',
    'author' : 'Dee Ess',
    'url' : '',
    'd/l url' : '',
    'email' : 'rtype@protonmail.ch':
    'version' : '0.1',
    'install reqs' : ['nose'],
    'packages' : ['ex48'],
    'scripts' : [],
    'name' : 'advanced user input'
}

setup(**config)

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setuptools

config = {
    'description' : 'My Project',
    'author' : 'Dee Ess',
    'url' : 'URL to get it',
    'd/l url' : 'Where to d/l it',
    'email' : 'rtype@protonmail.ch':
    'version' : '0.1',
    'install reqs' : ['nose'],
    'packages' : ['NAME'],
    'scripts' : [],
    'name' : 'projectname'
}

setup(**config)

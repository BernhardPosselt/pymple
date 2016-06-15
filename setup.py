from setuptools import setup, find_packages
from sys import exit, version_info
from platform import python_version

if version_info < (3, 4):
    print('Error: Python 3.4 required but found %s' % python_version())
    exit(1)

if version_info < (3, 5):
    install_requires = ['typing']
else:
    install_requires = []

with open('README.rst', 'r') as infile:
    long_description = infile.read()

setup (
    name = 'pymple',
    version = '0.1.0',
    description = 'A simple Inversion of Control container',
    long_description = long_description,
    author = 'Bernhard Posselt',
    author_email = 'dev@bernhard-posselt.com',
    url = 'https://github.com/Raydiation/pymple',
    install_requires = install_requires,
    packages = find_packages(exclude=('tests',)),
    license = 'GPL',
    keywords = ['pymple', 'ioc', 'inversion of control', 'container', 'dependency injection'],
    test_suite = 'tests',
)

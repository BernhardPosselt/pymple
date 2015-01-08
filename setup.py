from setuptools import setup, find_packages

with open('README.rst', 'r') as infile:
    long_description = infile.read()

setup (
    name = 'pymple',
    version = '0.0.4',
    description = 'A simple Inversion of Control container',
    long_description = long_description,
    author = 'Bernhard Posselt',
    author_email = 'dev@bernhard-posselt.com',
    url = 'https://github.com/Raydiation/pymple',
    packages = find_packages(exclude=('tests',)),
    license = 'GPL',
    keywords = ['pymple', 'ioc', 'inversion of control', 'container', 'dependency injection'],
    test_suite = 'tests',
)

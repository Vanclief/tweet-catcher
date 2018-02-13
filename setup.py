# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='tweet-catcher',
    version='1.0.0',
    description='A Python utility for collecting tweets in a time series database',
    long_description=readme,
    author='Franco Valencia',
    author_email='franco.avalencia@gmail.com',
    url='https://github.com/Vanclief/tweet-catcher',
    license=license,
    packages=find_packages(exclude=('tests'))
)

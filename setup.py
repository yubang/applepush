# coding:UTF-8


from setuptools import setup, find_packages

setup(
    name='applepush',
    version='0.0.1',
    description='一个基于python2和http2的苹果推送SDK',
    author='yubang',
    author_email='yubang93@gmail.com',
    url='https://github.com/yubang/applepush',
    packages=find_packages(),
    install_requires=['hyper', ],
)

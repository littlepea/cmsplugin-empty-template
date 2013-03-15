#!/usr/bin/env python
import os

from setuptools import find_packages, setup

README = open('README.rst').read()

setup(
    name='cmsplugin-',
    version=__import__('cmsplugin_').__version__,
    author='...',
    author_email='...@gmail.com',
    description = ('django-cms plugin template to quickly create your own custom plugins.'),
    long_description = README,
    license = "BSD",
    url = "https://github.com/.../cmsplugin-",
    packages=find_packages(),
    provides=['cmsplugin_', ],
    include_package_data=True,
    install_requires = [
        'django-sekizai',
    ],
)

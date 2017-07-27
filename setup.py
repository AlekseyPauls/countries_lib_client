# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='countries_lib_client',
    version='1.0',
    include_package_data=True,
    packages=find_packages(),
    test_suite='tests.py',
    install_requires=[
        'requests',
        'json'
    ]
)

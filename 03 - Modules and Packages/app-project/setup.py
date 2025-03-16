# setup.py

import os
from setuptools import setup, find_packages

setup(
    name='app',
    author='Nicolas Marois',
    author_email='...@gmail.com',
    maintainer='Nicolas Marois',
    packages=find_packages(),
    scripts=['main.py'],
    package_data={'app':
                      ['data/*']}
)

""" Install
"""
from setuptools import setup, find_packages
import os, sys

PACKAGE_NAME = "xlsserver"
PACKAGE_VERSION = "1.0"
SUMMARY = (
    "Simple Server HTTP for reading *.xls and *.xlsx files. "
)
DESCRIPTION = (
    open("README.rst", 'r').read() + '\n\n' +
    open('HISTORY.rst', 'r').read()
)

setup(name=PACKAGE_NAME,
      version=PACKAGE_VERSION,
      description=SUMMARY,
      long_description=DESCRIPTION,
      author='Catalin Mititiuc',
      author_email='mititiuc.cata@gmail.com',
      url='https://github.com/catalinmititiuc/SimpleServerHTTP/tree/master/HTTPServer/xlsserver',
      license='GPLv2',
      packages=find_packages(exclude=['ez_setup']),
      entry_points = {
          'console_scripts': [
              'xlserver = ilogin.ilogin3:main',
          ]},
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          "Programming Language :: Python",
          'Operating System :: OS Independent',
          'Topic :: Software Development :: Libraries :: Python Modules',
          ],
)
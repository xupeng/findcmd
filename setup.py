from setuptools import setup, find_packages
import sys, os

version = '0.1.1'

setup(name='findcmd',
      version=version,
      description="A command line tool for searching commands",
      long_description="""\
This is a simple command line tool for searching through PATHs to find out commands contain certian keywords.

Usage: findcmd [options] cmd

Options:
  -h, --help            show this help message and exit
  -c, --case-sensitive
  -e, --match-all
  --no-color

For example:
xupeng@hopes ~ $ findcmd disk
/sbin/auto**disk**mount
/sbin/**disk**label
/usr/bin/**disk**hits
/usr/sbin/**disk**arbitrationd
/usr/sbin/**disk**managementd
/usr/sbin/**disk**tool
/usr/sbin/**disk**util
/usr/sbin/f**disk**
/usr/sbin/p**disk**
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='console command sysutils',
      author='Xupeng Yun',
      author_email='xupeng@xupeng.me',
      url='https://github.com/xupeng/findcmd',
      license='Apache-2.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points={
          'console_scripts': [
              'findcmd = findcmd.findcmd:main',
          ]
      },
      )

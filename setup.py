from setuptools import setup, find_packages
import sys, os

ROOT = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(ROOT, 'README')).read()

version = '0.1.1'

setup(name='findcmd',
      version=version,
      description="A command line tool for searching commands",
      long_description=README,
      classifiers=[
          'Environment :: Console',
          'Operating System :: MacOS',
          'Operating System :: POSIX :: Linux',
          'Operating System :: POSIX :: BSD',
          'Operating System :: Unix',
          'Programming Language :: Python',
          'Topic :: System :: Systems Administration',
          'Topic :: Utilities',
      ],
      keywords='console sysutils',
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

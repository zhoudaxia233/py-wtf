import os
import sys
from setuptools import setup

version = '0.0.1'

# "setup.py publish" shortcut.
if sys.argv[-1] == 'publish':
    os.system('python3 setup.py sdist')
    os.system('twine upload dist/*')
    sys.exit()

setup(
    name='pywtf',
    version=version,
    description="A static analyzer of Python which forces you to write comments, and write them in a well-mannered way.",
    keywords='static-analyzer',
    author='Zheng Zhou',
    author_email='yootaoo@gmail.com',
    url='https://github.com/zhoudaxia233/pywtf',
    license='MIT',
    packages=['pywtf'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    dependency_links=[],
    entry_points={
        'console_scripts': [
          'wtf=pywtf.main:main',
      ]
    }

)

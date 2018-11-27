import os
import sys
import io
import re
import pywtf
from setuptools import setup


# "setup.py publish" shortcut.
if sys.argv[-1] == 'publish':
    os.system('python3 setup.py sdist')
    os.system('twine upload dist/*')
    os.system('rm -rf dist py_wtf.egg-info')
    sys.exit()

setup(
    name='py-wtf',
    version=pywtf.__version__,
    description="A static analyzer of Python which forces you to write comments, and write them in a well-mannered way.",
    keywords='static-analyzer',
    author='Zheng Zhou',
    author_email='yootaoo@gmail.com',
    url='https://github.com/zhoudaxia233/py-wtf',
    license='MIT',
    packages=['pywtf'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    python_requires='>=3.5',
    dependency_links=[],
    entry_points={
        'console_scripts': [
          'wtf=pywtf.main:main',
      ]
    }

)

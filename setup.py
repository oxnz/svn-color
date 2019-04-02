"""A svn wrapper provides colorful output

See:
    https://github.com/oxnz/svn-color
"""

import os
import codecs
import setuptools

HERE = os.path.abspath(os.path.dirname(__file__))

def readfile(fpath, encoding='utf-8'):
    if not os.path.isabs(fpath):
        fpath = os.path.join(HERE, fpath)
    with codecs.open(fpath, 'rb', encoding) as f:
        return f.read()

print(setuptools.find_packages(exclude=['contrib', 'docs', 'tests']))
setuptools.setup(
        name='svn-color',
        version='1.0.0',
        url='https://github.com/oxnz/svn-color',
        license='MIT',
        author='oxnz',
        description='Colorized svn wrapper',
        long_description=readfile('README.md'),
        packages=setuptools.find_packages(exclude=['contrib', 'docs', 'tests']),
        entry_points = {
            'console_scripts': [
                'svn-color=colorizedsvn:main',
                ],
            },
        )


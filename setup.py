#!/usr/bin/env python

from distutils.core import setup
import os
import os.path
import sys

VERSION = '0.1'


description = 'Stubs for SQLAlchemy'
with open('README.md') as f:
    long_description = f.read()


def find_installable_stubs(package_names):
    """Find all stubs to install, for setup(data_files=).

    Arguments:
      package_names:  List of directories to search in.

    """
    result = []
    for package_name in package_names:
        for root, _, files in os.walk(package_name):
            files = [os.path.join(root, filename) for filename in files
                     if filename.endswith('.pyi')]
            if not files:
                continue
            target = os.path.join(
                'shared', 'type-hinting',
                'python{}.{}'.format(*sys.version_info[:2]),
                root)
            result.append((target, files))
    return result

classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache License',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Software Development',
]

if __name__ == '__main__':
    setup(
        name='sqlalchemy-stubs',
        version=VERSION,
        description=description,
        long_description=long_description,
        author='Jelle Zijlstra',
        author_email='jelle.zijlstra@gmail.com',
        url='https://github.com/JelleZijlstra/sqlalchemy-stubs',
        license='Apache License 2.0',
        data_files=find_installable_stubs(['sqlalchemy']),
        classifiers=classifiers,
    )

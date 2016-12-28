#!/usr/bin/env python
import os
from setuptools import setup, find_packages

setup(
    name='lwt',
    author='Veit Heller',
    version='0.1.0',
    license='MIT',
    url='https://github.com/port-zero/lwt',
    description='Extensible data structure traversal in the command line',
    download_url = 'https://github.com/port-zero/lwt/tarball/0.1.0',
    packages=find_packages('.'),
    entry_points={
        'console_scripts': [
            'lwt = lwt:run',
        ]
    },
)


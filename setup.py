#!/usr/bin/env python
import os
from setuptools import setup, find_packages

setup(
    name='lwt',
    author='Veit Heller',
    version='0.1.0',
    license='MIT',
    url='https://github.com/port-zero/lwt',
    description='Get processes with open sockets but no permission to use them',
    download_url = 'https://github.com/port-zero/lwt/tarball/0.1.0',
    packages=find_packages('.'),
    entry_points={
        'console_scripts': [
            'lwt = lwt:run',
        ]
    },
)


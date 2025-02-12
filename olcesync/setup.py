#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created on 2018-08-12 19:22

import setuptools

setuptools.setup(
    name="olcesync",
    version="0.0.1",
    author="J. Zhao",
    author_email="author@example.com",
    description="A small example package",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests==2.*',
        'beautifulsoup4==4.*',
        'yaspin==2.*',
        'python-dateutil~=2.8.1',
        'click==8.*',
        'socketIO-client==0.5.7.4',
        'PySide6==6.*'
    ],
    entry_points={
        'console_scripts': [
                'olcesync=olcesync.olsync:main'
        ]
    }
)

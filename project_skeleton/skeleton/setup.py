#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
from setuptools import setup


setup(
    name='projectname',
    version='0.1',  # Version number
    license='License name',
    author='author name',
    author_email='author@email.com',
    description='project description',
    packages=['package_name'],
    platforms='systems on which to use this like, windows, linux, aws, etc.',
    install_requires=[
        'required',
        'libraries'
        'lists'
    ],
    classifiers=[
        'Development Status :: development version - Beta/production',
        'Environment :: Project Environment like Web Environment',
        'Intended Audience :: Who is going to be using this, generally Developers',
        'License :: OSI Approved :: License version',
        'Operating System :: Windows, Linux, Mac, OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
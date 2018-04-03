#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import pypeline


setup(

    name="pypeline",
    version=pypeline.__version__,
    packages=find_packages(),
    author="Martin Tovmassian",
    author_email="martin.tovmassian@protonmail.com",
    description="Pypeline Library: Unix pipes with Python",
    classifiers=[
        "Programming Language :: Python3",
        "Topic :: Pipes and coroutines"
    ]

)

#!/usr/bin/env python3

from setuptools import setup

setup(name='dev_aberto_isabella',
      version='0.1',
      packages=['dev_aberto'],
      author='Isabella Oliveira',
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
      ],
      python_requires='>=3.6',
      install_requires=['requests'],
      scripts=['scripts/hello.py']
      )

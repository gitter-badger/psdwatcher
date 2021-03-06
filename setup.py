#!/usr/bin/env python
#coding: utf-8

import os
from distutils.core import setup
from psdwatcher import __version__, __author__

def makebin():
    # make dir
    if not os.path.isdir("bin"):
        os.system("mkdir bin")

    # copy file
    os.system("cp psdwatcher.py bin/psdwatcher")

    # add permission
    os.system("chmod +x bin/psdwatcher")

makebin()

setup(
    name="psdwatcher",
    author=__author__,
    version=__version__,
    license=open("LICENSE").read(),
    url="https://github.com/alice1017/psdwatcher",
    description="You can watch the change log of psd file using git",
    long_description=open("README.rst").read(),
    requires=['termcolor'],
    scripts=['bin/psdwatcher']
)


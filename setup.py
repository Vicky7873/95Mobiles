import setuptools
from setuptools import setup,find_packages
import sys
import os

setup(
    name="95Mobiles",
    version="0.0.1",
    author="Bhikipallai",
    author_email="vicky.pallai900@gmail.com",
    packages=find_packages(where='src'),
    package_dir={'':'src'},
    install_requires = []
)
#!/usr/bin/env python

"""Setup script."""

import os
import glob
from setuptools import setup, find_packages

setup_dir = os.path.dirname(os.path.abspath(__file__))

# Long description loaded from the README
README = os.path.join(setup_dir, 'README.rst')

# Get requirements
REQUIREMENTS = os.path.join(setup_dir, 'requirements.txt')

# Get __version__ from version.py without importing package itself.
VERSION = os.path.join(setup_dir, 'extinctions/version.py')

# Package name
NAME = 'extinctions'

# Packages (subdirectories in extinction/)
PACKAGES = find_packages()

# Scripts (in scripts/)
SCRIPTS = glob.glob("scripts/*.py")

PACKAGE_DATA = {NAME: ["data/maps.yaml"]}

CLASSIFIERS = ['Development Status :: 3 - Alpha',
               'Intended Audience :: Science/Research',
               'Topic :: Software Development :: Build Tools',
               'License :: OSI Approved :: MIT License',
               'Programming Language :: Python :: 2',
               'Topic :: Scientific/Engineering :: Astronomy']

setup(name=NAME,
      version=open(VERSION).read().split('"')[1],
      description=("Extinction laws, maps and corrections"),
      license="MIT",
      classifiers=CLASSIFIERS,
      url="https://github.com/nicolaschotard/extinctions",
      author="Nicolas Chotard",
      author_email="nchotard@in2p3.fr",
      packages=PACKAGES,
      scripts=SCRIPTS,
      package_data=PACKAGE_DATA,
      long_description=open(README).read(),
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      install_requires=open(REQUIREMENTS).read().splitlines()
     )

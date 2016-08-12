#!/usr/bin/env python

import os
import glob
import yaml

from setuptools import setup

README = '/'.join(os.path.realpath(__file__).split('/')[:-1]) + '/README.rst'
VERSION = '/'.join(os.path.realpath(__file__).split('/')[:-1]) + '/version.yaml'

# Get __version__ from version.py without importing package itself.
__version__ = yaml.load(open(VERSION))['version']

# Package name
name = 'Extinction'

# Packages (subdirectories in extinction/)
packages = ["Extinction", "Extinction.extern"]

# Scripts (in scripts/)
scripts = glob.glob("scripts/*.py")

cmdclass = {}
command_options = {}
package_data = {name: ["data/maps.yaml"]}

setup(name=name,
      version=__version__,
      description=("Extinction laws, maps and corrections"),
      license="MIT",
      classifiers=["Topic :: Scientific :: Astronomy",
                   "Intended Audience :: Science/Research"],
      url="https://github.com/nicolaschotard/Extinction",
      author="Nicolas Chotard, Celine Combet, Dominique Boutigny",
      author_email="nchotard@in2p3.fr",
      package_dir={name: 'extinction'},
      packages=packages,
      #py_modules=modules,
      scripts=scripts,
      package_data=package_data,
      cmdclass=cmdclass,
      command_options=command_options
)

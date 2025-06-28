# In Python, setup.py is a module used to build and distribute Python packages. It typically contains information 
# about the package, such as its name, version, and dependencies, as well as instructions for building and installing the package.

from setuptools import find_packages,setup

file = open('requirements.txt')
requirements = file.readlines()
requirements = [i.replace("\n", "") for i in requirements]
if "-e ." in requirements:
    requirements.remove("-e .")

# parameters of setup
setup(name='mlproject',
version='0.0.1',
author='Anwesha',
author_email='anwesha.bose2021@gmail.com',
packages=find_packages(), # initializing the module find_packages # where is the parameter of find_packages
install_requires=requirements)
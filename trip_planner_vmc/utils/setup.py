#add package you want to make global
#run file with command:  python.exe setup.py install

from setuptools import setup, find_packages  
setup(name = 'utils', packages = find_packages())
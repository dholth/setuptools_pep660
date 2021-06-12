from setuptools import setup

# expose package 'b' but it's in directory 'a'
# works with normal install but not 'setup.py develop'
# not necessarily a must-have feature for improved develop mode
setup(name="00_package_dir", package_dir={"b": "a"}, packages=["b"])

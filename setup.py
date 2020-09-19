from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('src/algo.pyx'))
setup(ext_modules = cythonize('src/node_class.pyx'))
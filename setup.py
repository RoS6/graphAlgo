from setuptools import setup
import distutils.core
from Cython.Build import cythonize
# distutils.core.setup(
#     ext_modules=cythonize("cp.pyx"),
#     # name = 'cpapp'
#     # package_dir = {'cp':''}
# )
setup(
    ext_modules=cythonize("cp.pyx")
    # name = 'cpapp'
    # package_dir = {'cp':''}
)
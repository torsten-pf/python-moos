from setuptools import setup
from pathlib import Path
import sys, os

__version__ = "2022.1"

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# append local pybind11 directory to find the required files
sys.path.append(os.path.join(this_directory, 'pybind11'))

# Available at setup time due to pyproject.toml (not working on older systems)
from pybind11.setup_helpers import Pybind11Extension, build_ext
from pybind11 import get_cmake_dir

ext_modules = [
    Pybind11Extension("pymoos",
        ["src/pyMOOS.cpp"],
        libraries=["MOOS"],
        define_macros=[('VERSION_INFO', __version__)],
        ),
]

setup(
    name="pymoos",
    version=__version__,
    author='Mohamed Saad Ibn Seddik <ms.ibnseddik@gmail.com>',
    maintainer='Russ Webber <russ@rw.id.au>',
    description='MOOS Python Wrapper.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/russkel/python-moos",
    ext_modules=ext_modules,
    extras_require={"test": "pytest"},
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
)

from setuptools import setup, find_packages
import re
_version_re = re.compile(r"__version__\s+=\s+(.*)")
with open('my_school/__init__.py', 'r') as f:
    version = _version_re.search(f.read()).group(1).strip("'\"\n ")
setup(
    name='my_school',
    version=version,
    description='Custom Education extensions for dept',
    author='Your Dept',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
)

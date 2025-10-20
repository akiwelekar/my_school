from setuptools import setup, find_packages

setup(
    name='my_school',
    version='0.0.1',
    description='School Management App for ERPNext',
    author='Arvind Kiwelekar',
    author_email='akiwelekar@gmail.com',  # Optional but recommended
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
)

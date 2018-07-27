# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def requirements(fname):
    req = open(fname).readlines()
    install_requires = [i.strip('\r\n ') for i in req]
    return install_requires

setup(
    name='prometheus-http-client',
    version='0.1.0',
    description='Common prometheus client for python3',
    long_description=long_description,
    url='',
    author='xin.lin2@transwarp.io',
    author_email='xin.lin2@transwarp.io',
    keywords='Util',
    include_package_data=True,
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=requirements('requirements.txt'),
    package_data={},
)

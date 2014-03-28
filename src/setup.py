from distutils.core import setup
from setuptools import find_packages

setup(
    name='msml-webrunner',
    version='0.1',
    packages=['msmlweb', 'msmlweb.forms', 'msmlweb.model', 'msmlweb.views', 'msmlworker'],
    package_dir={'': 'src'},
    url='http://github.com/areku/msml-webrunner',
    license='gplv3',
    author='Alexander Weigl',
    author_email='uiduw@student.kit.edu',
    description='Running msml in the clouds',
    include_package_data = True,
    packages = find_packages(),
    package_dir = {'':'src'},

)

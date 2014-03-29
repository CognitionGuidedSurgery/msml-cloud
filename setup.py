from distutils.core import setup

from setuptools import find_packages


def file_get_contents(f):
    with open(f) as h:
        return h.readlines()


setup(
    name='msml-webrunner',
    version='0.1',
    packages=['web', 'web.forms', 'web.model', 'web.views', 'worker'],
    package_dir={'': 'src'},
    url='http://github.com/areku/msml-webrunner',
    license='gplv3',
    author='Alexander Weigl',
    author_email='uiduw@student.kit.edu',
    description='Running msml in the clouds',
    include_package_data=True,
    packages=find_packages(),
    package_dir={'': 'src'},
    install_requires=file_get_contents('requirements.txt')
)

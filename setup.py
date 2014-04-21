from setuptools import setup, find_packages


setup(
    name='linode',
    version='0.4',
    description='Python wrapper of the Linode API',
    long_description=open('README.rst').read(),
    author='George Hickman',
    author_email='george@ghickman.co.uk',
    url='http://github.com/ghickman/linode',
    license='MIT',
    packages=find_packages(),
    install_requires=('requests',)
)


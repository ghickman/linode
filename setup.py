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
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

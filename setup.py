from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='extracty',
    version=version,
    description='various utilities to extract metadata from HTML documents',
    author='Andrey Popp',
    author_email='8mayday@gmail.com',
    license='BSD',
    packages=['extracty', 'justext'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'lxml',
        'docopt',
    ],
    package_data={'justext': ['stoplists/*.txt']},
    test_suite='tests',
    entry_points="""
    # -*- Entry points: -*-
    [console_scripts]
    extracty = extracty:main
    justext = justext:main
    """)

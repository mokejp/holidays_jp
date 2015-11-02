from setuptools import setup, find_packages
import os

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
long_description = f.read()
f.close()

setup(
    name='holidays_jp',
    version='1.0.0',
    description='Calculate the Japanese holidays since 1948.',
    long_description=long_description,
    author='mo.kejp',
    url='https://github.com/mokejp/holidays_jp',
    packages=['holidays_jp', 'holidays_jp.countries'],
    install_requires=[
        'python-dateutil',
    ],
    license='MIT License',
    zip_safe=True,
    keywords=[
        'holidays_jp',
        'holiday',
        'japanese',
        'japan',
    ],
    classifiers=(
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7'
    ),
    test_suite="holidays_jp.tests",
)

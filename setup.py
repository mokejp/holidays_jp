from setuptools import setup, find_packages
import os

with open(os.path.join(os.path.dirname(__file__), 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='holidays-jp',
    version='1.0.2',
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
        'holidays-jp',
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

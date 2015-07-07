from setuptools import setup

import os
del os.link

setup(
    name='icd9',
    version='0.1',
    description='Supports comorbidity analysis using ICD9 codes, based on the R package of the same name',
    url='http://github.com/macroeyes/icd9',
    author='Kerby Shedden',
    author_email='kshedden@umich.edu',
    license='BSD',
    install_requires=[
        'pandas',
        'numpy'
    ],
    packages=['icd9'],
    include_package_data=True,
    test_suite ='icd9.tests.all_tests'
)

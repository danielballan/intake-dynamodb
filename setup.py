# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import versioneer

requires = open('requirements.txt').read().strip().split('\n')

setup(
    name='intake_dynamodb',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='dynamodb plugins for Intake',
    url='https://github.com/informatics-lab/intake-dynamodb',
    maintainer='Jacob Tomlinson',
    maintainer_email='jacob.tomlinson@informaticslab.co.uk',
    license='BSD',
    py_modules=['intake_dynamodb'],
    packages=find_packages(),
    package_data={'': ['*.csv', '*.yml', '*.html']},
    include_package_data=True,
    install_requires=requires,
    long_description=open('README.md').read(),
    zip_safe=False, )

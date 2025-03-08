#!/usr/bin/env python3

from setuptools import find_packages
from setuptools import setup

setup(
    name='wazo-custom-cdr',
    version='1.0',
    description='wazo custom cdr',
    author='workano team',
    author_email='info@workano.com',
    packages=find_packages(),
    url='https://workano.com',
    include_package_data=True,
    package_data={
        'wazo_custom_cdr': ['api.yml'],
    },

    entry_points={
        'wazo_call_logd.plugins': [
            'wazo_custom_cdr = wazo_custom_cdr.plugin:Plugin'
        ]
    }
)

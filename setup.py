#!/usr/bin/env python3

from setuptools import find_packages
from setuptools import setup

setup(
    name='wazo-call-on-queue-stat',
    version='1.0',
    description='wazo queue stat',
    author='workano team',
    author_email='info@workano.com',
    packages=find_packages(),
    url='https://workano.com',
    include_package_data=True,
    package_data={
        'wazo_call_on_queue_stat': ['api.yml'],
    },

    entry_points={
        'wazo_call_logd.plugins': [
            'call_on_queue_stat = wazo_call_on_queue_stat.plugin:Plugin'
        ]
    }
)

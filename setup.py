#!/usr/bin/env python
"""
sentry-redmine
==================

An extension for Sentry which integrates with Redmine. Specifically, it allows
you to easily create Redmine tickets from events within Sentry.

:copyright: (c) 2015 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""
from setuptools import setup, find_packages
import os

tests_require = [
    'exam',
    'flake8>=2.0,<2.1',
    'responses',
    'sentry>=8.9.0',
    'pytest-cov>=2.5.1,<2.6.0',
    'pyjwt>=0.3.2',
]
install_requires = [
    'sentry>=7.3.0',
]

setup(
    name='sentry-redmine',
    version='0.1.0',
    author='Sentry Team',
    author_email='support@getsentry.com',
    url='http://github.com/getsentry/sentry-redmine',
    description='A Sentry extension which integrates with Redmine.',
    long_description=__doc__,
    license='BSD',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=install_requires,
    extra_requires={'tests': tests_require},
    test_suite='runtests.runtests',
    include_package_data=True,
    entry_points={
        'sentry.apps': [
            'redmine = sentry_redmine',
        ],
        'sentry.plugins': [
            'redmine = sentry_redmine.plugin:RedminePlugin'
        ],
    },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'Django>=1.8,<2.2',
]

setup(
    author="Aidas Bendoraitis",
    author_email='aidasbend@yahoo.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="A Django App Providing the `{% include_by_ajax %}` Template Tag",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='django_include_by_ajax',
    name='django-include-by-ajax',
    packages=find_packages(include=['include_by_ajax']),
    url='https://github.com/archatas/django-include-by-ajax',
    version='0.4.0',
    zip_safe=False,
)
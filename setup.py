import os
from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='django-finkok',
    version='0.0.1',
    description='Simple django application to integrate the FINKOK \
service for sending invoices to the mexican treasury (SAT)',
    long_description=readme,
    # long_description=read("README.md"),
    author='GRVTYlabs',
    author_email='daniel.ortiz@grvtylabs.com',
    url='https://github.com/letops/django-finkok',
    packages=find_packages(),
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'suds-jurko',
    ],
)

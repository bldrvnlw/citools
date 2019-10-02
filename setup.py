import os
import sys
import setuptools

PROJECT_DIR = os.path.dirname(__file__)
sys.path.append(os.path.join(PROJECT_DIR, 'citools'))

from version import get_version

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='citools',
    setup_requires=['pygithub==1.43.8'],
    version=get_version().replace(' ', '-'),
    author='Baldur van Lew',
    author_email='b.van_lew@lums.nl',
    description='Handy tools for ci/cd rangling',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bldrvnlw/citools',
    install_requires=['pygithub==1.43.8'],
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
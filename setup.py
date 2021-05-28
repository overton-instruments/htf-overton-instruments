from setuptools import setup, find_packages
import htf_overton_instruments
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='htf-overton-instruments',
    version=htf_overton_instruments.__version__,
    packages=find_packages(exclude=("examples", )),
    license='MIT',
    description='Add-on package for the Hilster Testing Framework which enables'
                'testing Overton Instrument devices.',
    author='Overton Instruments',
    author_email='overton@overtoninstruments.com',
    url='https://github.com/overton-instruments/htf-overton-instruments',
    keywords=['htf', 'overton', 'HILSTER', 'Testing'],
    install_requires=[
        'htf>=2.0',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
)

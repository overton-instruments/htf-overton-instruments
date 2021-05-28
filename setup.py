from setuptools import setup, find_packages

import htf_overton_instruments

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
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers, QA Testers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.X'
    ],
)

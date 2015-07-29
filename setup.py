import sys

from setuptools import setup, find_packages

if sys.version_info[0] == 2:
    execfile('random_name_generator/version.py')
else:
    exec(open('random_name_generator/version.py', 'r').read())

long_description = """
Random name generator. Perfect for generating names for
anonymous users or suggested names for users.

See https://github.com/appressoas/random_name_generator/
"""

setup(
    name='random_name_generator',
    description='Random name generator.',
    license='BSD',
    version=__version__,
    url='http://github.com/appressoas/random_name_generator',
    author='Espen Angell Kristiansen',
    author_email='post@appresso.no',
    long_description=long_description,
    packages=find_packages(exclude=[]),
    install_requires=[
        'future'
    ],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)

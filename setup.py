from setuptools import setup
import pkg_resources
import re


def read(path):
    with open(pkg_resources.resource_filename(__name__, path)) as f:
        return f.read()


def long_description():
    return re.split('\n\.\. pypi [^\n]*\n', read('README.rst'), 1)[1]


setup(
    name='best_log_formatter',
    version='0.1',
    author='Chris Martin',
    author_email='ch.martin@gmail.com',
    packages=['best_log_formatter'],
    url='https://github.com/cardforcoin/best-python-log-formatter',
    license='MIT',
    description='A pretty cool log formatter.',
    long_description=long_description(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    install_requires=read('requirements-install.txt').split('\n'),
    tests_require=read('requirements-test.txt').split('\n'),
)

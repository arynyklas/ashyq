import pathlib
import re
import sys

from setuptools import find_packages, setup


WORK_DIR = pathlib.Path(__file__).parent

MINIMAL_PY_VERSION = (3, 5)

if sys.version_info < MINIMAL_PY_VERSION:
    raise RuntimeError('ashyq works only with Python {}+'.format('.'.join(map(str, MINIMAL_PY_VERSION))))


def get_version():
    txt = (WORK_DIR / 'ashyq' / '__init__.py').read_text('utf-8')

    try:
        return re.findall(r"^__version__ = '([^']+)'\r?$", txt, re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')


def get_description():
    with open('README.rst', 'r', encoding='utf-8') as f:
        return f.read()


setup(
    name='ashyq',
    version=get_version(),
    packages=find_packages(exclude=('examples.*',)),
    url='https://github.com/arynyklas/ashyq',
    license='MIT',
    author='Aryn Yklas',
    requires_python='>=3.5',
    author_email='arynyklas@gmail.com',
    description='Is a simple and synchronous framework for Private Ashyq API',
    long_description=get_description(),
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
    ],
    install_requires=[
        'requests>=2.26.0',
    ],
    include_package_data=False,
)

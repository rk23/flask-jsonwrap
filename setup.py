"""
Flask-JSONWrap

Wraps a Flask app such that all errors returned are JSON-API compatible,
rather than being HTML.
"""
from setuptools import setup, find_packages

requires = {
    'setup': [
    ],
    'install': [
        'Flask',
        'simplejson',
    ],
    'tests': [
        'pytest',
        'pytest-cov',
        'pytest-flake8',
        'requests',
    ],
}

requires['all'] = list({dep for deps in requires.values() for dep in deps})


def readme():
    with open('README.md', 'r') as f:
        return f.read()

setup(
    name='Flask-JSONWrap',
    description='Make a Flask app JSON API friendly.',
    long_description=readme(),
    url='http://github.com/daroot/flask-jsonwrap/',
    version='1.0.1',
    author='Dan Root',
    author_email='rootdan+pypi@gmail.com',
    license='WTFPL',

    packages=find_packages(exclude=['doc', 'test']),
    setup_requires=requires['setup'],
    install_requires=requires['install'],
    tests_require=requires['tests'],
    zip_safe=False,
    include_package_data=True,

    platforms='any',

    keywords=['flask', 'jsonapi'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: Freely Distributable',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

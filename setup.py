#!/usr/bin/env python

from pyntervalslib.version import APP_NAME, APP_VERSION
from distutils.core import setup

setup(name=APP_NAME,
        version=APP_VERSION,
        description='CLI client API for myintervals timetask service',
        author='Michel Petit',
        author_email='petit.michel@gmail.com',
        url='https://github.com/malenkiki/Pyntervals',
        packages=['pyntervalslib'],
        scripts=['pyntervals']
        )

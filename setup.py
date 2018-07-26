#!/usr/bin/env python
from setuptools import setup, find_packages
name = "nodejs_codegen"

requires = []

setup(
    name = name,
    version = '0.0.1',
    author = 'Zongying Cao',
    author_email = 'zongying.cao@dxc.com',
    description = 'nodejs-codegen is a library for generating the infrastructure code of microservices in nodejs.',
    long_description = """nodejs-codegen is a library for generating the infrastructure code of microservices in nodejs.""",
    url = 'https://github.com/cao5zy/nodejs-codegen',
    packages = [name, "nodejs_codegen.code", "nodejs_codegen.templates", "nodejs_codegen.templates.deploy"],
    include_package_data=True,
    install_requires = requires,
    license = 'Apache',
    classifiers = [
               'Development Status :: 4 - Beta',
               'Intended Audience :: Developers',
               'License :: OSI Approved :: Apache Software License',
               'Natural Language :: English',
               'Operating System :: OS Independent',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development :: Libraries',
           ],
)

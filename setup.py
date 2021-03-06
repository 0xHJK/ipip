#!/usr/bin/env python3
# -*- coding=utf-8 -*-


import setuptools
from os import path


proj_dir = path.dirname(path.realpath(__file__))
about_file = path.join(proj_dir, "ipip", "__version__.py")

about = {}
exec(open(about_file, "r", encoding="utf-8").read(), about)

long_description = open("README.md", "r", encoding="utf-8").read()

requirements = open("requirements.txt", "r", encoding="utf-8").read().splitlines()


setuptools.setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    license=about["__license__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    test_suite="tests",
    package_data={"ipip": ["db/qqwry.ipdb", "db/ipipfree.ipdb"]},
    entry_points={"console_scripts": ["ipip = ipip.__main__:main"]},
    install_requires=requirements,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Security",
        "Topic :: System",
        "Topic :: Utilities",
    ],
)

#!/usr/bin/env python
from setuptools import setup

setup(
    name="target-slack",
    version="0.1.0",
    description="Singer.io target for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["target_slack"],
    install_requires=[
        "singer-python>=5.0.12",
        "slack_sdk"
    ],
    entry_points="""
    [console_scripts]
    target-slack=target_slack:main
    """,
    packages=["target_slack"],
    package_data = {},
    include_package_data=True,
)

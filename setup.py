from setuptools import setup, find_packages

setup(
    name="common-lib",
    version="0.1.0",                          
    packages=find_packages(include=["common", "common.*"]),
    install_requires=[
    ],
    url="https://github.com/my-org/common-lib",
    python_requires='>=3.8',
)

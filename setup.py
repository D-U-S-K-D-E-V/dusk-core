from setuptools import setup, find_packages

setup(
    name="duskcore",
    version="0.1.3",
    packages=find_packages(where='src', exclude=['tests*']),
    package_dir={"": "src"},
    install_requires=[
        "requests",
        "pycryptodome",
        "fastapi",
        "pycryptodome"
    ],
    author="Ryan Clark",
    author_email="accounts@dusk-inc.com",
    description="This is a core library used by all Dusk microservices to function and distribute updates quickly.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/D-U-S-K-D-E-V/duskcore",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
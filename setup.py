import setuptools

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)                 
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)   

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tempailab",
    version="0.0.1",
    description='artificial intelligence and DBMS lab programs definitions',
    license='MIT',
    author="aiml department",
    author_email="aiml5thsem@gmail.com",
    url = 'https://github.com/aiml5thsem/tempailab',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=['artificial intelligence lab', 'DBMS lab', 'aimllab module'],
    install_requires=['py3nvml','numpy','psutil','py-cpuinfo','sparklines'],
    python_requires='>=3.6',
    py_modules=['tempailab'],
    package_dir={'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        'sys',
        'itertools',
        'numpy',
        'random',
        'time'
    ]
)
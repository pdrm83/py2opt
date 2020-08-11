import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="py2opt",
    version="1.0.9",
    description=" ",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/pdrm83/py2opt",
    author="Pedram Ataee",
    author_email="pedram.ataee@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["Py2Opt"],
    include_package_data=True,
    install_requires=['numpy', 'math', 'time', 'random2', 'itertools'],
    entry_points={
        "console_scripts": [
            "pdrm83=Py2Opt.__main__:main",
        ]
    },
)
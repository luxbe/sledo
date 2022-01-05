import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="sledo",
    version="0.1.0",
    description="A simple demodata generator for the command-line.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/luxbe/sledo",
    author="luxbe",
    author_email="luxbe@tutanota.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(exclude=["tests.*", "tests"]),
    install_requires=[
        'click',
        'pyyaml',
        'schema'
    ],
    entry_points={
        "console_scripts": [
            "sledo=sledo:cli"
        ]
    },
)

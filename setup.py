from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name = "pystack-manager",
    version = "0.9.4",
    author = "Plydow",
    maintainer = "Plydow",
    maintainer_email = "plydow.contact@gmail.com",
    keywords = "stack pystack",
    classifiers = ["Development Status :: 5 - Production/Stable",
        "Topic :: Education",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"],
    py_modules = ["pystack"],
    description = "python stack manager",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    license = "GNU GPLv3",
    python_requires = '>=3',
    platforms = "ALL"

)

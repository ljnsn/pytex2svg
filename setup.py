from setuptools import setup, find_packages


VERSION = "0.0.1"

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pytex2svg",
    version=VERSION,
    author="iuvbio",
    author_email="lyndonbjohn@gmail.com",
    description="A simple command line tool to convert TeX equations to SVG.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    scripts=["bin/pytex2svg"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
        "Operating System :: OS Independent",
    ],
    keywords="svg tex vector graphics convert",
    url="http://github.com/iuvbio/pytex2svg",
    license="GPLv3+",
    install_requires=["matplotlib"],
)

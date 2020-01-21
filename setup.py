import sys
import os
import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    MESSAGE = f.read()

if "HACKY_OVERRIDE_TO_BUILD_SDIST" not in os.environ:
    sys.stderr.write(MESSAGE)
    sys.exit(1)

setuptools.setup(
    name="ahip",
    version="0.0.1",
    description="A placeholder package for the hip project",
    long_description=MESSAGE,
    author="Nathaniel J. Smith",
    author_email="njs@pobox.com",
    url="https://github.com/python-trio/hip",
    license="MIT -or- Apache License 2.0",
    python_requires=">=3.5",
)

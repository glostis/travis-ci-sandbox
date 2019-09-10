import ast
import re
from codecs import open

from setuptools import setup

_version_re = re.compile(r"__version__\s+=\s+(.*)")

with open("travis_ci_sandbox.py", "rb") as f:
    version = str(ast.literal_eval(_version_re.search(f.read().decode("utf-8")).group(1)))


def readme():
    with open("README.md", "r", "utf-8") as f:
        return f.read()


setup(
    name="travis_ci_sandbox",
    version=version,
    description="Useless package to fool around with Travis CI",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="http://hello.world",
    author="Guillaume Lostis",
    author_email="hello@world.com",
    py_modules=["travis_ci_sandbox"],
    install_requires=[],
    python_requires=">=3.5",
)

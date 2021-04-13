import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fivempy",
    version="0.0.2",
    author="itasli",
    author_email="ilyas.tasli@outlook.com",
    description="A python wrapper for FiveM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/itasli/fivempy",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
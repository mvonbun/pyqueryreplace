# https://packaging.python.org/tutorials/packaging-projects/
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="query-replace-mvonbun",
    version="0.1.0",
    author="Michael Vonbun",
    author_email="m.vonbun@gmail.com",
    description="A small package to quer-search-and-replace strings in files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mvonbun/pyqueryreplace",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)

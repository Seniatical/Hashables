import setuptools

with open("README.md", "r", encoding="utf-8") as readme_file:
    desc = readme_file.read()

setuptools.setup(
  
    name = "hashize",
    version = "0.0.1",
    author = "Seniatical",
    license = "MIT",
  
    description = "Rewrite of the default python datatypes",
    long_description = desc,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Seniatical/Hashize",

    classifiers=[
        "Programming Language :: Python :: 3",
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',

    ],
)

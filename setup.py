import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="DigiLogger",
    version="1.0.0",
    author="DigiDuncan",
    author_email="digiduncan@gmail.com",
    description="DigiLogger",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DigiDuncan/DigiLogger",
    python_requires=">=3.7",
    install_requires=requirements,
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ]
)

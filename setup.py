import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PasswordManager",
    version="0.1.0",
    author="Stefano Vanin",
    description="Python password manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stefano-v37/password-manager",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
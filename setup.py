import setuptools

with open("README.md", "r") as fh:
    long_description =fh.read()

setuptools.setup(
    name="gufs",
    version="1.0.0",
    packages=setuptools.find_packages(),
    include_package_data=True,
    author_email="unaichi.chinonso@gmail.com",
    long_description=long_description,
    install_requires=['tqdm'],
    classifiers=["Programming Language :: Python :: 3"],

)

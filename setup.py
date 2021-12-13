from setuptools import setup


setup(
    name="starproduct",
    version="0.0.1",
    author="ht-90",
    author_email="",
    packages=["starproduct"],
    scripts=[],
    url="http://pypi.python.org/pypi/starproduct/",
    license="LICENSE",
    description="",
    long_description=open("README.md").read(),
    install_requires=[
        "requests",
        "beautifulsoup4",
    ],
)

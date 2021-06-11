from setuptools import setup

setup(
    name="setuptools_pep660",
    version="0.1",
    description="An experimental replacement for 'setup.py develop'",
    long_description="Implements a PEP 517 + PEP 660 backend",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Archiving :: Packaging",
    ],
    author="Daniel Holth",
    author_email="dholth@fastmail.fm",
    url="https://github.com/dholth/setuptools_pep660",
    keywords="setuptools pep660 pep517",
    license="MIT",
    packages=["setuptools_pep660"],
    package_dir={"": "src"},
    install_requires=[
        "setuptools",
    ],
    include_package_data=True,
    zip_safe=False,
)

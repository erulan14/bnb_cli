from setuptools import setup, find_packages

setup(
    name='bnb_cli',
    version="1.0",
    packages=find_packages(exclude=[]),
    install_requires=[
        "click", "pycosmicwrap"
    ],
    entry_points={
        "console_scripts": [
             "bnb_cli=bnb_cli.main:cli"
        ]
    }
)

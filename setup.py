from setuptools import setup, find_packages
from io import open
from os import path
import pathlib

#getting the directory which contains this file
HERE = pathlib.Path(__file__).parent

#text of the README.md file
README = (HERE / "README.md").read_text()

setup(
        name='arrange',
        description="""A simple Command-line application for arranging the files
        into folders whose names are the date of creation of the files""",
        version='1.0.0',
        packages=find_packages(), #list of packages
        python_requires='>=2.7',
        entry_points={
                'console_scripts':['arrange=arrange.__main__:main'
                ]
        },
        author="Maharshi Basu",
        keyword="arrange, file-arrange, cli",
        long_description=README,
        long_description_content_type="text/markdown",
        license='MIT',
        url='https://github.com/MashyBasker/arrange',
        author_email='basumaharshi10@gmail.com',
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            ]
        )




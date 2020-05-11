"""Setup file."""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dbg_assignment_ignat",
    version="0.0.1",
    author="Ignat Kudryavtsev",
    author_email="ignat@ignat.tel",
    description="DreamBroker Assignment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/db-garage/dbg-assignment-ignat",
    package_dir={'': 'src'},
    packages=["dbg_assignment_ignat"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

    install_requires=[
        "flask",
    ],

    entry_points={
        'console_scripts': [
            'dbg_assignment_ignat = dbg_assignment_ignat.__main__:main'
        ],
    }
)

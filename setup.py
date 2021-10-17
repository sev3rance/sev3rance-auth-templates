import os

from setuptools import find_packages, setup

from sev3rance_auth_templates import __version__

# read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="sev3rance-auth-templates",
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    license="GPLv3",
    description="Sev3rance Template Overrides for Alliance Auth",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sev3rance/sev3rance-auth-templates",
    author="Rounon Dax",
    author_email="rounon.dax@terra-nanotech.de",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires="~=3.7",
    install_requires=[
        "allianceauth>=2.9.0",
    ],
)

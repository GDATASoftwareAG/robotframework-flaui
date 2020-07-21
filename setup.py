import os
from setuptools import setup, find_packages

branch = os.getenv('BRANCH_NAME', 'local')
build_number = os.getenv('BUILD_ID', 0)
release = branch == 'master'

long_description = ''
with open("Readme.md", "r") as fh:
    long_description = fh.read()

version_data = {}
with open(os.path.join("src", "FlaUILibrary", "version.py")) as f:
    exec(f.read(), version_data)

requirements = []
with open("requirements.txt", "r") as f:
    requirements = list(filter(lambda s: s != "", f.read().split("\n")))

if release:
    version = "{}".format(version_data["VERSION"])
else:
    version = "{}rc{}".format(version_data["VERSION"], build_number)

setup(name="robotframework-flaui",
      version=version,
      description="Windows GUI testing library for Robot Framework",
      long_description=long_description,
      long_description_content_type="text/markdown",
      author="G DATA CyberDefense AG",
      author_email="opensource@gdata.de",
      install_requires=requirements,
      packages=find_packages("src"),
      package_dir={"FlaUILibrary": "src/FlaUILibrary"},
      package_data={"FlaUILibrary": ["bin/*.dll"]},
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      )

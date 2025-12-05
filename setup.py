from setuptools import setup, Distribution

class BinaryDistribution(Distribution):
    """Distribution which always forces a binary package with platform name"""

    # pylint: disable=no-self-use
    def has_ext_modules(self):
        """Distribution which always forces a binary package with platform name"""
        return True


with open("./src/FlaUILibrary/version.py", "r") as fh:
    VersionFile = fh.read()
    VersionFile = VersionFile.replace("\n", "")
    IGNORE, VERSION = VersionFile.split(" = ")
    VERSION = VERSION.replace("\"", "")

setup(
    version=VERSION,
    distclass=BinaryDistribution,
    platforms=['Windows'],
    license="MIT",               # SPDX identifier for modern setuptools
    license_files=["LICENSE"]    # Points to your license file (tuple or list)
)

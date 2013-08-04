from setuptools import setup, find_packages
from rest_nested_viewsets import __version__
import os


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


setup(
    name="drf-nested-viewsets",
    version=__version__,
    url="https://github.com/kevin-brown/drf-nested-viewsets/",
    license="MIT",
    description="Flat URLs can only go so far, bring nested URLs to your API."
    author="Kevin Brown",
    author_email="kbrown@rediker.com",
    packages=find_packages(exclude=["tests*", ]),
    package_data=get_package_data("rest_nested_viewsets"),
    install_requires=[
        "Django>=1.3",
        "djangorestframework"
    ]
)

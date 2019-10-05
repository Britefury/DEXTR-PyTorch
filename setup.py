import os
from setuptools import find_packages
from setuptools import setup

version = '0.1.dev1'

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.md')).read()
except IOError:
    README = ''

install_requires = [
    'six',
    'numpy',
    'Pillow',
    'scikit-image',
    # 'cv2',
    'torch',
    'torchvision',
    ]

tests_require = [
    ]

include_package_data = True

setup(
    name="DEXTR-PyTorch",
    version=version,
    description="PyTorch implementation of DEXTR",
    long_description="\n\n".join([README]),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: User Interfaces",
        ],
    keywords="",
    author="Sergi Caelles",
    url="https://github.com/Britefury/DEXTR-PyTorch",
    license="GPLv3",
    packages=find_packages(),
    include_package_data=include_package_data,
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'testing': tests_require,
        },
    )

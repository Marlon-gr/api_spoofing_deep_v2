# -*- encoding: utf-8 -*-
# Source:
# https://packaging.python.org/guides/distributing-packages-using-setuptools/

import io
import re

from setuptools import find_packages, setup

dev_requirements = [
    'bandit',
    'flake8',
    'isort',
    'pytest',
]
unit_test_requirements = [
    'pytest',
    'pytest-cov',
    'pyyaml',
    'requests'
]
integration_test_requirements = [
    'pytest',
]
run_requirements = [
    'Pillow==6.2.1', 'fastapi==0.108.0', 'gunicorn', 'flask-swagger-ui==3.25.0',
    'pyyaml==5.3.1', 'pydantic==2.5.3', 'torch==1.6.0', 'torchvision==0.7.0',
    'numpy==1.18.4', 'opencv-python==4.2.0.34', 'prometheus_client==0.8.0',
    'wget==3.2', 'starlette==0.29.0', 'loguru'
]

with io.open('./api_spoofing_deep_v2/__init__.py', encoding='utf8') as version_f:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_f.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

with io.open('README.md', encoding='utf8') as readme:
    long_description = readme.read()

setup(
    name="api_spoofing_deep_v2",
    version=version,
    author="Marlon Gonzalez Ramirez",
    author_email="glezmarlon0@gmail.com",
    packages=find_packages(exclude='tests'),
    include_package_data=True,
    url=""
        "api-spoofing-deep-v2",
    license="COPYRIGHT",
    description="Check if an image is taken from another image or from the "
                "real world.",
    long_description=long_description,
    zip_safe=False,
    install_requires=run_requirements,
    extras_require={
         'dev': dev_requirements,
         'unit': unit_test_requirements,
         'integration': integration_test_requirements,
    },
    python_requires='>=3.6',
    classifiers=[
        'Intended Audience :: Information Technology',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6'
    ],
    keywords=(),
    entry_points={
        'console_scripts': [
            'api_spoofing_deep_v2 = '
            'api_spoofing_deep_v2.main:app'
        ],
    },
)

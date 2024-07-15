from setuptools import setup, find_packages

setup(
    name='geo_zip',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'scipy',
    ],
    extras_require={
        'dev': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'geo-zip=geo_zip.main:main',
        ],
    },
    package_data={
        'geo_zip': ['data/geo_zip.csv'],
    },
    include_package_data=True,
)


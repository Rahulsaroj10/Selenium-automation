from setuptools import setup, find_packages

setup(
    name='selenium-automation',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'selenium>=4.10.0',
        'pytest>=7.0.0',
    ],
    entry_points={
        'console_scripts': [
            'selenium_automation=selenium_automation:main',
        ],
    },
)

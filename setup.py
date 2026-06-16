from setuptools import find_packages, setup

setup(
    name="ask",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.9",
    entry_points={"console_scripts": ["ask=ask.cli:main"]},
)

from setuptools import find_packages, setup

setup(
    name="nsrdesafio01",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "pydantic==2.4.2",
        "requests==2.27.1"
        # Add any other required packages here
    ],
    entry_points={
        "console_scripts": [
            "run_forever=nsrdesafio01.src.main:main",
        ],
    },
)

from setuptools import setup, find_packages

setup(
    name="asana_xt",
    version="0.0.1",
    author="Virgilio So",
    author_email="virgilio.so@extremelogic.ph",
    description="A Python package to interact with Asana's API and manage tasks",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/extremelogic-ph/asana_xt",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests>=2.20.0",
    ],
    entry_points={
        "console_scripts": [
            "asana_xt=asana_xt.main:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

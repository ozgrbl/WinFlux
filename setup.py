from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="winflux",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A powerful Windows system optimizer and cleanup tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chethanyadav456/WinFlux",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: System :: Systems Administration",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.10",
    install_requires=[
        "click>=8.1.0",
        "rich>=13.0.0",
        "psutil>=5.9.0",
        "colorama>=0.4.6",
        "winshell>=0.6; platform_system=='Windows'",
        "pywin32>=305; platform_system=='Windows'",
    ],
    entry_points={
        "console_scripts": [
            "winflux=winflux.cli:cli",
        ],
    },
)

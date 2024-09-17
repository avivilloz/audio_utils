from setuptools import setup, find_packages

setup(
    name="audio_utils",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pydub",
    ],
    author="Aviv Illoz",
    author_email="avivilloz@gmail.com",
    description=(
        "This is a Python package that provides a collection of utility "
        "functions for audio processing and manipulation. It offers simple "
        "and efficient tools for common audio-related tasks, with plans for "
        "expansion to cover a wide range of audio operations."
    ),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/avivilloz/audio_utils",
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

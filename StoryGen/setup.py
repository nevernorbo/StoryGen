from setuptools import setup, find_packages

with open("../README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as req_file:
    requirements = req_file.readlines()

setup(
    name="StoryGenSN",
    version="1.0.0",
    author="Sári Norbert",
    author_email="h164903@stud.u-szeged.hu",
    description="A Python package for Story generation using the ChatGPT API and OpenAI image creation tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SNorebo/StoryGen",
    packages=find_packages(),
    install_requires=requirements,
)

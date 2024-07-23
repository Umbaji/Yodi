from setuptools import setup, find_packages


with open("README.md", "r") as f:
    description = f.read()

setup(
    name="yodis",
    version="0.5.5",
    packages=find_packages(),
    install_requires=[
        'pathlib',
        'tensorflow',
        'matplotlib',
        'numpy',
        'seaborn',
        'IPython',
        'gradio',
    ],

    long_description=description,
    long_description_content_type="text/markdown",
)

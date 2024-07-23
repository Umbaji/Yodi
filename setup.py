from setuptools import setup, find_packages


with open("README.md", "r") as f:
    description = f.read()

setup(
    name="umbaji_yodi",
    version="1.0.0",
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

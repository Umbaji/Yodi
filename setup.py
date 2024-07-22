from setuptools import setup, find_packages


with open("README.md", "r") as f:
    description = f.read()

setup(
    name="yodi",
    version="0.0.0",
    packages=find_packages(),
    install_requires=[
        # Add dependencies here.
        # e.g. 'numpy>=1.11.1'
            "pathlib",
            "tensorflow",
            "matplotlib",
            "numpy",
            "seaborn",
            "IPython",
            "gradio"
    ],
    long_description=description,
    long_description_content_type="text/markdown",
)
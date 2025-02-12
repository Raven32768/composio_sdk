from setuptools import setup
import os


def get_current_dir():
    return os.path.dirname(os.path.realpath(__file__))


def resolve_paths(*paths):
    return os.path.join(*paths)


readme_path = resolve_paths(get_current_dir(), "README.md")

setup(
    name="composio_lyzr",
    version="0.2.12",
    author="Sawradip",
    author_email="sawradip@composio.dev",
    description="Use Composio to get an array of tools with your Lyzr workflow.",
    long_description=open(readme_path).read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SamparkAI/composio_sdk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    include_package_data=True,
)

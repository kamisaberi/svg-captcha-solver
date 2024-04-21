import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "svg-captcha-solver",
    version = "0.0.9",
    author = "kamran saberifard",
    author_email = "kamisaberi@gmail.com",
    description = "svg captcha solver",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/kamisaberi",
    project_urls = {
        "Bug Tracker": "https://github.com/kamisaberi",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.10"
)
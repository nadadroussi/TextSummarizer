import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

version = "0.0.0"

REPO_NAME = "TextSummarizer"
AUTHOR_USER_NAME = "Nada Droussi"
SRC_REPO = "TextSummarizer"
AUTHOR_EMAIL = "nada.droussi@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
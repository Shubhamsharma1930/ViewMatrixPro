import setuptools

with open("README.md", "r", encoding="UTF-8") as f:
    long_description = f.read()


__version__ = "0.0.3"

REPO_NAME = "ViewMatrixPro"
AUTHOR_USER_NAME = "Shubhamsharma1930"
AUTHOR_EMAIL = "shabby1930@gmail.com"
SRC_REPO = "ViewMatrixPro"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="secretenv",
    version="0.1.5",
    description="Playing with a secrets-in-repo idea.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="gmfawcett",
    url="https://github.com/gmfawcett/secretenv",
    author_email="graham.fawcett@gmail.com",
    license="MIT",
    packages=["secretenv"],
    install_requires=["scrypt==0.8.18"],
    python_requires=">=3.8",
)

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pumas-Amaretto-Coke", # Replace with your own username
    version="0.0.1",
    author="Brandon Muise",
    author_email="brandonmuise1@gmail.com",
    description="Project Unified Management Achive",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Amaretto-Coke/pumas",
    project_urls={
        "Bug Tracker": "https://github.com/Amaretto-Coke/pumas/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)

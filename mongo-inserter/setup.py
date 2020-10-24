import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mongo-inserter-omerbenda",
    version="1.0.0",
    author="Omer Ben David",
    author_email="omerbendavid21@gmail.com",
    description="MongoDB inserter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://192.168.5.124/omerbenda/omer-content-aggregator/mongo-inserter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

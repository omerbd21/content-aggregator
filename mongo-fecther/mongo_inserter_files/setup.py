import setuptools


setuptools.setup(
    name="mongo_inserter_omerbenda",
    version="1.0.0",
    author="Omer Ben David",
    author_email="omerbendavid21@gmail.com",
    description="MongoDB inserter",
    url="http://192.168.5.124/omerbenda/omer-content-aggregator/mongo-inserter",
    packages=['api', 'classes', 'connection', 'settings'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

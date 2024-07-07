from setuptools import setup, find_packages

setup(
    name="p1-tools",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'p1-pause=pause.__main__:main',
        ],
    },
    author="Dalton Serey",
    author_email="daltonserey@gmail.com",
    description="Ferramentas para p1@UFCG",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/daltonserey/p1-tools",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

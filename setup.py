from setuptools import setup, find_packages

setup(
    name="fpl",
    version="0.6.0",
    packages=find_packages(),
    description="A Python wrapper for the Fantasy Premier League API",
    url="https://github.com/amosbastian/fpl",
    author="amosbastian",
    author_email="amosbastian@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ],
    keywords="fpl fantasy premier league",
    project_urls={
        "Documentation": "http://fpl.readthedocs.io/en/latest/",
        "Source": "https://github.com/amosbastian/fpl"
    },
    entry_points="""
        [console_scripts]
        fpl=fpl.cli:cli
    """,
)

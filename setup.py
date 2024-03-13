from setuptools import setup, find_packages

setup(
    name="apl-compiler",  # Replace with your package name
    version="0.1",  # The initial release version
    packages=find_packages(),  # Automatically find and include all packages
    description="APL (Arabic Programming Language) Compiler - A tool for translating Arabic code into executable Python code, based on the APL specification.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",  # This is important for a Markdown README
    author="Serry Sibaee",
    author_email="ssibaee@psu.edu.sa",
    url="https://github.com/riotu-lab/apl-compiler",  # Optional
    install_requires=[
        'openai',
    ],
    python_requires='>=3.6',  # Specify the minimum Python version required
    classifiers=[
        # Choose your license as you wish
        'License ::  MIT License',
        'Programming Language :: Python :: 3.8'
    ],
)

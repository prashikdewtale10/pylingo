from setuptools import setup, find_packages

setup(
    name="PyLingo",
    version="0.1",
    description="A Python package for translating text to Hindi and Marathi",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Prashik Dewtale",
    author_email="prashikdewtale10@gmail.com",
    url="https://github.com/prashikdewtale10/PyLingo",
    packages=find_packages(),
    install_requires=[
        "googletrans==4.0.0-rc1"
    ],
    entry_points={
        'console_scripts': [
            'pylingo=translate.cli:main'  # Command-line interface (CLI)
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',  # Indicate the current development status
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',  # Specify Python version compatibility
        'License :: OSI Approved :: MIT License',  # License type
        'Operating System :: OS Independent',
        'Natural Language :: Hindi',  # Indicate languages supported
        'Natural Language :: Marathi',
    ],
    python_requires='>=3.6',
    include_package_data=True

)
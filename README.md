# Python Self-contained Runnable Package Template

This repository provides a template for creating a self-contained python
project in the form of a runnable python package.

In other words, a package that can be run directly from the command-line as
follows:

    python3 -m packagename

If one wishes to further wrap this package into a zipfile (e.g. package.zip), it
can still be executed without unzipping, as follows:

    export PYTHONPATH="package.zip"
    python3 -m packagename

Unit Tests can be run independently by typing:

    python3 -m packagename.tests

The overall structure is as follows:

    packagename         : Root folder (init/main files, etc)
    ├── config          : Folder containing editable package configuration(s)
    ├── doc             : Folder containing documentation resources
    ├── inputs          : Optional folder containing inputs to package
    ├── lib             : Optional folder containing third-party dependencies
    ├── outputs         : Optional folder for collecting outputs
    ├── res             : Folder containing resources (e.g. images, audio)
    ├── src             : Folder containing all modules used by __main__.
    └── tests           : Unit Tests. Can be run independently of main package


The template provided is simply a slightly more concretized example of this
hierarchy, demonstrating some of the implementation details that could be taken
into consideration when creating your own package. As such, the template itself
is a runnable example, producing nominal output purely for demonstration
purposes. However, note that it is still primarily intended as a template, and
its main purpose is to inspect all the files contained and modify as needed.

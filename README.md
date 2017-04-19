# Mesh 3D

[![Build](https://img.shields.io/travis/shawes/mesh3d-python.svg)](https://travis-ci.org/shawes/mesh3d-python)
[![GitHub issues](https://img.shields.io/github/issues/shawes/mesh3d-python.svg)](https://github.com/shawes/mesh3d-python/issues)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/shawes/mesh3d-python/master/LICENSE.md)


Mesh3d is an application to layer quadrats on 3D mesh files, gathering metrics on each quadrat to inform about the 3D mesh. It reads in a mesh file (or over lapping mesh files) stored in the [wavefront .obj format](https://en.wikipedia.org/wiki/Wavefront_.obj_file) and then creates quadrats of a given size from the midpoint of the bounding box. Metrics (e.g. rugosity) are applied to each quadrat and the output is saved to a .csv file for data manipulation.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Pre-requisites are Python3


### Installing

```
make install
```
## Usage



## Running the tests

```
make test
```


### Break down into end to end tests

Explain what these tests test and why

Give an example

### And coding style tests

Explain what these tests test and why

Give an example

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Python3](https://www.python.org) - The language framework used
* [Pypy](https://pypy.org) - Compiler used to increase execution time
* [PyTest](https://docs.pytest.org/en/latest/) - Unit testing framework
* [Sphinx](http://www.sphinx-doc.org/en/stable/) - Documentation generator

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* [Steven Hawes](https://github.com/shawes)
* [Will Figueira](https://github.com/willfig)

## License

[MIT](LICENSE.md) @ Steven Hawes

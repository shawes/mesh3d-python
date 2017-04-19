# Mesh 3D

[![Build](https://img.shields.io/travis/shawes/mesh3d-python.svg)](https://travis-ci.org/shawes/mesh3d-python)
[![GitHub issues](https://img.shields.io/github/issues/shawes/mesh3d-python.svg)](https://github.com/shawes/mesh3d-python/issues)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/shawes/mesh3d-python/master/LICENSE.md)

Mesh3d is an application to layer quadrats on 3D mesh files, gathering metrics on each quadrat to inform about the 3D mesh. It reads in a mesh file (or over lapping mesh files) stored in the [wavefront .obj format](https://en.wikipedia.org/wiki/Wavefront_.obj_file) and then creates quadrats of a given size from the midpoint of the bounding box. Metrics (e.g. rugosity) are applied to each quadrat and the output is saved to a .csv file for data manipulation.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine.

## Installing
Pre-requisites are Python (it was developed using Python3) and also the JIT compiler [PyPy](https://pypy.org).
```
make install
```

## Usage
```
mesh3d
Usage: pypy main.py [options]

  --dim <value>       the dimensions of the input files WLH (width-length-height)
  --size <value>      the size of a quadrat (standard is metres, but depends on the mesh units)
  --verbose           verbose is a flag
  --out <value>       output .csv file
  --meshes <file(s)>  input mesh files (.obj format)
```

### Example
To run mesh3d on three meshes (mesh1.obj, mesh2.obj, mesh3.obj) with dimensions of WHL in the XYZ plane. It will generates quadrats inside the bounding box using the size of 1 (units of the mesh) and print verbose output. The results will be stored in a file called output.csv.
```
	pypy main.py --dim XYZ --size 1 --verbose --out "output.csv" --meshes "mesh1.obj" "mesh2.obj" "mesh3.obj"
```

## Algorithm
1. Read in a list of .obj mesh files
2. Find the bounding box that encloses all the meshes
3. Subdivide the each mesh into the specified number of quadrats, starting at the centroid of the bounding box
4. Determine the number of faces (& vertices) that fall within each quadrat for each given mesh
5. Perform metrics on each quadrat (e.g. calculate surface rugosity)
6. Prints the output to a .csv file

### Csv Output
|Column Name| Description |
|-----------|-------------|
| mesh_name | The name of the processed mesh file |
| quadrat_size_m | The size of the fitted quadrats | In the base unit of the mesh, which should be metres |
| quadrat_rel_x | The relative x coordinates of the quadrat |
| quadrat_rel_y | The relative y coordinates of the quadrat |
| quadrat_rel_z_avg | The average of the relative z coordinates of the quadrat |Not implemented yet |
| quadrat_rel_z_stddev | The standard deviation of the relative z coordinates of the quadrat | Not implemented yet |
| quadrat_abs_x | The absolute x coordinates of the quadrat |
| quadrat_abs_y | The absolute x coordinates of the quadrat |
| quadrat_abs_z | The absolute x coordinates of the quadrat |
| num_faces | The number of faces in the quadrat |
| num_vertices | The number of vertices in the quadrat |
| 3d_surface_area | The area of the faces in the quadrat |
| 2d_surface_area | The area of the faces in the quadrat without the Z component |
| surface_rugosity | Surface rugosity is calculated as 3d_surface_area/2d_surface_area |

## Running the unit tests
```
make test
```

## Built With
* [Python3](https://www.python.org) - The language framework used
* [Pypy](https://pypy.org) - Compiler used to increase execution time
* [PyTest](https://docs.pytest.org/en/latest/) - Unit testing framework
* [Sphinx](http://www.sphinx-doc.org/en/stable/) - Documentation generator

## Versioning
We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/shawes/mesh3d-python/tags).

## Authors
* [Steven Hawes](https://github.com/shawes)
* [Will Figueira](https://github.com/willfig)

## License
[MIT](LICENSE.md) @ Steven Hawes

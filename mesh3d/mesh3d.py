import argparse
from io.obj_reader import ObjReader
from dimension_order import DimensionOrder
from bounding_box import BoundingBox
from quadrat_builder import QuadratBuilder
from shapes.mesh import Mesh
from io.csv_writer import CsvWriter


class Mesh3d(object):

    parser = argparse.ArgumentParser(
                            description='Measures rugosity of 3D meshes.',
                            prog='Mesh3D',
                            usage='%(prog)s [options]')
    parser.add_argument('--dim',
                        help='the dimensions of the input files WLH (width-length-height)',
                        default='XYZ')
    parser.add_argument('--size',
                        help='the size of a quadrat (standard is metres, but depends on the mesh units)',
                        type=float)
    parser.add_argument('--verbose',
                        help='prints verbose output',
                        action='store_true')
    parser.add_argument('--out',
                        help='output file to which to write (it has to be a .csv file)',
                        type=argparse.FileType('w'))
    parser.add_argument('--meshes',
                        help='input mesh files (.obj)',
                        nargs='*',
                        type=argparse.FileType('r'))
    args = parser.parse_args()

    if args.verbose:
        print("Starting to read the mesh files...")

    reader = ObjReader(args.verbose, DimensionOrder(args.dim))
    meshes = map(reader.read, args.meshes)

    if args.verbose:
        print("Finished reading in the mesh files.")

    if args.verbose:
        print("Calculating the bounding box...")

        bounding_box = BoundingBox(meshes)

    if args.verbose:
        print("Finished calculating the bounding box.")
        #print("Bounding box is of length" + l)
        # print("A: " + str(bounding_box.vertex_1))
        # print("B: " + str(bounding_box.vertex_2))
        # print("C: " + str(bounding_box.vertex_3))
        # print("D: " + str(bounding_box.vertex_4))

    # Generate virtual quadrats using the centroid of the bounding box
    if args.verbose:
        print("Generating the quadrats inside the bounding box...")

    quadrat_builder = QuadratBuilder()
    quadrats = quadrat_builder.build(bounding_box, args.size)

    if args.verbose:
        print("Finished generating all the quadrats.")

    if args.verbose:
        print("Calculating the area...")

    areas = map(lambda x: x.get_area(quadrats), meshes)

    if args.verbose:
        print("Finished calculating the area.")

    if args.verbose:
        print("Writing the output to a .csv file...")

    writer = CsvWriter()
    writer.write(arg.out, files.toList, quadrats, arg.size, areas)

    if args.verbose:
        print("Finished writing to " + arg.out.name)

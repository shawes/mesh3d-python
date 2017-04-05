import argparse
from dimension_order import DimensionOrder
from quadrat_builder import QuadratBuilder
from quadrilateral import Quadrilateral
from vertex import Vertex
import mesh_io
import pdb
import sys


def read_in_meshes(args):
    if args.verbose:
        print("Starting to read the mesh files...")

    meshes = []
    for mesh in args.meshes:
        meshes.append(mesh_io.read_obj(
            mesh, args.verbose, DimensionOrder(args.dim)))

    if args.verbose:
        print("Finished reading in the mesh files.")
    return meshes

def calculate_bounding_box(args, meshes):
    if args.verbose:
        print("Calculating the bounding box...")

    max_x = sys.maxsize * -1
    max_y = sys.maxsize * -1
    min_x = sys.maxsize
    min_y = sys.maxsize

    for mesh in meshes:
        for face in mesh.faces:
            for vertex in face.vertices:
                if vertex.x < min_x:
                    min_x = vertex.x
                if vertex.x > max_x:
                    max_x = vertex.x
                if vertex.y < min_y:
                    min_y = vertex.y
                if vertex.y > max_y:
                    max_y = vertex.y

    bounding_box = Quadrilateral(Vertex(min_x, min_y, 0), Vertex(max_x, min_y, 0),
                                 Vertex(max_x, max_y, 0), Vertex(min_x, max_y, 0))

    if args.verbose:
        print("Finished calculating the bounding box.")
        print("Bounding box is " + str(bounding_box))
    return bounding_box


def fit_quadrats_to_meshes(args, bounding_box):
    if args.verbose:
        print("Generating the quadrats inside the bounding box...")

    #quadrat_builder = QuadratBuilder()
    quadrats = QuadratBuilder().build(bounding_box, args.size)

    if args.verbose:
        print("Finished generating all the quadrats.")
        print("There are this many quadrats: " + str(len(quadrats)))
    return quadrats


def calculate_metrics_of_quadrats(args, meshes, quadrats):
    if args.verbose:
        print("Calculating the area...")

    metrics = map(lambda x: x.calculate_metrics(quadrats), meshes)

    if args.verbose:
        print("Finished calculating the area.")
    return metrics


def write_output(args, metrics):
    if args.verbose:
        print("Writing the output to a .csv file...")

    mesh_io.write_csv(args, metrics)

    if args.verbose:
        print("Finished writing to " + args.out.name)


def setup_command_line_parser():
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
    return parser


def main():
    parser = setup_command_line_parser()
    args = parser.parse_args()
    meshes = read_in_meshes(args)
    bounding_box = calculate_bounding_box(args, meshes)
    quadrats = fit_quadrats_to_meshes(args, bounding_box)
    evaluated_meshes = calculate_metrics_of_quadrats(args, meshes, quadrats)
    write_output(args, evaluated_meshes)

main()

import argparse
from dimension_order import DimensionOrder
from bounding_box import BoundingBox
from quadrat_builder import QuadratBuilder
import mesh_io
import pdb

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

def read_in_meshes(args):
    if args.verbose:
        print("Starting to read the mesh files...")
    #reader = mesh_io.read_obj(args.verbose, DimensionOrder(args.dim))
    meshes = []
    for mesh in args.meshes:
        meshes.append(mesh_io.read_obj(mesh, args.verbose, DimensionOrder(args.dim)))
    # meshes = list(map(lambda x: mesh_io.read_obj(x, args.verbose, DimensionOrder(args.dim)), args.meshes))
    if args.verbose:
        print("Finished reading in the mesh files.")
    return meshes

def calculate_bounding_box(args, meshes):
    if args.verbose:
        print("Calculating the bounding box...")
    bounding_box = BoundingBox(meshes)
    print("Bounding box is " + str(bounding_box))
    if args.verbose:
        print("Finished calculating the bounding box.")
    return bounding_box

def fit_quadrats_to_meshes(args, bounding_box):
    if args.verbose:
        print("Generating the quadrats inside the bounding box...")
    quadrat_builder = QuadratBuilder()
    quadrats = quadrat_builder.build(bounding_box, args.size)
    print("There are this many quadrats: " + str(len(quadrats)))
    if args.verbose:
        print("Finished generating all the quadrats.")
    return quadrats

def calculate_areas_faces_in_quadrats(args, meshes, quadrats):
    if args.verbose:
        print("Calculating the area...")
    #pdb.set_trace()
    areas = list()
    for mesh in meshes:
        areas += mesh.get_area(quadrats)

    #areas = list(map(lambda x: x.get_area(quadrats), meshes))
    print("Areas is "+ str(len(areas)))
    if args.verbose:
        print("Finished calculating the area.")
    return areas

def write_output(args, quadrats, areas):
    if args.verbose:
        print("Writing the output to a .csv file...")
    mesh_io.write_csv(args, quadrats, areas)
    if args.verbose:
        print("Finished writing to " + args.out.name)

args = parser.parse_args()
meshes = read_in_meshes(args)
bounding_box = calculate_bounding_box(args, meshes)
quadrats = fit_quadrats_to_meshes(args, bounding_box)
areas = calculate_areas_faces_in_quadrats(args, meshes, quadrats)
write_output(args, quadrats, areas)

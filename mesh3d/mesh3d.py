import argparse


class Mesh3d(object):

    parser = argparse.ArgumentParser(
                            description='Measures rugosity of 3D meshes.',
                            prog='Mesh3D',
                            usage='%(prog)s [options]')
    parser.add_argument('--dim', help='the dimensions of the input files WLH (width-length-height)',default='XYZ')
    parser.add_argument('--size', help='the size of a quadrat (standard is metres, but depends on the mesh units)', type=float)
    parser.add_argument('--verbose', help='prints verbose output', action='store_true')
    parser.add_argument('--out', help='output file to which to write (it has to be a .csv file)',type=file)
    parser.add_argument('--meshes', help='input mesh files (.obj)', nargs='*', type=file)
    args = parser.parse_args()
    run_mesh_3d()


    print("Verbose is "+ args.verbose.__str__())


"""

  def main(args: Array[String]) {
    parser.parse(args, Config()) match {
      case Some(config) =>
        val startTime = Calendar.getInstance.getTimeInMillis
        runMesh3D(config)
        val finishTime = Calendar.getInstance.getTimeInMillis
        println("Completed mesh quadrats in " + (finishTime - startTime) / 1000 + " seconds")
      case None =>
    }
  }

  def runMesh3D(config: Config): Unit = {
    val reader = new MeshReader(config.verbose, new DimensionOrder(config.dim))
    val files = config.files.par

    // Read in each mesh, creating a list of vertices and faces
    val meshes = files.map(x => reader.read(x))
    if (config.verbose) println("Finished reading in the mesh files")

    // Calculate the minimum bounding box that covers all the meshes
    val boundingBox = new BoundingBox(meshes)
    if (config.verbose) {
      println("Finished constructing the bounding box:")
      println("A: " + boundingBox.a)
      println("B: " + boundingBox.b)
      println("C: " + boundingBox.c)
      println("D: " + boundingBox.d)
    }

    // Generate virtual qudrats using the centroid of the bounding box
    val quadratBuilder = new QuadratBuilder()
    val quadrats = config.size.map(size => quadratBuilder.build(boundingBox, size))
    if (config.verbose) {
      print("Finished generating quadrats of sizes " + config.size.mkString(",") + " of which there were ")
      quadrats.foreach(quadrat => if (quadrats.head == quadrat) print(quadrat.size) else print("," + quadrat.size))
      print(" respectively.\n")
    }

    // Calculate the 3d & 2D areas of the quadrats, also returns the number of faces and vertices
    val areas = meshes.map(x => x.getArea(quadrats))
    if (config.verbose) println("Finished calculating the 2D and 3D areas of the quadrats")

    // Write the output to a CSV file
    val writer = new MeshCsvWriter()
    writer.write(config.out, files.toList, quadrats, config.size.toList, areas, config.append)
    if (config.verbose) println("Finished writing to " + config.out)
  }


}
"""

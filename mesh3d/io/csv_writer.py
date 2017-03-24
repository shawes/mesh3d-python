import os.path
import itertools


class CsvWriter(object):

    def write(self, args, quadrats, areas):
        # Strip extensions off filenames
        csv_file = args.out
        files = args.meshes
        quadrat_size = args.size
        names = map(lambda x: x.name.split('.')[0], files)
        areas = list(itertools.chain.from_iterable(areas))
        #files_exists = os.path.isfile(output_file)
        #csv_file = file.open(output_file)


        # Write headers if new file
        #if files_exists is True:
        csv_file.write("mesh_name, quadrat_size_m, quadrat_coord_x, quadrat_coord_y," +
                                "quadrat_centroid_x, quadrat_centroid_y, faces, 3d_area, 2d_area, rugosity\n")

        area_index = 0
        #size_index = 0
        for name in names:
            print(name)
            for quadrat in quadrats:
                print(str(quadrat.id[0]) + " " + str(quadrat.id[1]))
                area_info = areas[area_index]
                area3d = area_info[0]
                area2d = area_info[1]
                faces = area_info[2]
                vertices = area_info[3]
                rugosity = 0
                if(area2d > 0):
                    rugosity = area3d / area2d
                if area3d > 0 and area2d > 0:
                    csv_file.writeline(name + "," + str(size) + "," + str(quadrat.id[0]) + "," +
                                       str(quadrat.id[1]) + "," + quadrat.midpoint.x + "," + quadrat.midpoint.y + "," +
                                       faces + "," + vertices + "," + area3d + "," + area2d + "," + rugosity)
                area_index += 1
                #size_index += 1
        csv_file.flush()
        csv_file.close()

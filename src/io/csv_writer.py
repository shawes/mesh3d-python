import os.path


class CsvWriter(object):

    def write(output_file, files, quadrats_list, quadrat_size, areas_3D, areas_2D):
        # Strip extensions off filenames
        names = map(lambda x: x.name.split('.')[0], files)
        files_exists = os.path.isfile(output_file)
        csv_file = file.open(output_file)

        # Write headers if new file
        if files_exists is True:
            csv_file.writeline("mesh_name, quadrat_size_m, quadrat_coord_x, quadrat_coord_y," +
                           "quadrat_centroid_x, quadrat_centroid_y, faces, 3d_area, 2d_area, rugosity")

        areas_3D_merged = list(itertools.chain.from_iterable(
            list(itertools.chain.from_iterable(areas_3D))))
        areas_2D_merged = list(itertools.chain.from_iterable(
            list(itertools.chain.from_iterable(areas_2D))))

        area_index = 0
        size_index = 0
        for name in names:
            for mesh_quadrats in quadrats:
                for quadrat in mesh_quadrats:
                    area3d = (areas_3D_merged[area_index])[0]
                    area2d = areas_2D_merged[area_index][0]
                    faces = areas_3D_merged[area_index][1]
                    rugosity = area3d / area2d
                    if area3d > 0 and area2d > 0:
                        csv_file.writeline(name + "," + sizes[size_index] + "," + quadrat.id[0] + "," +
                                           quadrat.id[1] + "," + quadrat.midpoint.x + "," + quadrat.midpoint.y + "," +
                                           faces + "," + area3d + "," + area2d + "," + rugosity))

                    area_index += 1
                size_index += 1
            size_ndex += 0
        csv_file.flush()
        csv_file.close()

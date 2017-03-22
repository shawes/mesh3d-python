init:
	pip install -r requirements.txt

test:
	nosetests tests

run:
	python mesh3d/mesh3d.py

scenario1:
	python mesh3d/mesh3d.py --dim ZYX --size 10 --verbose --out "tests/output/scenario1.csv" --meshes "tests/input/aligned1.obj" "tests/input/aligned2.obj" "tests/input/aligned3.obj"

scenario2:
	python mesh3d/mesh3d.py --dim XYZ --size 5 --verbose --out "scenario_2.csv" --meshes "mesh1.obj" "mesh2.obj" "mesh3.obj"

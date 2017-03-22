init:
	pip install -r requirements.txt

test:
	nosetests tests

run:
	python mesh3d/mesh3d.py

scenario_1:
	python mesh3d/mesh3d.py --dim XYZ --size 10 --verbose --out "scenario_1.csv" --meshes "mesh1.obj" "mesh2.obj" "mesh3.obj"

scenario_2:
	python mesh3d/mesh3d.py --dim XYZ --size 5 --verbose --out "scenario_2.csv" --meshes "mesh1.obj" "mesh2.obj" "mesh3.obj"

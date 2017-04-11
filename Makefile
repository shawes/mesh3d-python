init:
	pip3 install -r requirements.txt

test:
	pytest -v

run:
	python3 mesh3d/mesh3d.py

test_obj_small:
	pypy main.py --size 0.1 --verbose --out "tests/output/small.csv" --meshes "tests/input/cube1.obj" "tests/input/cube2.obj" "tests/input/cube3.obj"

test_obj_large:
	pypy mesh3d/mesh3d.py --dim ZYX --size 1 --verbose --out "tests/output/large.csv" --meshes "tests/input/aligned1.obj" "tests/input/aligned2.obj" "tests/input/aligned3.obj"

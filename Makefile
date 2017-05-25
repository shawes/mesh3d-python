install:
	pip install -r requirements.txt

test:
	pytest -v

run:
	pypy main.py

test_obj_small:
	python main.py --size 0.1 --verbose --out "tests/output/small.csv" --meshes "tests/input/cube1.obj" "tests/input/cube2.obj" "tests/input/cube3.obj"

test_obj_large:
	pypy main.py --dim ZYX --size 1 --verbose --out "tests/output/large.csv" --meshes "tests/input/aligned1.obj" "tests/input/aligned2.obj" "tests/input/aligned3.obj"

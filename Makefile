all: setup mv_files

setup:
	python setup.py build_ext --inplace

mv_files:
	mv *.so src/

clean:
	rm src/*.c
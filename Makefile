.PHONY: beautiful black build clean isort jacobus py311 py312 reset sort_json zip
SHELL := /bin/zsh

beautiful: sort_json isort black jacobus

black: py311
	conda run -n py311 pip install 'black>=24.5,<26';
	conda run -n py311 black --line-length=79 . ;

build: beautiful clean dist/oblivion.zip

clean:
	rm -fr 'dist/';
	rm -fr 'out/';

dist:
	mkdir -p dist/

dist/oblivion.zip: | dist
	cd src/oblivion && zip -rq ../../dist/oblivion.zip . -x ".*" "*/.*"

isort: py311
	conda run -n py311 pip install 'isort>=6.0,<7';
	conda run -n py311 isort . ;

jacobus: py311
	conda run -n py311 pip install 'jacobus>=2.2,<3';
	conda run -n py311 python -m jacobus @make/jacobus.txt;
	conda run -n py311 python -m jacobus @make/jacobus_Makefile.txt;
	conda run -n py311 python -m jacobus @make/jacobus_gitignore.txt;

py311:
	conda run -n base python make/env.py py311 --python=3.11;

py312:
	conda run -n base python make/env.py py312 --python=3.12;

reset:
	git reset HEAD~1;

sort_json: py311
	conda run -n py311 python make/sort_json.py @make/sort_json.txt;

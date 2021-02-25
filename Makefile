all: clean build

build:
	cd src ; \
	zip ../PCS-Alfred.alfredworkflow . -r --exclude=*.DS_Store* --exclude=.git/* --exclude="LICENSE"

clean:
	rm -f *.alfredworkflow
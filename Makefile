# make a myflib python module using f2py
all:
	f2py -c -m myflib helmholtz.f90 timmes.f90 -I/path/to/files/*.dek
clean:
	rm -r *.so


all:
	f2py -c -m myflib compute_functions.f90
clean:
	rm -r *.so
#gfortran compute_functions.f90 main.f90 -o run.exe


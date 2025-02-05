# make a myflib python module using f2py
all:
	f2py -c -m myflib helmholtz.f90 timmes.f90 -I/home/sudarshan/research_utk/SPH_LOG_UG_SPARK/python_differenteos
	f2py -c -m myflib_changed helmholtz_changed.f90 timmes.f90 -I/home/sudarshan/research_utk/SPH_LOG_UG_SPARK/python_differenteos
	#f2py -c -m myflib_changed_2 helmholtz_changed_2.f90 timmes.f90 -I/home/sudarshan/research_utk/SPH_LOG_UG_SPARK/python_differenteos

clean:
	rm -r *.so


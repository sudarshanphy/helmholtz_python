## Description
This repo has helmholtz and timmes EOS obtained from [Frank Timmes coccocubed](http://cococubed.asu.edu/code_pages/eos.shtml) website, along with a simple EOS having ideal gas and radiation contribution. [f2py](https://numpy.org/doc/stable/f2py/) has been used to construct a python wrapper for above mentioned EOS. 

## Prerequisites
 - Tests have been performed using python 3. 
 - f2py is necessary to build the python module.

## Building and running
 - Generate python module using "make"
 - Load the module in python scripts and use the subroutines inside. See [eos_test.py](https://github.com/sudarshanphy/python_differenteos/blob/main/eos_test.py).


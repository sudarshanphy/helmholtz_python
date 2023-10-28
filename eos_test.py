import myflib

#inputs:
temp = 1.0e8
dens = 1.0e6
abar = 1.2358393408856847
zbar = 1.0813594232749741

#ouput:
#pres, eint, entr

#read the helm table for helmholtz eos
myflib.helm.read_helm_table()

print(myflib.helm.helmeos(temp, dens, abar, zbar))
print(myflib.timm.eosfxt(temp, dens, abar, zbar))
print(myflib.helm.modgamma(temp, dens, abar, zbar))


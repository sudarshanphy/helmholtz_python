import myflib
import myflib_changed
import yt
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys


mpl.rcParams['lines.linewidth'] = 3
mpl.rcParams['font.family'] = 'DeJavu Serif'
mpl.rcParams['font.serif'] = ['Times New Roman']
mpl.rcParams['font.size'] = 20.0

d = "./1drun_flashx/"
fname = "ccsn_1dsph_3609_flashx_init_hdf5_plt_cnt_0000"



ds = yt.load(d+fname)

ad = ds.all_data()

r = np.array(ad[("flash","radi")])
dens = np.array(ad[("flash","dens")])
temp = np.array(ad[("flash","temp")])

index = 1 #return eint

helm1_data = []
helm2_data = []
timmes_data = []


myflib.helm.read_helm_table("helm_table_original.dat")
for rad,t,d in zip(r,temp,dens):
    helm1_data.append(myflib.helm.helmeos(t, d, 1.0, 1.0)[index])
    timmes_data.append(myflib.timm.eosfxt(t, d, 1.0, 1.0)[index])


# A helmholtz table that has tlo = 01, thi = 11, jmax = 201
# dlo = -18, fhi = 09, imax = 541
myflib_changed.helm.read_helm_table("helm_table_0111201-1809541.dat")
for rad,t,d in zip(r,temp,dens):
    helm2_data.append(myflib_changed.helm.helmeos(t, d, 1.0, 1.0)[index])
    #timmes_data.append(myflib_changed_2.timm.eosfxt(t, d, 1.0, 1.0)[index])



fig = plt.figure(figsize=(10,10))
ax = fig.subplots(1)
fig.set_tight_layout(True)
#plt.tight_layout()


#plt.title("Comparison of Helmholtz EOS with Timmes EOS (exact)")

ax.plot(r, \
         abs(np.array(timmes_data)-np.array(helm1_data))/np.array(timmes_data),\
         "r-" , label = "original EOS")
ax.plot(r, \
         abs(np.array(timmes_data)-np.array(helm2_data))/np.array(timmes_data),\
         "g--" , label = "extended EOS")

ax.set_xlabel("Radius (cm)")
ax.set_ylabel("Fractional difference in Internal Energy")# + r" $\frac{|timmes - table|}{timmes}$")


ax.legend()

ax.set_xscale("log")
ax.set_yscale("log")
#plt.savefig("nasa_eos_helm_table_compare.png")
plt.show()

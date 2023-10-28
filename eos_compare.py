import myflib
import yt
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys


mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['font.family'] = 'DeJavu Serif'
mpl.rcParams['font.serif'] = ['Times New Roman']
mpl.rcParams['font.size'] = 15.0

#read the helm table
myflib.helm.read_helm_table()

ds = yt.load("./chk_files/ccsn_1dsph_flashx_gcc_ug_hybrid_summit_compare_3_hdf5_chk_0000")

ad = ds.all_data()

#print(ds.field_list)

r = np.array(ad[("flash","radi")])
dens = np.array(ad[("flash","dens")])
temp = np.array(ad[("flash","temp")])
abar = np.array(ad[("flash","abar")])
zbar = np.array(ad[("flash","zbar")])
eint = np.array(ad[("flash","eint")])
ye = np.array(ad[("flash","ye  ")])

pres = np.array(ad[("flash","pres")])

helm_r = []
helm_temp = []
helm_pres = []
helm_eint = []
helm_entr = []

mgam_r = []
mgam_temp = []
mgam_pres = []
mgam_eint = []
mgam_entr = []

timmes_r = []
timmes_temp = []
timmes_pres = []
timmes_eint = []
timmes_entr = []

#print(myflib.timm.eosfxt(1.0e4, 1.0e-9, 1.32, 1.22))


for rad,t,d,a,z in zip(r,temp,dens,abar,zbar):
    #if (t >= 1.0e4 or d >= 5.0e-10):
    #if (d >= 5.0e-10):
    helm_r.append(rad)
    helm_temp.append(t)
    helm_pres.append(myflib.helm.helmeos(t, d, a, z)[0])
    helm_eint.append(myflib.helm.helmeos(t, d, a, z)[1])
    helm_entr.append(myflib.helm.helmeos(t, d, a, z)[2])
    
    timmes_r.append(rad)
    timmes_temp.append(t)
    timmes_pres.append(myflib.timm.eosfxt(t, d, a, z)[0])
    timmes_eint.append(myflib.timm.eosfxt(t, d, a, z)[1])
    timmes_entr.append(myflib.timm.eosfxt(t, d, a, z)[2])
    #if (t < 2.0e4 or d < 5.0e-8):
    #if (d < 5.0e-8):
    mgam_r.append(rad)
    mgam_temp.append(t)
    mgam_pres.append(myflib.helm.modgamma(t, d, a, z)[0])
    mgam_eint.append(myflib.helm.modgamma(t, d, a, z)[1])
    mgam_entr.append(myflib.helm.modgamma(t, d, a, z)[2])
    
plt.figure(1)
#plt.plot(helm_r, helm_pres, "r-" , label = "helmholtz")
#plt.plot(timmes_r, timmes_pres, "b--" , label = "timmes")
#plt.plot(mgam_r, mgam_pres, "g-", label = "modified gamma")
#plt.plot(r, pres, "ko--", label = "FlashX init")
#plt.axvline(x = 1.5e13, color = "b")

plt.plot(helm_r, abs(np.array(helm_pres)-np.array(timmes_pres)), "r-" , label = "helmholtz - timmes")


'''
plt.plot(temp, helm_pres, "r-" , label = "helmholtz")
plt.plot(temp, mgam_pres, "g--", label = "modified gamma")

plt.plot(dens, helm_pres, "r-" , label = "helmholtz")
plt.plot(dens, mgam_pres, "g--", label = "modified gamma")
'''
plt.legend()

'''
plt.figure(2)
plt.plot(r, ye, "r-", label="ye")
plt.plot(r, zbar/abar, "g--", label="zbar/abar")
plt.legend()
'''
plt.xscale("log")
plt.yscale("log")
plt.show()
#print(output)


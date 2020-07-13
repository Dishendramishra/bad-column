#%%
import astropy.io.fits as fits
import matplotlib.pyplot as plt
import numpy as np

%matplotlib

#%%
# Finding wavelentgs under bad columns in each order

flat = fits.getdata("fits_src/fl_MED_30sec.fits")
flat = flat[:,:][::-1]
flat = flat[40:,51:6195]

wavelength_fitted = fits.getdata("fits_src/wavelength_fitted.fits")
wavelength_fitted = wavelength_fitted[:,:][::-1]
wavelength_fitted = wavelength_fitted[:6160,:]

# flat = flat[:,:][::-1]
# fits.writeto("output/stripped_flat.fits",data=flat,overwrite=True)
# wavelength_fitted = wavelength_fitted[:,:][::-1]
# fits.writeto("output/stripped_wavelength_fitted.fits",data=wavelength_fitted,overwrite=True)

#%%
temp = wavelength_fitted[:,2552:2594+1]
indicies = np.nonzero(temp)

y = indicies[0]
x = indicies[1] + 2552

wavelengths_wasted = wavelength_fitted[y,x]
wavelengths_wasted = wavelengths_wasted.reshape(73,43)
wavelengths_wasted = np.array([sorted(x) for x in wavelengths_wasted])
    

# np.savetxt("output/wavelengths_wasted.txt",wavelengths_wasted,delimiter="\t")
# np.savetxt("output/wavelengths_wasted.csv",wavelengths_wasted,delimiter=",")
#%%
table = [["order "+str(i) for i in range(1,74)]]
table.append(np.round(wavelengths_wasted[:,0]*10000,3))
table.append(np.round(wavelengths_wasted[:,-1]*10000,3))
table = np.array(table)

table = table.T
np.savetxt("output/wavelengths_wasted.txt",table,fmt="%s",delimiter="    ")
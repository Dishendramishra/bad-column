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
# flat = flat[1:6160,51:6195]

wavelength_fitted = fits.getdata("fits_src/wavelength_fitted.fits")
wavelength_fitted = wavelength_fitted[:,:][::-1]
wavelength_fitted = wavelength_fitted[:6160,:]

# flat = flat[:,:][::-1]
# fits.writeto("output/stripped_flat.fits",data=flat,overwrite=True)
# wavelength_fitted = wavelength_fitted[:,:][::-1]
# fits.writeto("output/wavelength_fitted.fits",data=wavelength_fitted,overwrite=True)


#%%
temp = wavelength_fitted[:,2552:2594+1]
indicies = np.nonzero(temp)
# x = indicies[0].reshape(73,40)
# y = indicies[1].reshape(73,40)

y = indicies[0]
x = indicies[1] + 2552

wavelengths_wasted = wavelength_fitted[y,x]
wavelengths_wasted = wavelengths_wasted.reshape(73,43)

# np.savetxt("output/wavelengths_wasted.txt",wavelengths_wasted,delimiter="\t")
# np.savetxt("output/wavelengths_wasted.csv",wavelengths_wasted,delimiter=",")
#%%
table = [["order "+str(i) for i in range(73,0,-1)]]
table.append(np.round(wavelengths_wasted[:,0]*10000,3))
table.append(np.round(wavelengths_wasted[:,-1]*10000,3))
table = np.array(table)

table = table.T

np.savetxt("output/wavelengths_wasted.txt",table,fmt="%s",delimiter="    ")


# #%%
# img = fits.getdata("fl_MED_30sec.fits")
# plt.imshow(img,origin="lower")
# plt.show()

# #%%
# # Superimposing Artifical Spectra on Dark Frame

# art_spectra = fits.getdata("conv_spatial.fits")
# art_spectra = art_spectra[:-31,:]
# dark = fits.getdata("da_MED_0sec.fits")
# dark = dark[1:6160,51:6195]

# spectra = np.add(art_spectra,dark)
# fits.writeto("spectra.fits",data=spectra,overwrite=True)
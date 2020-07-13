#%%
import numpy as np 

g2_mask = np.loadtxt("src/G2.sophie.mas",delimiter="\t")
g2_mask = g2_mask.round(3)

#%%

# ==================================================
#  Creating x-axis,  
x = np.arange(3781,6806,0.001)
x = x.round(3)
y = np.zeros(3025000)

dic = {i:0 for i in x}


# #  Filling values at indcies using G2 mask
# for row in g2_mask:
#     try:
#         dic[row[0]] = row[2]
#         dic[row[1]] = row[2]
#     except:
#         pass
# x = list(dic.keys())
# x = np.round(x,3)
# y = list(dic.values())


for row in g2_mask:
    i = np.where(x == row[0])
    if len(i[0]) != 0:
        y[i] = row[2]
        
    i = np.where(x == row[1])
    if len(i[0]) != 0:
        y[i] = row[2]
    
# ==================================================


# ==================================================
# replacing values in template using G2 mask
filler = 0

for i,v in enumerate(y):
    
    if v == 0 and filler != 0:
        y[i] = filler
        
    else:
        if v != filler:
            filler = v
        else:
            filler = 0
# ==================================================

#%%

temp = np.column_stack((x,y))
np.savetxt("output/features.txt",temp,delimiter="    ",fmt='%1.3f')

# #%%
# Algo for replacing values in template using values for G2 mask
# a = [0,2,0,0,2,0,0,0,0,0,4,4,0,0,0,0,0,0,6,0,0,0,6,0,6,0,0,0,0,6]

# filler = 0

# for i,v in enumerate(a):
    
#     if v == 0 and filler != 0:
#         a[i] = filler
        
#     else:
#         if v != filler:
#             filler = v
#         else:
#             filler = 0
            
# if filler:
#     print("imbalanced array")
            
            
            

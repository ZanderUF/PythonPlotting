#Author:  Zander
#Purpose: Plotting PKTEST Data KENOVI vs. KENOVA for neutronics calculations


import numpy as np
import matplotlib.pyplot as plt

#usecols defines columns of data
data = np.genfromtxt('/Users/macosx/Documents/UF_Research/INL_REPORT/pktest_comp_k5VsK6.csv',delimiter=',',usecols=(1,4,14))

#get the data 
x=data[:,0]
y1=data[:,1]
y2=data[:,2]

plt.plot(x,y1, '-',label='KENOVI')
plt.plot(x,y2,label='KENOVa')
     
#Define Plot parameters                       
plt.title('PKTEST')
plt.xlabel('Time (s)')
plt.ylabel('Power (MW)')
plt.legend(loc='lower left',prop={'size':8},numpoints=1)
plt.grid(True)

plt.show()
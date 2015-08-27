#Purpose: Plotting QUENCH TREAT MODEL Data KENOVI vs. KENOVA for neutronics calculations


import numpy as np
import matplotlib.pyplot as plt


data = np.genfromtxt('/Users/macosx/Documents/UF_Research/INL_REPORT/quench_k6_k5vsk6.csv',delimiter=',',usecols=(1,4))

#get the data 
x=data[:,0]
y1=data[:,1]

plt.axis([0,8,0,4000])
plt.plot(x,y1, '-',label='KENOVI')
     
#Define Plot parameters                       
plt.title('Quench')
plt.xlabel('Time (s)')
plt.ylabel('Power (MW)')
plt.legend(loc='upper right',prop={'size':8},numpoints=1)
plt.grid(True)


plt.show()
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np






#  ------------------------------------------------------
#  PLOTDATA: plots a line and saves
#  it as a png image ...
#
def plotData(x,y,name):
    plt.clf()
    plt.plot(x,y,'k.')
    plt.title('Raw Data')
    plt.savefig(name)

#  ------------------------------------------------------
#  PLOTFIT: plots line AND data and saves it as a png
#
#
def plotFit(x,y,z,name):
    plt.clf()
    plt.plot(x,y,'k.')
    plt.plot(x,z,'k-')
    plt.title('Fit to Data')
    plt.savefig(name)

#  ------------------------------------------------------
#  GRABDATA
#    Pulls data from file and stores it in x,y
#
def grabData():
    dat=np.genfromtxt('linFit.txt')
    x=dat[:,0]
    y=dat[:,1]

    return (x,y)



#  ------------------------------------------------------
# Step 3: Given list of x return list of h0*x
def hubble(x,h0):

    m= [] 
    for i in x:
         m.append(h0*i)
    
    return m
    
        
        


#     Given data lists x and y, this function
#     finds how well a line, hubble(x) = h0*x fits
#     by calculating the sum of the square of
#     the residuals
#

#Step 5:
def SSR(x,y,h0):
    b=hubble(x,h0)
    
    SSR=0
    for i in range(len(x)):

        r = b[i]-y[i]
        rsq=r**2
        SSR=SSR+rsq
        
    return SSR 
    
        

#
#  Step 2: Get data, plot it
#

x, y=grabData()
plotData(x,y,'rawData.png')


#   Step 4: Plot example function
#
x,y=grabData()
z= hubble(x,10)
plotFit(x,y,z,'badFit.png')

#
#  Step 6: Find SSR for poor fit from example function
#

x,y=grabData()

m = SSR(x,y,10)
print m



#
#   list for possible slopes. 
#

h0s=np.arange(0.,100.,0.1)

#
#  Step 7: Find slope and intercept that minimize
#              the RSS
#
best_h0 = 0.
min_ssr = np.inf

for h0 in h0s: 

    k = SSR(x,y,h0)
    if k<min_ssr:
        best_h0=h0
        min_ssr=k


print best_h0
print min_ssr

    


    

#
#   Step 8: Plot Result
#
#
x,y=grabData()
z=hubble(x,best_h0)
plotFit(x,y,z,'bestFit.png')

#
#   Step 9: Plot Residuals
#
#
res =[z[i]-y[i] for i in range(len(y))]

plotData(x,res,'resids.png')






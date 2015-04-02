import matplotlib.pyplot as plt
import numpy as np



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
    dat=np.genfromtxt('linfit.txt')
    x=dat[:,0]
    y=dat[:,1]

    return (x,y)



#  ------------------------------------------------------
# Given list of x return list of h0*x
def hubble(x,h0):
    return 0.


#     Given data lists x and y, this function
#     finds how well a line, hubble(x) = h0*x fits
#     by calculating the sum of the square of
#     the residuals
#
def SSR(x,y,h0):


#
#  Get data, plot it
#

x, y=grabData()

#   Plot example function
#


#
#  Find SSR for poor fit from example function
#


#
#   Make lists for possible slopes and
#              intercepts, then print them
#

h0s=np.arange(0.,100.,0.1)

#
#  Find slope and intercept that minimize
#              the RSS
#
bestSlope = 0.
min_ssr = np.inf

#
#   Plot Result
#
#


#
#   Plot Residuals
#
#


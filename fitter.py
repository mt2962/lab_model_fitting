import matplotlib.pyplot as plt


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
	f = open('linFit.dat','r')
		
	dataString = f.read()
	f.close()
	dataLines = dataString.split('\n');
	N = len(dataLines)-1
	x = []
	y = []

	for i in range(N):
		line = dataLines[i].split('\t')
		x.append(float( line[0] ))
		y.append(float( line[1] ))

	return (x,y)
	


#  ------------------------------------------------------
#  F
#    Given data list x, returns a list y = mx+b 
#
def f(x,m,b):
	return 0					# FIXME!

#
#   SSR
# 
#     Given data lists x and y, this function
#     finds how well a line, f(x) = mx+b fits
#     by calculating the sum of the square of
#     the residuals
#
def SSR(x,y,m,b):
	return 0 					# FIXME!

#
#  STEP 3 ---- Get data, plot it
#


#
#  STEP 5 ---- Plot example function
#

#
#  STEP 7 ---- Find SSR for poor fit from example function
#

#
#  STEP 8 ---- Make lists for possible slopes and
#              intercepts, then print them
#

slopes = []
for i in range(-50,50):
	slopes.append( i/10.0 )

#
#  STEP 9 ---- Find slope and intercept that minimize
#              the RSS
#
bestSlope = 0
bestInter = 0
minSSR = 10000

#
#  STEP 10 ---- Plot Result
#
#


#
#  STEP 11 ---- Plot Residuals
#
#

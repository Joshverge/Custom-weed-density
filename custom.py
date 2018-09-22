import wx
import re
import tempfile
import numpy as np
import os.path
import matplotlib.pyplot as plt
import math
import os

a = [1]
a[0] = 1

def getData(filename):
    print "Plotting : ", str(filename)
    fileIn = open(filename,'r')
    fileStr = fileIn.read()
        #print "CSV all"
    data = np.genfromtxt(filename, unpack=True, delimiter=',',skip_header=2) #unpack=True flips data


    return data

def dlatlon2xy(lat, lon, xoffset=0, yoffset=0 ): #converts lat and lon to x and y

    rlat1 = []
    rlat2 = []
    rlon1 = []
    rlon2 = []
    dlat = []
    dlon = []
    dx = []
    dy = []
    x = []
    y = []
    R = 6371000
    i=0

    for j in range(len(lat)):
        x.append(0) #  X AND Y offset are interchanged again
        y.append(0) #

    while i < len(lat)-1:
        rlat1.append(lat[i]*math.pi/180);
        rlat2.append(lat[i+1]*math.pi/180);
        rlon1.append(lon[i]*math.pi/180);
        rlon2.append(lon[i+1]*math.pi/180);

        dlat.append(rlat2[i] - rlat1[i])
        dlon.append(rlon2[i] - rlon1[i])

        dx.append(R*dlon[i]*math.cos((rlat1[i]+rlat2[i])/2))
        dy.append(R*dlat[i])

        if i==0:
            x[i] += dx[i] + yoffset #X & Y offset are interchanged as plotdata
            y[i] += dy[i] + xoffset #X & Y offset are interchanged as plotdata

        else:
            x[i] = dx[i] + x[i-1]
            y[i] = dy[i] + y[i-1]
        i+=1

    return (x, y)





rootDir = '/home/companion/DropPlot/weed custom script/Weed density'

cap = []
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found Directory: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)

        datalogVals = getData(dirName +'/' + fname)
        print("printing vals")
        cap.extend(datalogVals[56])

# norm = [float(i)/max(cap) for i in cap]

for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found Directory: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)

        datalogVals = getData(dirName +'/' + fname)

        mpc_llx, mpc_lly = dlatlon2xy(datalogVals[25],datalogVals[26] )
        plt.scatter(mpc_lly, mpc_llx,s=1,c=datalogVals[56],cmap='jet',label='Weed density')



    foldername = os.path.basename(dirName)
    print(foldername)
    plt.xlabel('x (m)', fontsize=16)
    plt.ylabel('y (m)', fontsize=16)
    plt.savefig(foldername, dpi=800)
    # plt.show()

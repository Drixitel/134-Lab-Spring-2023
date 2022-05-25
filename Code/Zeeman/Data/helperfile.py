#packages needed 
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.colors as colors
import pandas as pd 

from astropy.visualization import astropy_mpl_style
from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits

from scipy.optimize import curve_fit
import scipy.stats as stat
from scipy.signal import argrelextrema
from scipy.signal import find_peaks
from scipy.misc import electrocardiogram


# Collect Data
def GetImage(fitfile): 
    '''Takes: .fit file
        Returns: file, data  (n,m) for n rows and m colums, file info '''
    file = get_pkg_data_filename(fitfile)
    image_data = fits.getdata(file, ext = 0)
    return file, image_data, fits.info(file)

def CreateData(txtfilename):
    ''' Takes: .txt file (must only contain 2 columns)
        Returns: arrays: x,y = Bins, Intensities'''
    #Declare lists  
    bins = []
    intensities = []
    #read file
    f = open(txtfilename, 'r')
    #loop and campartmentaize 
    for row in f: 
        row = row.split()
        bins.append(int(row[0]))
        intensities.append(int(row[1]))
    return bins, intensities


# Plotting
def PlotRings(image_data, title, xlabel, ylabel, invert = True, figsize0 = 'a', figsize1 = 'a'): 
    '''Specifics for Ploting Ring image'''
    # Style
    plt.style.use(astropy_mpl_style)
    # plt.style.use('bmh')
    hfont = {'fontname':'Consolas'}
    if figsize0 and figsize1 == 'a': 
        print('Ratio set to Default:  (12,10)')
        fig, axes = plt.subplots(figsize= (12,10))
    elif figsize0 and figsize1 != 'a': 
        print(f"Ratio override to ({figsize0},{figsize1})")
        fig, axes = plt.subplots(figsize= (figsize0,figsize1))

    #plot
    axes.imshow(image_data, cmap = 'gray', norm= colors.PowerNorm(gamma=0.5))

    #labels 
    axes.set_title(title, **hfont)
    axes.set_ylabel(ylabel, **hfont)
    axes.set_xlabel(xlabel, **hfont)
    if invert == True: 
        plt.gca().invert_yaxis()
    else: 
        plt.gca()

    return  

def Plots(x, y, title, xlabel, ylabel, xrange = [ -1 , -1 ] , yrange = [ -1 , -1 ], figsize0 = 'a', figsize1 = 'a'):
    '''Plots anything but plots Intensities really well'''
    #style plot
    if figsize0 != 'a' and figsize1 != 'a': 
        print(f'Ratio set : ({figsize0}, {figsize1})')
        fig, axes = plt.subplots(figsize= (figsize0,figsize1))
        
    elif figsize0 == 'a' and figsize1 == 'a': 
        print('Data ratio set')
        fig, axes = plt.subplots()
        if yrange == [ -1 , -1 ] :
            yspan = max(y) - min(y)
            yrange =[ min(y) - yspan/10. , max(y) + yspan/10. ]
            plt.ylim( yrange )
        if xrange == [ -1 , -1 ] :
            xspan = max(x) - min(x)
            xrange = [ min(x) - xspan/10. , max(x) + xspan/10. ]
            plt.xlim( xrange )

    plt.style.use(astropy_mpl_style)
    hfont = {'fontname':'Consolas'}

    #plot
    axes.plot(x, y, label= 'File Data', color='blue')

    #labels 
    axes.set_title(title, **hfont)
    axes.set_ylabel(ylabel, **hfont)
    axes.set_xlabel(xlabel, **hfont)
    return 

def SaveFigure(filename):
    '''If you forget the keyword'''
    plt.savefig(filename, bbox_inches ='tight' )
    return

def LabelPeaks_ShrinkData( xvalues, yvalues, lowerxlim, upperxlim, lowerylim): 
    ''' Takes: Original bulk data (x,y) and limits to truncate the data
        Returns: The desired peaks and the truncated data (xnew,ynew)'''
    #Find bin x-values to associated local y-Max values
    peaks, _ = find_peaks(yvalues, distance=25)

    #Label the associated y-Max values
    all_ymax = yvalues[peaks]

    #forloop/zip: This applies the truncation on the Peak values ONlY
    #For p value our zip set (bin,intensity)
    #if: select the range of peaks we want
    #and: select the limit of intensity values
    tru_peaks = [p for (p,y) in zip(peaks,all_ymax) if ((p >= lowerxlim and p<= upperxlim) and y >= lowerylim)]

    # Truncate the data to make the peak values 
    new_yvalues =[]
    new_xvalues =[]
    for n in xvalues: 
        if n >= lowerxlim and n <= upperxlim:
            new_xvalues.append(n)
            new_yvalues.append(yvalues[n])
        else: 
            continue
    return tru_peaks, new_xvalues, new_yvalues

def PlotNewPeaks(newpeaks, OG_intensities ):
    '''Just a specific way to plot the Peaks with a red (x)'''
    plt.plot(newpeaks, OG_intensities[newpeaks], 'x', color ='red', label = 'Peaks')
    return

# Gaussian Fitting 
def gaussian( x , *p ) :
    return np.absolute( p[0] ) * np.exp( -( x - p[1] )**2/( 2*p[2]**2 ) )

def ZeemanPeakfit(x, *p): 
    '''Attempting with only one Gaussian - anything greater made sifting harder'''
    return  1200 + gaussian( x , *p[0:3] )  

def PeakBinValuesbyfit(fitfunction, newx, newy, NewPeaks, OG_intensity, AmpAdjust, ShiftAdjust, p0 = 1):
    ''' Takes: Fitfunction, the new data (xnew,ynew), the original yvalues, 
                our small adjustments of Amp and x-shift
        Returns: Parameters for all fitGausians and the mean bin location of our peaks 
                    This is the mean parameter of our gaussian'''
    #convert list to array - new version should be one value
    peak = np.array(NewPeaks)
    #empty array becomes out initial guesses for the fit - should be 3 values
    p = np.zeros(len(peak)*3)
    #counter
    if p0 == 1:
        print('Default input parameters chosen: random')
        n = 0 
        p[n] = OG_intensity[peak][n] + AmpAdjust
        #Shift
        p[n+1] = peak[n]+ShiftAdjust
        #factor
        p[n+2] = np.random.uniform(0.6,0.9)
        
    elif p0 != 1: 
        print('Default input parameters overriden')
        n = 0 
        p[n] = OG_intensity[peak][n] + AmpAdjust
        #Shift
        p[n+1] = peak[n]+ShiftAdjust
        p[2] = p0[0]
    print(p)
    #fit 
    # sigma = np.random.uniform(100,200, len(newy))

    popt , pcov = curve_fit( fitfunction, newx, newy, p0 = p, absolute_sigma=True, maxfev=2000)

    #Paramerters of our gaussians 
    popt1 = np.array(popt)
    #Take the 2nd term of each set of 3 
    peakbinvalues = []
    for i in range(1, len(popt), 3): 
        peakbinvalues.append(popt[i])
    
    return popt, peakbinvalues


# Radius from 2 pixel values 
def RadiusMicoMeter(bin1,bin2):
    ''' Takes: final desired Bin-Peak locations
        Returns: radius values from the inner peak to the outer peak
                 in micro-meters'''
    b1 = np.array(bin1)
    b2 = np.array(bin2)
   
    diameter = abs(b1 -b2)

    radius = diameter/2
    #reverse the order: inner ring is now first 
    # radius = radius[::-1]
    #convert to micrometer (per pixel) is (9um x 9um)
    radius_micometer = radius*9

    return radius_micometer

def RadiusValuesInner_to_Outer(peakbinsvalues):
    ''' Takes: final desired Bin-Peak locations
        Returns: radius values from the inner peak to the outer peak
                 in micro-meters'''
    start = 0
    end = len(peakbinsvalues) - 1
    diameter = []
    while start < end:
        # Create pairs taking from the start and the end of the list
        pair = (peakbinsvalues[start], peakbinsvalues[end])
        # take their difference 
        diameters = abs(pair[0] - pair[1])
        # Round
        d = np.round(diameters, decimals=3)
        diameter.append(d)
        # iterate 
        start += 1
        end -= 1
    #list to array - this list is diameters from the outer rings to the inner rings
    diameter = np.array(diameter)
    #convert to radius
    radius = diameter/2
    #reverse the order: inner ring is now first 
    radius = radius[::-1]
    #convert to micrometer (per pixel) is (9um x 9um)
    radius_micometer = radius*9
    return radius_micometer 

# Chi^2 Values 

def Chi2Values(fitfunction, xdata, ydata, fitparams, ysigma):
    yfit = fitfunction(xdata, *fitparams)

    chisq = sum( (ydata - yfit)**2 / ysigma**2 )

    ndf = len(ydata)-len(fitparams)

    chisq_reduced = chisq/float(ndf)

    cdf = stat.chi2.cdf(chisq, df = ndf)

    pvalue = 1-cdf

    print('Chi-square: ',chisq)
    print('Degrees of freedom: ',ndf)
    print('Reduced chi-square: ',chisq_reduced)
    print('CDF: ', cdf)
    print('p-test value: ',pvalue)

    return
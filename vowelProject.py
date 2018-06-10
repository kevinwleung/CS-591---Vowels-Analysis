'''
Kevin Leung
CS591 - Computational Audio 
Wayne Snyder

vowelProject.py

Objective: To differentiate standard English vowel sounds from IPA
chart through computation of the .wav waves using SciPy
FFT and finding the frequency spectrum and manipulating data from
the spectrum. ***Uncomment print statements when necessary***

The standard English vowels analyzed are u, i, ɛ, ɘ, e, ɔ, æ and ɒ

CREDIT FOR FINDING FREQUENCY SPECTRUM: 
Lines 30-40 and 145 are borrowed from:
http://stackoverflow.com/questions/23377665/python-scipy-fft-wav-files
'''

import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile # get the api

'''
analyzeVowel - This converts the data of .wav file to array.
SciPy FFT is used to find the frequency spectrum which is further
analyzed to determine what the vowel the .wav file is.
'''
def analyzeVowel(fs, data):
    a = data.T[0] # this is a two channel soundtrack, I get the first track
    b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
    c = fft(b) # calculate fourier transform (complex numbers list)
    d = len(c)/2  # you only need half of the fft list (real signal symmetry)
    
    FS = abs(c[:(d-1)])
    print()
    
    # Plot points. X axis = frequency, Y axis = magnitude
    plt.plot(FS,'r')
    plt.show()
    
    # Length of the wav file
    #print("Length: " + str(len(FS)))
    
    max = 0
    for x in range(0, len(FS)):
        if FS[x] > max:
            max = int(FS[x])
    
    # The highest peak in the spectrum
    #print("Peak1: " + str(max))
    
    # Where we begin next in the array to look for the next
    # highest peak
    begin = int(0.06*len(FS))
    
    
    #print("Begin to Find Peak2: " + str(begin))
    
    # maxLimit is the number of the magnitude value (y-axis)
    # that is the magnitude of max2 (2nd largest peak)
    # should be lower than, to be a "u" vowel
    maxLimit = int(0.02 * max)
    
    #print("Peak Limit: " + str(maxLimit))
    
    #represents the x-axis of the 2nd largest peak
    max2X = 0
    #represents y-axis value for 2nd largest peak
    max2 = 0
    for x in range(begin, len(FS)):
        if FS[x] > max2:
            max2 = int(FS[x])
            max2X = x
    
    #print("X-Axis of 2nd Peak: " + str(max2X))
            
    #print("Peak2: " + str(max2))
    #print("Peak1/Peak2 Ratio: " + str(max2/max))
    
            
    if max2 < maxLimit:
        return('u')
    
    # in order for vowel to be "i", 2nd largest peak (max2)
    # must be between maxLimitIUpper & maxLimitILower    
    maxLimitILower = 0.35 * max
    maxLimitIUpper = 0.6 * max
    
    if FS[int(0.06*len(FS))] < 0.3 * max:
        if max2 >= maxLimitILower:
            if max2 <= maxLimitIUpper:
                if FS[int(0.28*len(FS))] < 0.01 * max:
                    return('i')

    # in order for vowel to be "ɔ or ɒ", 2nd largest peak (max2)
    # must be between maxLimitIUpper & maxLimitILower       
    maxLimitLower2 = 0.025 * max  
    maxLimitUpper2 = 0.11 * max
    
    if max2 >= maxLimitLower2:
        if max2 <= maxLimitUpper2:
            return('ɔ or ɒ')
       
    # Frequency spectrums of ɘ, e, æ and ɛ look relatively similar
    # Therefore cannot be analyzed
    return('either ɘ, e æ or  ɛ')

'''
Main Method: Prints out what vowel the .wav file is. 
There are three sets of the same vowels to use for comparison.

name represents file name
'''
def main():
    '''
    NOTE: Uncomment the line corresponding to the folder of wav
    files of vowels you want to choose below.
    '''

    folder = "Vowels1/"
    #folder = "Vowels2/"
    #folder = "Vowels3/"

    '''
    NOTE: Uncomment the line corresponding to the wav file of the specific
    vowel you want to choose below.
    '''
    

    #fileName = folder + 'u.wav'
    #fileName = folder + 'i.wav'
    #fileName = folder + 'ɛ.wav'
    #fileName = folder + 'ɘ.wav'
    #fileName = folder + 'e.wav'
    #fileName = folder + 'ɔ.wav'
    #fileName = folder + 'æ.wav'
    fileName = folder + 'ɒ.wav'

    print()
    print()
    print("***Analzying wav file: " + str(fileName)+"***")
    print()
    
    fs, data = wavfile.read(fileName) # load the data
    
    # call function to analyze vowels and print results
    print("Result: " + "The vowel from " + fileName + " is: " +\
        analyzeVowel(fs, data))

#Run main method
main()
            

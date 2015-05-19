import wave

import numpy
import pygame


# # # # #
# CONSTANTS

# sound length (seconds, a float)
SOUNDLEN = 3.0

# maximal amplitude
MAXAMP = 32767 / 2
# sampling frequency (in Herz: the number of samples per second)
SAMPLINGFREQ = 48000
# the number of channels (1=mono, 2=stereo)
NCHANNELS = 2


# # # # #
# PREPARE

# initialise mixer module
pygame.mixer.init(frequency=SAMPLINGFREQ, channels=NCHANNELS)

# create an array of random numbers
noise = numpy.random.rand(SOUNDLEN * SAMPLINGFREQ) * MAXAMP
if NCHANNELS == 2:
	noise = numpy.repeat(noise, 2, axis=0)
	noise.reshape(len(noise)/2,2)

# create a sound from the list
snd = pygame.mixer.Sound(noise.astype('int16'))


# # # # #
# WAVE IT UP
	
# open new wave file
sfile = wave.open('white_noise.wav', 'w')

# set the parameters
sfile.setframerate(SAMPLINGFREQ)
sfile.setnchannels(NCHANNELS)
sfile.setsampwidth(2)

# write raw PyGame sound buffer to wave file
sfile.writeframesraw(snd.get_buffer().raw)

# close file
sfile.close()

import wave

import numpy
import pygame


# # # # #
# CONSTANTS

# sound length (seconds, a float)
SOUNDLEN = 3.0
# sound frequency (in Herz: the number of vibrations per second)
SOUNDFREQ = 1000

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

# calculate the amount of sound cycles in the lenght of this sound
ncycles = SOUNDLEN * SOUNDFREQ
# calculate the amount of samples per cycle
spc = int((SAMPLINGFREQ * SOUNDLEN) / ncycles)

# create a single vibration (range with stepsize = number of samples per cycle)
sine = numpy.arange(0, 2*numpy.pi, (2*numpy.pi)/spc)
# sine is now just increasing numbers between 0 and 2 pi. Apply a sinusoid to
# make them into a wave function
sine = numpy.sin(sine)
# multiply the current numbers by the maximum amplitude to make audible sound
sine *= MAXAMP

# repeat the single cycle as much as we need to fill the current sound
sine = numpy.hstack(int(ncycles)*list(sine))
# for stereo: double the samples, and reshape the single array to two arrays
if NCHANNELS == 2:
	sine = numpy.repeat(sine, 2, axis=0)
	sine.reshape(len(sine)/2,2)

# create a sound from the list
snd = pygame.mixer.Sound(sine.astype('int16'))


# # # # #
# WAVE IT UP
	
# open new wave file
sfile = wave.open('pure_tone.wav', 'w')

# set the parameters
sfile.setframerate(SAMPLINGFREQ)
sfile.setnchannels(NCHANNELS)
sfile.setsampwidth(2)

# write raw PyGame sound buffer to wave file
sfile.writeframesraw(snd.get_buffer().raw)

# close file
sfile.close()

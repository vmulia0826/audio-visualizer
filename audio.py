import wave
import pandas
from matplotlib import pyplot as plt
import numpy

wav_obj = wave.open('hard_choices.wav', 'rb')
# samples of the sound taken every second
sample_freq = wav_obj.getframerate()

# sample frequency quantifying the number of samples per second
n_samples = wav_obj.getnframes()

#length of our audio file in seconds
t_audio = n_samples/sample_freq


#number of channels
n_channels = wav_obj.getnchannels()

#values of the signal or amplitude of the wave at point in time
signal_wave = wav_obj.readframes(n_samples)

#Turn to numpy from object byte
signal_array = numpy.frombuffer(signal_wave, dtype=numpy.int16)

#print(len(signal_array)) #6273024 elements found

#split the data into individual channels
l_channel = signal_array[0::2]
r_channel = signal_array[1::2]




# our left and right channels are separated

#Plotting the Signal Amplitude

#Obtaining the time at which each sample is taken
times = numpy.linspace(0, n_samples/sample_freq, num=n_samples)


plt.figure(figsize=(15, 5))
plt.plot(times, l_channel)
plt.title('Left Channel')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.show()
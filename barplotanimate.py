import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import librosa
import pyaudio
import wave


#Start Pyaudio Stream

CHUNK = 1024
FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 1
WAVE_OUTPUT_FILENAME = "output1.wav"

p = pyaudio.PyAudio()

print p.get_default_input_device_info()

stream = p.open(input_device_index = 0, format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=1024)
############




def get_chroma(stream):
    wav_bytes= stream.read(1024, exception_on_overflow = False)
    np_floats = librosa.util.buf_to_float(wav_bytes, 4)
    chromagram = librosa.feature.chroma_cqt(y=np_floats , sr = 44100)
    return chromagram[0]


def animate(frameno):
    # x = mu + sigma * np.random.randn(N)
    x = get_chroma(stream)
    n, _ = np.histogram(x, bins, normed=True)
    for rect, h in zip(patches, n):
        rect.set_height(h)
    return patches

N, mu, sigma = 10000, 100, 15
fig, ax = plt.subplots()

#x = mu + sigma * np.random.randn(N)
x=get_chroma(stream)
print len(x)

n, bins, patches = plt.hist(x, normed=1, facecolor='green', alpha=0.75)
plt.axis([0, 1, 0, 10])
frames = 10000
ani = animation.FuncAnimation(fig, animate, blit=True, interval=0,
                              frames=frames,
                              repeat=False)
plt.show()
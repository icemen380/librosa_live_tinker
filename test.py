import matplotlib.pyplot as plt
import librosa
import pyaudio
import wave
import numpy
#start pyaudio stream

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
                frames_per_buffer=CHUNK)

print("* recording")


# stream.stop_stream()
# stream.close()
# p.terminate()
#
# wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()
#





#y, sr = librosa.load('test.wav')
#plt.figure(figsize=(12, 8))


for i in range (0,10):
    # frames = []
    #
    # for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    #     data = stream.read(CHUNK)
    #     frames.append(data)
    data= stream.read(512)
    #numpy float:
    strm=[]
    nfloat = librosa.util.buf_to_float(data, 4)
    #print nfloat

    #print len(nfloat)
    # for ch in range(CHUNK):
    #     flt=data[ch*4:ch*4+4]
    #     nfloat = librosa.util.buf_to_float(flt,4)
    #     strm.append(nfloat)
    #     #print nfloat

    # npar=numpy.asarray(strm)
    # print strm[400]
    # print npar[400]
    #y,sr = librosa.load(frames)
        #
    chromagram = librosa.feature.chroma_cqt(y=nfloat , sr = 44100)
    print chromagram
    plt.hist(chromagram, 12 ,normed=False,alpha=1)
    plt.show()
    # plt.subplot(4,2,5)
    # librosa.display.specshow(chromagram, y_axis='chroma')
    # plt.colorbar()
    # plt.title('chroma')
    # plt.tight_layout()
    # plt.show()
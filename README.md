# librosa_live_tinker
Testing live audio functionality with the librosa sound processing libray


Librosa ["http://librosa.github.io/"] does lots of sound processing in python. Right now I'm focused on the Chromagram functionality, which bins the frequency spectrum into the twelve notes. By analyzing these bins, we can make a guess of what chord is being played in the audio signal.


There are a lot of programs that do this, but I'm having trouble finding anything that does it in realtime. Supercollider (which is generally well suited to live stuff), does produce a live chromagram, though I'm not well versed in programming in it.


I'm taking a shot at running the librosa modules on live audio as librosa does things like provide the chromagram in a convenient numpy array.


The goal is to take data from a pyAudio input stream and feel it into the librosa modules. The fundamental problem is that the pyAudio data is in byte arrays (raw PCM I believe), and librosa wants numpy arrays with floats.


The answer appears that librosa already has the code to do this with a call to librosa.util.buf_to_float(byte array, size_of_PCM data). 
The challenges after that are verifying that this audio stream data is actually coming through correctly, and after that handling the buffering of the pyAudio stream, especially if we're trying to do other stuff. It's probably best to have the stream-to-chromagram going on in its own thread.

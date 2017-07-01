# scope waveforms
to save space, all waveforms were converted from .txt format to .npz format using convert.py  
open with ´A = np.load('file.npz')['arr_0']´.  

## folder contents
* 20Hz: (time (ms), current (mA), voltage (V))
* 10kHz: (time (us), current (mA), voltage (V))
* phototransistor: (time (ms), current (mA), voltage (V)) file name is voltage of light bulb used to illuminate phototransistor
* piezo: (time (ms), voltage (V)) just some pretty waveforms

all but piezo contain one cycle of current and voltage used to plot current-voltage characteristics

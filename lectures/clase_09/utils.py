import numpy as np
import keras
import keras.backend as K

def sin_wave(secs, freq, sr, gain):
    '''
    Generates a sine wave of frequency given by freq, with duration of secs.
    '''
    t = np.arange(sr * secs)
    return gain * np.sin(2 * np.pi * freq * t / sr)


def whitenoise(gain, shape):
    '''
    Generates white noise of duration given by secs
    '''
    return gain * np.random.uniform(-1., 1., shape)

def chord_wave(secs, f0, sr, gain, major):
    """major: bool"""
    t = np.arange(sr * secs)
    sine_f0 = gain * np.sin(2 * np.pi * f0 * t / sr)
    if major:
        sine_third = gain * np.sin(2 * np.pi * f0 * 2. ** (4./12.) * t / sr)
    else:
        sine_third = gain * np.sin(2 * np.pi * f0 * 2. ** (3./12.) * t / sr)
    return sine_f0 + sine_third

def add_channel_axis(cqt):
    if K.image_data_format == 'channels_first':
        return cqt[np.newaxis, :, :]
    else:
        return cqt[:, :, np.newaxis]
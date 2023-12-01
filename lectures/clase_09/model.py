import numpy as np
import librosa 
from tensorflow.keras.utils import Sequence
from utils import sin_wave, whitenoise, chord_wave, add_channel_axis
import keras
import keras.backend as K
from future.utils import implements_iterator  



class DataGenerator(Sequence):
    def __init__(self, sr=16000, batch_size=128):
        np.random.seed(1209)
        self.pitches = [440., 466.2, 493.8, 523.3, 554.4, 587.3,
                        622.3, 659.3, 698.5, 740., 784.0, 830.6]
        self.sr = sr
        self.n_class = 2
        self.secs = 1.
        self.batch_size = batch_size
        self.labels = np.eye(self.n_class)[range(0, self.n_class)]

        #placeholder : espacio donde guardo informacion
        self.major_cqts = []
        self.minor_cqts = []

        for freq in self.pitches:
            cqt_major = librosa.cqt(chord_wave(self.secs, freq, self.sr, gain=0.5, major=True), sr=self.sr,
                                    fmin=220, n_bins=36, filter_scale=2)[:, 2:5]
            cqt_major = librosa.amplitude_to_db(cqt_major, ref=np.min)
            cqt_major = cqt_major / np.max(cqt_major)
            self.major_cqts.append(add_channel_axis(cqt_major))

            cqt_minor = librosa.cqt(chord_wave(self.secs, freq, self.sr, gain=0.5, major=False), sr=self.sr,
                                    fmin=220, n_bins=36, filter_scale=2)[:, 2:5]
            cqt_minor = librosa.amplitude_to_db(cqt_minor, ref=np.min)
            cqt_minor = cqt_minor / np.max(cqt_minor)
            self.minor_cqts.append(add_channel_axis(cqt_minor))

        self.cqt_shape = add_channel_axis(cqt_minor).shape

    # metodo privado
    def __len__(self):
        total_samples = len(self.major_cqts)
        return total_samples * 2

    def __getitem__(self, index):
        #print(f"Fetching batch {index}")
        choice = np.random.choice(12, size=self.batch_size // 2, replace=True)
        noise_gain = 0.1 * np.random.random_sample(1)
        noise = whitenoise(noise_gain, self.cqt_shape)

        xs = [noise + self.major_cqts[i] for i in choice]
        xs += [noise + self.minor_cqts[i] for i in choice]

        ys = np.eye(2)[np.hstack((np.zeros(self.batch_size // 2, dtype=int),
                                  np.ones(self.batch_size // 2, dtype=int)))]

        return np.array(xs, dtype=np.float32), np.array(ys, dtype=np.float32)

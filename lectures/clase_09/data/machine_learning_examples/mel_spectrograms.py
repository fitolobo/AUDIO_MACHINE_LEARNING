import time
import os
import librosa
import numpy as np
import tensorflow

def procesando_data_path(path,sample_rate,separador,add_silence=False):
    lst = []

    start_time = time.time()
    count = 0
    for subdir, dirs, files in os.walk(path):
        for file in files:
            #print(file)
            count += 1
            try:
                ##Load librosa array, obtain mfcss, store the file and the mcss information in a new array
                X, sample_rate = librosa.load(os.path.join(subdir,file), res_type='kaiser_fast')
                
                if add_silence == True:
                    X = concatenate_segments(X, sr=sample_rate, pad_time=1)
                # Keras Model
                mfccs = librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T
                file = int(file.split(separador)[2])  # solo cambió esto!
                arr = mfccs, file
                lst.append(arr)
          # If the file is not valid, skip it
            except ValueError:
                continue
            if count == 1:
                break
    print("Total Number of Audio Files")
    print(count)
    print("--- Data loaded. Loading time: %s seconds ---" % (time.time() - start_time))
    
    return lst
import pandas as pd
import numpy as np
import os
import soundfile as sf
from sklearn import svm, linear_model
from scipy.fftpack import fft
from scipy.signal import stft


def main():
    # read in meta data
    md_df = pd.read_csv('data/birdsong_metadata.csv')

    # make file id, species dict
    species_id = dict()
    for index, row in md_df.iterrows():
        id = md_df['file_id'][index]
        species = md_df['english_cname'][index]
        species_id[id] = species

    print(species_id)

    # read in sound data
    s_path = os.path.join('data', 'songs', 'songs')
    files = [f for f in os.listdir(s_path) if os.path.isfile(os.path.join(s_path, f))]

    # make sound species list
    sound_labels =list()
    for file in files:
        data = read_song(path=s_path, file=file)
        name = bird_name(file, species_id)
        sound_labels.append((name, data))

    y = [point[0] for point in sound_labels]
    print(y)
    X = [point[1] for point in sound_labels]
    print(X)

    # sc_y = sklearn.preprocessing.StandardScaler()
    # y = sc_y.fit_transform(y)
    print('training')
    # reg = linear_model.LinearRegression()
    model = svm.SVC(probability=True)
    model.fit(X, y)

    print(sound_labels)
    y = 0
    n = 0
    for bird in sound_labels:
        pred = model.predict([bird[1]])
        if bird[0] == pred[0]:
            y += 1
        else:
            n += 1
    print('y:', y)
    print('n:', n)

def read_song(path, file):
    data, samplerate = sf.read(os.path.join(path, file))
    # fft_data = np.abs(fft(data, n=128*4096))
    s = np.abs(stft(data, 1 / samplerate))
    return s

def bird_name(file, species_dict):
    id = int(file[2:-5])
    return species_dict[id]

main()


# import meta data

# for sample in samples
    # train_set = smaples - sample
    # train model with sklearn svm
    # save model to models
    # test on sample

# average all models
# output model weights 
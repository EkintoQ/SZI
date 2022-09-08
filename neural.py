import math
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Activation, Flatten
from keras.models import Sequential
from tqdm import tqdm

def create_training_data():
    DATADIR = "images"
    CATEGORIES = ["plastic", "other"]
    IMG_SIZE = 100
    training_data = []
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)  # 0 - plastic, 1 - other
        for img in tqdm(os.listdir(path)):
                try:
                    img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                    training_data.append([new_array, class_num])
                except Exception as e:
                    pass

    X = []
    y = []

    for features, label in training_data:
        X.append(features)
        y.append(label)

    X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    y = np.array(y)

    print("Training data created!")
    return X,y

def learn_neural_network(X,y):
    X = X/255.0

    model = Sequential()

    model.add(Conv2D(64, (3, 3), input_shape=X.shape[1:]))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())

    model.add(Dense(64))

    model.add(Dense(1))
    model.add(Activation('sigmoid'))

    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    model.fit(X, y, batch_size=1, epochs=1, validation_batch_size=0.1)

    return model

def prepare_img(filepath):
    IMG_SIZE = 100
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1) / 255

def predict(model, filepath):
    return model.predict([prepare_img(filepath)])

def result(prediction):
    if prediction[0][0] >= 0.65:
        print(prediction)
        print(math.ceil(prediction[0][0]))
        print('No plastic')
    elif prediction[0][0] < 0.65:
        print(prediction)
        print(math.floor(prediction[0][0]))
        print("Plastic")

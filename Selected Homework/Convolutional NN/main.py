# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YHIvw2XyA2XZbBG6X2xAzvumNOA8i_0i
"""

from google.colab import drive
drive.mount('/content/drive/')

# Commented out IPython magic to ensure Python compatibility.
import os
import numpy as np
from mlxtend.data import loadlocal_mnist
from sklearn.model_selection import train_test_split
import keras
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
import tensorflow as tf
import matplotlib.pyplot as plt
import timeit 

# %matplotlib inline

class mnist:
  def __init__(self):
    return None

  def load_mnist_from_file(self):
    if not os.path.exists("train-images-idx3-ubyte"):
      !curl -O http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
      !curl -O http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
      !curl -O http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
      !curl -O http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz
      !gunzip t*-ubyte.gz
          
    #Training dataset
    X_train, y_train = loadlocal_mnist(images_path="train-images-idx3-ubyte", labels_path="train-labels-idx1-ubyte")
    
    #Testing dataset
    X_test, y_test = loadlocal_mnist(images_path="t10k-images-idx3-ubyte", labels_path="t10k-labels-idx1-ubyte")

    #One hot encoding for y
    n_values = np.max(y_train) + 1
    y_train = np.eye(n_values)[y_train]

    #One hot encoding for y
    n_values = np.max(y_test) + 1
    y_test = np.eye(n_values)[y_test]

    
    X_train = X_train.reshape(X_train.shape[0], 28, 28, 1) / 255
    X_test = X_test.reshape(X_test.shape[0], 28, 28, 1) / 255

    print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
    return X_train, X_test, y_train, y_test, X_valid, y_valid

  def model(self):

    self.model = tf.keras.Sequential()
  
    self.model.add(tf.keras.layers.Conv2D(filters=4, kernel_size=(3, 3),strides=(1, 1), padding='valid', activation='relu', input_shape=(28, 28, 1)))

    self.model.add(tf.keras.layers.AveragePooling2D(pool_size=(2, 2), strides= (2,2) , name='pool_1'))

    self.model.add(tf.keras.layers.Conv2D(filters=2, kernel_size=(3, 3), strides=(3, 3), padding='valid', activation='relu', input_shape=(28, 28, 1)))

    self.model.add(tf.keras.layers.AveragePooling2D(pool_size=(4, 4), strides= (4,4) , name='pool_2'))

    self.model.add(tf.keras.layers.Flatten()) 

    self.model.add(tf.keras.layers.Dropout(0.2))

    self.model.add(tf.keras.layers.Flatten())

    self.model.add(tf.keras.layers.Dense(1000, activation='relu'))

    self.model.add(tf.keras.layers.Dropout(0.5))

    self.model.add(tf.keras.layers.Dense(10, activation='softmax'))


  def compile(self):
    self.model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

  def fit(self, X_train, X_test, y_train, y_test, batch_size = 100, epochs = 100):
    print('Fitting the model')
    print('Batch size: ', batch_size)
    print('Epochs: ', epochs)
    
    self.model.fit(X_train,
        y_train,
         batch_size=batch_size,
         epochs=epochs,
         validation_data=(X_test, y_test))

   


  def predict(self, X_valid, y_valid):
    prediction = model.predict([X_valid]) 
    return np.argmax(prediction[0])

  def modelEvaluation(self, x_test, y_test):
    loss, acc = self.model.evaluate(x_test, y_test)
    
    return loss, acc

  def summary(self):
    print(self.model.summary())

start = timeit.default_timer()


mnistDataset = mnist()

X_train, X_test, y_train, y_test, X_valid, y_valid = mnistDataset.load_mnist_from_file()

#Create Model
mnistDataset.model()

#compile model
mnistDataset.compile()

#Summary

mnistDataset.summary()

#Fit
mnistDataset.fit(X_train, X_test, y_train, y_test, batch_size = 100, epochs =10)

#Model Evaluation
val, acc = mnistDataset.modelEvaluation(X_test, y_test)

print("Validation score: ", val)
print("Accuracy: ", acc)

#time-stop
stop = timeit.default_timer()

#Total Time
print('Total time taken ', (stop - start))


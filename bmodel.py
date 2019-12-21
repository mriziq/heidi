# -*- coding: utf-8 -*-

from time import sleep

import keras

import random

import numpy as np

from collections import deque

from keras.models import Sequential
from keras.layers import Dense,Dropout
from keras.optimizers import Adam,SGD
from keras.utils import np_utils
from keras.utils import to_categorical
from keras.callbacks import ModelCheckpoint

from keras import backend as K

import pandas


colnames = ['Student', 'Internet' , 'Exam', 'GroupProject', 'Gender']
data = pandas.read_csv('~/Engineering/BUS194A/nida/data.csv', names=colnames)


gender = data.Gender.tolist()
internet = data.Internet.tolist()
exam = data.Exam.tolist()
group_project = data.GroupProject.tolist()


cheater = []
data_set = []
for i in range(len(exam)):
    if exam[i] == 1 or group_project[i] == 1:
        cheater.append(1)
    else:
        cheater.append(0)
    data_set.append([gender[i],internet[i]])



trainingData = data_set[0:-10]
trainingValues = cheater[0:-10]

testData = data_set[-10:-1]
testingValues = cheater[-10:-1]



# network and training
NB_EPOCH = 200 #Number of trials
BATCH_SIZE = 5 #optimal
VERBOSE = 4 #how much output you want
VALIDATION_SPLIT=0.1 # how much TRAIN is reserved for VALIDATION



(X_train, y_train), (X_test, y_test) = [[trainingData,trainingValues],[testData,testingValues]]#mnist.load_data()


y_train = np.array(y_train)

y_test = np.array(y_test)


X_train = np.array(X_train)
X_test = np.array(X_test)




X_train = X_train.astype('float32')

X_test = X_test.astype('float32')





model = Sequential()
model.add(Dense( 2, input_dim=2))
model.add(Dropout(0.5))
model.add(Dense(128,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='relu'))
adam = Adam()
model.compile(loss='mean_squared_error', optimizer=adam,metrics=['accuracy','mse'])


# Save the checkpoint in the /output folder
filepath = "cheater.hdf5"

# Keep only a single checkpoint, the best over test accuracy.
checkpoint = ModelCheckpoint(filepath,
                            monitor='val_mean_squared_error',
                            verbose=1,
                            save_best_only=True,
                            mode='min')
callbacks_list = [checkpoint]


history = model.fit( X_train, y_train,batch_size=BATCH_SIZE, epochs=NB_EPOCH,verbose=VERBOSE, validation_split=VALIDATION_SPLIT,
                    shuffle=True,callbacks=callbacks_list)

a = [ [3.,0.],[3.,0.],[3.,1.],[3.,1.]]
score = model.predict( np.array(a) )
print(a) # [3-> male 4-> female, 0 -> w/o internet, 1 -> w/ internet]
print(score) # percent chance of occuring

output = []
#for i in range(len(X_test)):
#    output.append([X_test[i],score[i]])

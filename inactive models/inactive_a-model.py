from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping
import pandas as pd

# DEEP LEARNING MODEL TO PREDICT ______ ? (EXAM CHEATING, MAJOR CHEATING RATE BASED ON___)

#import data and convert to dataframe

train_df = pd.read_csv("194A_data.csv", index_col="Student")

#creating dataframe with all training data except target prediction variable
train_X = train_df.drop(columns=['Gender'])

#target variable
train_Y = train_df[['Gender']]

#create model
model = Sequential()

#get number of columns in training data
n_cols = train_X.shape[1]

#adding neural net layers
model.add(Dense(10, activation='relu', input_shape=(n_cols,)))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='linear'))

#compiling the model using mean squared error as a measure of model performance
model.compile(optimizer='adam', loss='mean_squared_error')

#set early stopping monitor so the model stops training when it won't improve anymore
early_stopping_monitor = EarlyStopping(patience=3)

#train model
model.fit(train_X, train_Y, validation_split=0.2, epochs=50, callbacks=[early_stopping_monitor])

#predictions
test_x  = train_df.drop(columns=['Exam'])

test_y_predictions = model.predict(test_x)
print(test_y_predictions)

# 11/29/2019: NEED TO SPLIT DATA AND CONVERT TO BINOMIAL FORMAT
# https://towardsdatascience.com/building-a-deep-learning-model-using-keras-1548ca149d37

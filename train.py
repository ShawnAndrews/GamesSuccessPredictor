# Description: Given a file of CSV training data, train an ANN and output the model and weights to a folder
# to be loaded later. Note that CSV columns must match the size of the input + output layer.

import sys
import csv
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import InputLayer

SCRIPT_ARGS = 3
LAYER_1_SIZE = 34
LAYER_2_SIZE = 25
LAYER_3_SIZE = 1
NUM_EPOCHS = 500

if len(sys.argv) != SCRIPT_ARGS:
    sys.exit(-1)

# prepare training data
trainingInput = []
trainingOutput = []
with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        row = [float(i) for i in row]
        trainingOutput += [[row.pop()]]
        trainingInput += [row]
        line_count += 1
    print(f'Processed {line_count} lines.')
training_data = np.array(trainingInput, "float32")
target_data = np.array(trainingOutput, "float32")

# create model
model = Sequential([
    InputLayer(input_shape=(LAYER_1_SIZE,)),
    Dense(LAYER_2_SIZE, activation='relu'),
    Dense(LAYER_3_SIZE, activation='sigmoid')])
model.compile(loss='mean_squared_error',
              optimizer='adam',
              metrics=['binary_accuracy'])

# train
model.fit(training_data, target_data, epochs=NUM_EPOCHS, verbose=2)

# save model and weights to folder
model.save(sys.argv[2])

import numpy as np
import pandas as pd 
from collections import Counter 
from random import shuffle
import cv2

train_data = np.load('training_data.npy')

for data in train_data:
    img = data[0]
    direction = data[1]
    cv2.imshow('test', img)
    print(direction)
    if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
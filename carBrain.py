import numpy as np
import pandas as pd 
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

class ML:
    def __init__(self):
        print("done creating instance")
        self.nn=MLPClassifier(activation='logistic', solver='sgd', hidden_layer_sizes=(10,15),random_state=1)
        self.data=pd.read_csv('training_data.npy').as_matrix()
        self.x_train = self.data[0:300,1:]
        self.y_train = self.data[0:300,0]

    def train_data(self):
        self.nn.fit(self.x_train,self.y_train)
        print("done training ")
        self.x_test = self.data[21000:, 1:]
        self.actuall_label = self.data[21000:, 0]
        #single digit test 
        # d = self.x_test[8]
        # d.shape=(28,28)
        # print(d)
        # plt.imshow(d,cmap='gray')
        # plt.show()
        #preduct function 
        count = 0
        pred=self.nn.predict(self.x_test)
        for i in range(len(pred)):
            if pred[i]==self.actuall_label[i]:
                count=count+1
        print("predict ration" + str(count))
        print("accuracy" + str(count/len(pred)))

    def predict(self, in_oneRaw):
        print(" Driection prediction : ")
        print(self.nn.predict(in_oneRaw))
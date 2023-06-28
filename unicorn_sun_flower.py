# Mindful Fitness

#Import needed modules
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split

#Create a class for Mindful Fitness
class MindfulFitness:

    def __init__(self):
        self.fitness_data = None
        self.model = None
 
    #Function to load the data
    def load_data(self, file_name):
        self.fitness_data = pd.read_csv(file_name)
 
    #Function to preprocess the data
    def preprocess_data(self):
        self.fitness_data.dropna(inplace=True)
        self.fitness_data.reset_index(drop=True)
 
    #Function to create the train/test split
    def train_test_split(self, test_size):
        train, test = train_test_split(self.fitness_data, test_size=test_size, random_state=42)
        return train, test
 
    #Function to create the model
    def create_model(self, model):
        self.model = model
 
    #Function to fit the model
    def fit_model(self, X_train, Y_train):
        self.model.fit(X_train, Y_train)
 
    #Function to make predictions
    def predict(self, X_test):
        predictions = self.model.predict(X_test)
        return predictions
 
    #Function to evaluate the model
    def evaluate_model(self, X_test, Y_test):
        error = np.mean(np.abs(Y_test - self.predict(X_test)))
        return error
 
#End of Class Definition

#Function to run the program
def run_program(file_name, model, test_size):
    #Create an instance of the Mindful Fitness class
    mf = MindfulFitness()
 
    #Load the data
    mf.load_data(file_name)
 
    #Preprocess the data
    mf.preprocess_data()
 
    #Create the train/test split
    train, test = mf.train_test_split(test_size)
 
    #Separate the features (X) and targets (Y)
    X_train = train.iloc[:, :-1]
    Y_train = train.iloc[:, -1]
    X_test = test.iloc[:, :-1]
    Y_test = test.iloc[:, -1]
 
    #Create the model
    mf.create_model(model)
 
    #Fit the model
    mf.fit_model(X_train, Y_train)
 
    #Make predictions
    predictions = mf.predict(X_test)
 
    #Evaluate the model
    error = mf.evaluate_model(X_test, Y_test)
    print("Mean Absolute Error:", error)
 
#End of Function Definition

#Main Function
if __name__ == 'main':
    file_name = 'fitness_data.csv'
    model = LinearRegression()
    test_size = 0.2
    run_program(file_name, model, test_size)
 
#End of Code
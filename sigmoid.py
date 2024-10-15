import math

class Neuron:
    # init class 
    def __init__(self, values):
        self.values = values
        
    # calculate sigmoid
    def sigmoid(self,x):
        return 1 / (1 + math.exp(-x))

    def calculate_all(self):
        return [self.sigmoid(x) for x in self.values]


x_values = [2, 3]  # Input list
calculator = Neuron(x_values)  # Create an object of the class
result = calculator.calculate_all()  # Call the method to get the results
print(f"Sigmoid({x_values}) = {result}")  # Output the result



    



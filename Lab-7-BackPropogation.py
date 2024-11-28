import math
import random

def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))

def sigmoid_derivative(x):
    return x * (1.0 - x)

def init_network(input_size, hidden_size, output_size, learning_rate):
    weights_input_hidden = [[random.uniform(-0.5, 0.5) for _ in range(hidden_size)] for _ in range(input_size)]
    weights_hidden_output = [[random.uniform(-0.5, 0.5) for _ in range(output_size)] for _ in range(hidden_size)]
    
    return {
        'input_layer': [0.0] * input_size,
        'hidden_layer': [0.0] * hidden_size,
        'output_layer': [0.0] * output_size,
        'weights_input_hidden': weights_input_hidden,
        'weights_hidden_output': weights_hidden_output,
        'learning_rate': learning_rate
    }

def forward(network, inputs):
    hidden_layer = [0.0] * len(network['hidden_layer'])
    output_layer = [0.0] * len(network['output_layer'])
    
    for i in range(len(hidden_layer)):
        hidden_layer[i] = 0.0
        for j in range(len(inputs)):
            hidden_layer[i] += inputs[j] * network['weights_input_hidden'][j][i]
        hidden_layer[i] = sigmoid(hidden_layer[i])
    
    for i in range(len(output_layer)):
        output_layer[i] = 0.0
        for j in range(len(hidden_layer)):
            output_layer[i] += hidden_layer[j] * network['weights_hidden_output'][j][i]
        output_layer[i] = sigmoid(output_layer[i])
    
    network['hidden_layer'] = hidden_layer
    network['output_layer'] = output_layer
    
    return output_layer

def backpropagate(network, inputs, targets):
    output_errors = [0.0] * len(network['output_layer'])
    hidden_errors = [0.0] * len(network['hidden_layer'])
    
    for i in range(len(network['output_layer'])):
        output_errors[i] = (targets[i] - network['output_layer'][i]) * sigmoid_derivative(network['output_layer'][i])
    
    for i in range(len(network['hidden_layer'])):
        hidden_errors[i] = 0.0
        for j in range(len(network['output_layer'])):
            hidden_errors[i] += output_errors[j] * network['weights_hidden_output'][i][j]
        hidden_errors[i] *= sigmoid_derivative(network['hidden_layer'][i])
    
    for i in range(len(network['hidden_layer'])):
        for j in range(len(network['output_layer'])):
            network['weights_hidden_output'][i][j] += network['learning_rate'] * output_errors[j] * network['hidden_layer'][i]
    
    for i in range(len(inputs)):
        for j in range(len(network['hidden_layer'])):
            network['weights_input_hidden'][i][j] += network['learning_rate'] * hidden_errors[j] * inputs[i]

def train_network(network, training_inputs, training_targets, epochs):
    for epoch in range(epochs):
        total_error = 0.0
        
        for i in range(len(training_inputs)):
            forward(network, training_inputs[i])
            backpropagate(network, training_inputs[i], training_targets[i])
            
            total_error += 0.5 * sum((training_targets[i][j] - network['output_layer'][j])**2 for j in range(len(training_targets[i])))
        
        if epoch % 100 == 0:
            print(f"Epoch {epoch}, Error: {total_error}")


training_inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
training_targets = [[0], [1], [1], [0]]

network = init_network(2, 2, 1, 0.5)

train_network(network, training_inputs, training_targets, 1000)

for input_data in training_inputs:
    output = forward(network, input_data)
    print(f"Input: {input_data[0]}, {input_data[1]} => Output: {output[0]}")


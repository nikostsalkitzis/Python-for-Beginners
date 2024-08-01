# Backpropagation in Neural Networks

Backpropagation is a fundamental algorithm used for training neural networks, which involves calculating gradients of the loss function with respect to each weight in the network and using these gradients to update the weights. The process consists of a forward pass, where the input data propagates through the network to compute the output, and a backward pass, where the gradients are computed and the weights are updated.

## 1. Forward Pass

In the forward pass, the input vector $\mathbf{x}$ is propagated through each layer of the network. For a given layer $l$, the linear combination of inputs is calculated as:

$$
\mathbf{z}^{(l)} = \mathbf{W}^{(l)} \mathbf{a}^{(l-1)} + \mathbf{b}^{(l)},
$$

where:
- $\mathbf{W}^{(l)}$ is the weight matrix for layer $l$,
- $\mathbf{a}^{(l-1)}$ is the activation vector from the previous layer (with $\mathbf{a}^{(0)} = \mathbf{x}$),
- $\mathbf{b}^{(l)}$ is the bias vector for layer $l$.

The activation for layer $l$ is then obtained by applying a non-linear activation function $\sigma$:

$$
\mathbf{a}^{(l)} = \sigma(\mathbf{z}^{(l)}).
$$

The output of the network $\mathbf{a}^{(L)}$ is then compared to the true target values $\mathbf{y}$ using a loss function $L(\mathbf{a}^{(L)}, \mathbf{y})$.

## 2. Backward Pass

The backward pass involves computing the gradient of the loss function with respect to each weight and bias in the network. The key idea is to use the chain rule to efficiently compute these gradients.

For the output layer $L$, the error term $\delta^{(L)}$ is defined as:

$$
\delta^{(L)} = \nabla_{\mathbf{z}^{(L)}} L(\mathbf{a}^{(L)}, \mathbf{y}) = \frac{\partial L}{\partial \mathbf{a}^{(L)}} \odot \sigma'(\mathbf{z}^{(L)}),
$$

where $\odot$ denotes the Hadamard (element-wise) product, and $\sigma'$ represents the derivative of the activation function $\sigma$.

For hidden layers, the error term $\delta^{(l)}$ can be recursively computed using the error from the subsequent layer $(l+1)$:

$$
\delta^{(l)} = \left( (\mathbf{W}^{(l+1)})^T \delta^{(l+1)} \right) \odot \sigma'(\mathbf{z}^{(l)}).
$$

The gradients of the loss function with respect to the weights and biases are then given by:

$$
\frac{\partial L}{\partial \mathbf{W}^{(l)}} = \delta^{(l)} (\mathbf{a}^{(l-1)})^T,
$$

$$
\frac{\partial L}{\partial \mathbf{b}^{(l)}} = \delta^{(l)}.
$$

## 3. Weight and Bias Updates

After calculating the gradients, the weights and biases are updated to minimize the loss function using an optimization algorithm, such as gradient descent. The update rules are:

$$
\mathbf{W}^{(l)} \leftarrow \mathbf{W}^{(l)} - \eta \frac{\partial L}{\partial \mathbf{W}^{(l)}},
$$

$$
\mathbf{b}^{(l)} \leftarrow \mathbf{b}^{(l)} - \eta \frac{\partial L}{\partial \mathbf{b}^{(l)}},
$$

where $\eta$ is the learning rate, a hyperparameter that controls the size of the steps taken to reach the minimum of the loss function.

## Conclusion

By iteratively applying these updates through multiple epochs, the neural network adjusts its weights and biases to minimize the loss function, thereby improving its performance on the training data. Backpropagation is a crucial component in the training of neural networks, enabling them to learn complex patterns and relationships in the data.

[Previous: Loss Functions](Loss%20Functions.md) | [Next: Optimizers](Optimizers.md)


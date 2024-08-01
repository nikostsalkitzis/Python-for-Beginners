# Activation Functions in Neural Networks

Activation functions play a crucial role in neural networks by introducing non-linearity into the model, allowing it to learn complex patterns. This document provides a comprehensive overview of various activation functions, including their mathematical definitions and properties.

## 1. Linear Activation Function

The linear activation function is defined as:

$$
f(x) = x
$$

**Properties:**
- It does not introduce non-linearity.
- Limited use in practice, mostly in linear regression.

## 2. Step Function

The step function is defined as:

$$
f(x) = 
\begin{cases} 
1 & \text{if } x \geq 0 \\
0 & \text{if } x < 0
\end{cases}
$$

**Properties:**
- Non-differentiable at $x = 0$.
- Used in binary classification problems but less common in deep networks.

## 3. Sigmoid Function

The sigmoid function is defined as:

$$
f(x) = \frac{1}{1 + e^{-x}}
$$

**Properties:**
- Outputs values in the range $(0, 1)$.
- Smooth gradient and differentiable everywhere.
- Prone to vanishing gradient problem for very large or very small inputs.

## 4. Hyperbolic Tangent (tanh) Function

The hyperbolic tangent function is defined as:

$$
f(x) = \tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}
$$

**Properties:**
- Outputs values in the range $(-1, 1)$.
- Zero-centered, which helps in balancing the gradients.
- Less prone to vanishing gradient problem compared to sigmoid.

## 5. ReLU (Rectified Linear Unit) Function

The ReLU function is defined as:

$$
f(x) = \max(0, x)
$$

**Properties:**
- Outputs values in the range $[0, \infty)$.
- Computationally efficient.
- Prone to the "dying ReLU" problem where neurons can become inactive during training.

## 6. Leaky ReLU Function

The Leaky ReLU function is defined as:

$$
f(x) = 
\begin{cases} 
x & \text{if } x \geq 0 \\
\alpha x & \text{if } x < 0
\end{cases}
$$

where $\alpha$ is a small constant, typically $\alpha = 0.01$.

**Properties:**
- Addresses the dying ReLU problem by allowing a small gradient when $x < 0$.

## 7. Parametric ReLU (PReLU) Function

The PReLU function is defined as:

$$
f(x) = 
\begin{cases} 
x & \text{if } x \geq 0 \\
\alpha x & \text{if } x < 0
\end{cases}
$$

where $\alpha$ is a learned parameter.

**Properties:**
- The value of $\alpha$ is learned during training, providing more flexibility.

## 8. Exponential Linear Unit (ELU) Function

The ELU function is defined as:

$$
f(x) = 
\begin{cases} 
x & \text{if } x \geq 0 \\
\alpha (e^x - 1) & \text{if } x < 0
\end{cases}
$$

where $\alpha$ is a positive constant.

**Properties:**
- Outputs values in the range $(-\alpha, \infty)$.
- Addresses the vanishing gradient problem and has smooth gradients.

## 9. Swish Function

The Swish function is defined as:

$$
f(x) = x \cdot \sigma(x) = x \cdot \frac{1}{1 + e^{-x}}
$$

where $\sigma(x)$ is the sigmoid function.

**Properties:**
- Provides a smooth and non-monotonic curve.
- Can outperform ReLU in some cases.

## 10. Softmax Function

The softmax function is used primarily in the output layer of classification networks. It is defined as:

$$
f(x_i) = \frac{e^{x_i}}{\sum_{j} e^{x_j}}
$$

where $x_i$ is the input to the $i$-th neuron, and the sum is over all the neurons in the output layer.

**Properties:**
- Converts logits (raw output values) into probabilities.
- Useful for multi-class classification problems.

## Conclusion

Each activation function has its strengths and weaknesses. The choice of activation function can significantly impact the performance of a neural network, and often the best function depends on the specific problem and architecture.

Feel free to experiment with different activation functions to find the one that works best for your neural network model.
[Previous: Overview and Introduction](General Theory For Neural Networks.md) | [Next: Loss Functions](Loss Functions.md)

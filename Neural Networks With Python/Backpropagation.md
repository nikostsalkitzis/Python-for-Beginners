\documentclass{article}
\usepackage{amsmath}

\begin{document}

\section*{Backpropagation in Neural Networks}

Backpropagation is a fundamental algorithm used for training neural networks, which involves calculating gradients of the loss function with respect to each weight in the network and using these gradients to update the weights. The process consists of a forward pass, where the input data propagates through the network to compute the output, and a backward pass, where the gradients are computed and the weights are updated.

\subsection*{1. Forward Pass}

In the forward pass, the input vector $\mathbf{x}$ is propagated through each layer of the network. For a given layer $l$, the linear combination of inputs is calculated as:

\begin{equation}
\mathbf{z}^{(l)} = \mathbf{W}^{(l)} \mathbf{a}^{(l-1)} + \mathbf{b}^{(l)},
\end{equation}

where:
\begin{itemize}
    \item $\mathbf{W}^{(l)}$ is the weight matrix for layer $l$,
    \item $\mathbf{a}^{(l-1)}$ is the activation vector from the previous layer (with $\mathbf{a}^{(0)} = \mathbf{x}$),
    \item $\mathbf{b}^{(l)}$ is the bias vector for layer $l$.
\end{itemize}

The activation for layer $l$ is then obtained by applying a non-linear activation function $\sigma$:

\begin{equation}
\mathbf{a}^{(l)} = \sigma(\mathbf{z}^{(l)}).
\end{equation}

The output of the network $\mathbf{a}^{(L)}$ is then compared to the true target values $\mathbf{y}$ using a loss function $L(\mathbf{a}^{(L)}, \mathbf{y})$.

\subsection*{2. Backward Pass}

The backward pass involves computing the gradient of the loss function with respect to each weight and bias in the network. The key idea is to use the chain rule to efficiently compute these gradients.

For the output layer $L$, the error term $\delta^{(L)}$ is defined as:

\begin{equation}
\delta^{(L)} = \nabla_{\mathbf{z}^{(L)}} L(\mathbf{a}^{(L)}, \mathbf{y}) = \frac{\partial L}{\partial \mathbf{a}^{(L)}} \odot \sigma'(\mathbf{z}^{(L)}),
\end{equation}

where $\odot$ denotes the Hadamard (element-wise) product, and $\sigma'$ represents the derivative of the activation function $\sigma$.

For hidden layers, the error term $\delta^{(l)}$ can be recursively computed using the error from the subsequent layer $(l+1)$:

\begin{equation}
\delta^{(l)} = \left( (\mathbf{W}^{(l+1)})^T \delta^{(l+1)} \right) \odot \sigma'(\mathbf{z}^{(l)}).
\end{equation}

The gradients of the loss function with respect to the weights and biases are then given by:

\begin{equation}
\frac{\partial L}{\partial \mathbf{W}^{(l)}} = \delta^{(l)} (\mathbf{a}^{(l-1)})^T,
\end{equation}

\begin{equation}
\frac{\partial L}{\partial \mathbf{b}^{(l)}} = \delta^{(l)}.
\end{equation}

\subsection*{3. Weight and Bias Updates}

After calculating the gradients, the weights and biases are updated to minimize the loss function using an optimization algorithm, such as gradient descent. The update rules are:

\begin{equation}
\mathbf{W}^{(l)} \leftarrow \mathbf{W}^{(l)} - \eta \frac{\partial L}{\partial \mathbf{W}^{(l)}},
\end{equation}

\begin{equation}
\mathbf{b}^{(l)} \leftarrow \mathbf{b}^{(l)} - \eta \frac{\partial L}{\partial \mathbf{b}^{(l)}},
\end{equation}

where $\eta$ is the learning rate, a hyperparameter that controls the size of the steps taken to reach the minimum of the loss function.

\section*{Conclusion}

By iteratively applying these updates through multiple epochs, the neural network adjusts its weights and biases to minimize the loss function, thereby improving its performance on the training data. Backpropagation is a crucial component in the training of neural networks, enabling them to learn complex patterns and relationships in the data.

\end{document}

# Optimizers in Neural Networks

Optimizers are algorithms used to minimize the loss function during the training of neural networks. They update the network's weights to reduce the error between predicted and actual values. This document provides an overview of various optimization algorithms, including their mathematical definitions and properties.

## 1. Gradient Descent

Gradient Descent is one of the simplest optimization algorithms. It updates the weights by moving them in the direction of the negative gradient of the loss function.

The update rule is given by:

$$
w = w - \eta \nabla L(w)
$$

where:
- $w$ is the weight,
- $\eta$ is the learning rate,
- $\nabla L(w)$ is the gradient of the loss function $L(w)$ with respect to the weight $w$.

**Properties:**
- Simple and easy to implement.
- Can be slow to converge.
- May get stuck in local minima.

## 2. Stochastic Gradient Descent (SGD)

Stochastic Gradient Descent (SGD) is a variant of Gradient Descent where the weights are updated based on a single training example or a small batch of examples, rather than the entire dataset.

The update rule is:

$$
w = w - \eta \nabla L(w; x_i, y_i)
$$

where $(x_i, y_i)$ represents a single training example.

**Properties:**
- Faster than batch gradient descent for large datasets.
- Can introduce noise into the optimization process, which might help escape local minima.

## 3. Mini-Batch Gradient Descent

Mini-Batch Gradient Descent combines aspects of both Gradient Descent and Stochastic Gradient Descent. It updates the weights based on a small batch of training examples.

The update rule is:

$$
w = w - \eta \frac{1}{m} \sum_{i=1}^{m} \nabla L(w; x_i, y_i)
$$

where $m$ is the mini-batch size, and $(x_i, y_i)$ are the examples in the mini-batch.

**Properties:**
- Balances the computational efficiency of batch gradient descent with the faster convergence of SGD.
- Commonly used in practice.

## 4. Momentum

Momentum helps accelerate SGD by adding a fraction of the previous weight update to the current update. This method smooths out the optimization trajectory.

The update rules are:

$$
v = \beta v + (1 - \beta) \nabla L(w)
$$
$$
w = w - \eta v
$$

where:
- $v$ is the velocity (previous update),
- $\beta$ is the momentum coefficient, usually between 0.9 and 0.99.

**Properties:**
- Helps overcome local minima and accelerates convergence.
- Can improve performance in areas of the loss surface with shallow gradients.

## 5. Nesterov Accelerated Gradient (NAG)

Nesterov Accelerated Gradient is an improvement over standard momentum by incorporating the gradient of the approximate future position of the weights.

The update rules are:

$$
\hat{w} = w - \eta \beta v
$$
$$
v = \beta v + (1 - \beta) \nabla L(\hat{w})
$$
$$
w = w - \eta v
$$

where $\hat{w}$ is the "lookahead" weight.

**Properties:**
- Provides faster convergence compared to standard momentum.
- Helps to correct the direction of the gradient more accurately.

## 6. Adagrad

Adagrad adjusts the learning rate for each parameter individually based on its historical gradients. Parameters with larger gradients receive smaller updates.

The update rule is:

$$
w = w - \frac{\eta}{\sqrt{G_{t} + \epsilon}} \nabla L(w)
$$

where $G_t$ is the diagonal matrix of accumulated squared gradients, and $\epsilon$ is a small constant to avoid division by zero.

**Properties:**
- Adapts learning rates based on parameter updates.
- Can lead to very small learning rates for frequently updated parameters.

## 7. RMSprop

RMSprop modifies Adagrad by using a moving average of squared gradients to normalize the gradient updates.

The update rules are:

$$
v_t = \rho v_{t-1} + (1 - \rho) \nabla L(w)^2
$$
$$
w = w - \frac{\eta}{\sqrt{v_t + \epsilon}} \nabla L(w)
$$

where $v_t$ is the moving average of squared gradients, and $\rho$ is a decay factor (e.g., 0.9).

**Properties:**
- Addresses the problem of rapidly decreasing learning rates in Adagrad.
- Effective for non-stationary problems.

## 8. Adam (Adaptive Moment Estimation)

Adam combines the benefits of both RMSprop and momentum by using both the moving average of gradients and the moving average of squared gradients.

The update rules are:

$$
m_t = \beta_1 m_{t-1} + (1 - \beta_1) \nabla L(w)
$$
$$
v_t = \beta_2 v_{t-1} + (1 - \beta_2) \nabla L(w)^2
$$
$$
\hat{m}_t = \frac{m_t}{1 - \beta_1^t}
$$
$$
\hat{v}_t = \frac{v_t}{1 - \beta_2^t}
$$
$$
w = w - \frac{\eta \hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}
$$

where $m_t$ is the first moment (mean), $v_t$ is the second moment (uncentered variance), and $\hat{m}_t$ and $\hat{v}_t$ are bias-corrected estimates.

**Properties:**
- Combines the advantages of both RMSprop and momentum.
- Generally performs well in practice with minimal parameter tuning.

## 9. Nadam (Nesterov-accelerated Adaptive Moment Estimation)

Nadam combines Adam with Nesterov Accelerated Gradient, incorporating the lookahead gradient into the Adam update.

The update rules are:

$$
\hat{m}_t = \frac{m_t}{1 - \beta_1^t}
$$
$$
\hat{v}_t = \frac{v_t}{1 - \beta_2^t}
$$
$$
w = w - \frac{\eta (\beta_1 \hat{m}_t + (1 - \beta_1) \nabla L(w))}{\sqrt{\hat{v}_t} + \epsilon}
$$

**Properties:**
- Provides a blend of Adam and NAG.
- Can offer improved performance for some models.

## Conclusion

Each optimizer has its own strengths and weaknesses. The choice of optimizer can significantly impact the training speed and convergence of a neural network. Often, Adam and its variants are used due to their generally good performance across a wide range of tasks.

Feel free to experiment with different optimizers to find the one that works best for your neural network model.

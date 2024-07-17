# Linear Regression Algorithm

The Linear Regression algorithm has its roots in Galton's groundbreaking survey, which investigated the relationship between a son's and father's height. He coined the term "regression" to describe the phenomenon where a son's height tends to be closer to the average than the father's height, even though the father's height might pull it up or down from the mean. The goal of Linear Regression is to plot a line that has the least distance from every point in the dataset. This can be achieved using the method of Least Squares, where in a 2D space we calculate only the vertical distance ("up and down"). The objective is to minimize the distance of every point from the best-fit line. This can be done in various ways, such as minimizing the absolute or squared error, but the basis of all these methods is to minimize the distance from the line of regression.

## Foundation of the Problem

In the dataset, we are given a set of $n$ tuples of the format $(x_i, y_i)$ where $i = 1$ to $n$. We call the variable $x$ the independent variable and $y$ the dependent variable, and they both arise from observations. The model function uses the vector of the independent variables and another vector containing its $m$ parameters (let's denote this as $\mathbf{b}$). Furthermore, the mathematical formula of linear regression is $f(x, \mathbf{b})$, and we aim to find the vector $\mathbf{b}$ (meaning the parameters) which minimize the distance from the best-fit line. 

We define the residual as the distance from the actual $y_i$ of our prediction for $x_i$, so $r_i = y_i - f(x_i, \mathbf{b})$. The least squares method involves minimizing the sum of the squares of the residuals for every data point. In the 2D space, we have:

$$ f(x_i, \mathbf{b}) = b_1 x_i + b_0 $$

Thus, we need to determine the slope and the intercept of the line. In the more general case where we don't work in 2D space, we need to differentiate the equation of $S$ with respect to every parameter of the model. After applying that $r_i = y_i - f(x_i, \mathbf{b})$, we obtain this equation from which we can derive the best parameters. For more information on the further mathematics behind linear and non-linear least squares, please visit this [link](https://en.wikipedia.org/wiki/Linear_regression).

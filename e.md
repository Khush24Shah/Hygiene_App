# Softplus

In machine learning, we often use the `softplus` activation function. It is a smooth approximation to the `relu` function.

It is defined as:

$$\text{softplus}(x) = \log(1 + e^x)$$

The inverse of the `softplus` function is the `softminus` function. It is defined as:

$$\text{softminus}(x) = \log(e^x - 1)$$
Python Monte Carlo Efficient Frontier (PyMCEF) package
======================================================

Purpose
=======
PyMCEF is a python package to generate efficient frontier based on Monte Carlo simulated returns.

Fixed-target expected under performance is used as the risk measure for this stochastic programming problem.

User input
==========
The Monte Carlo simulated returns for all the assets in the investment universe is the input 
and will be to used to train the efficient frontier.

(Optional) The returns as a validation set to measure the performance of the efficient frontier.

Computation results
==================
The complete efficient frontier stored as a vector of efficient portfolios, 
each of which containing the following:
    1. A python dictionary, storing the asset index and weight in the portfolio
    2. In sample performance (Sharpe ratio etc.)
    3. The lower and upper bound for the lagrangian multiplier producing this particular portfolio
    4. Validation performance, if validation Monte Carlo simulated returns are provided.

Advantage
=========
This algorithm is very efficient, starting with lagrangian multiplier being infinite and the optional
portfolio being 100% in the asset with largest average return, only portfolios on the efficient 
frontier will be visited. 

This algorithm is based on simulated returns so it is model agnostic. This introduce huge flexibility 
to the user as no assumption is made on the type of return distribution (e.g. Gaussian)

Works remain to be done
=======================
At least two desirable functionalities are not implemented yet:
    1. Support for short position
    2. Support user specified upper and lower bound of the weights of each asset.

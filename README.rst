Python Monte Carlo Efficient Frontier (PyMCEF) package
======================================================

Purpose
=======
PyMCEF is a python package that can generate efficient frontier based on Monte Carlo simulated returns.

`A Quickstart tutorial`_

`Benchmark`_

PyMCEF is based on axiomatic Second-order Stochastic dominance portfolio theory.

Absolute SemiDeviation and Fixed-target expected under performance are used as the risk measure for
this stochastic programming problem. 
These two risk measures don't have the theoretical flaw in mean variance model. 

`One example when mean variance model fails`_

User input
==========
The Monte Carlo simulated returns for all the assets in the investment universe is the input 
and will be to used to train the efficient frontier.

(Optional) The returns as a validation set to measure the performance of the efficient frontier.

Computation results
===================
The complete efficient frontier stored as a vector of efficient portfolios, 
each of which containing the following:

    1. A python dictionary, storing the asset index and weight in the portfolio
    2. In sample performance (Sharpe ratio etc.)
    3. The lower and upper bound for the risk tolerance producing this particular portfolio
    4. Validation performance, if validation Monte Carlo simulated returns are provided.

Advantage
=========

This package implements the algorithm introduced by Prof. Robert J. Vanderbei in his Book:
`Linear Programming: Foundations and Extensions`_ and paper `Frontiers of Stochastically Nondominated Portfolios`_

This algorithm is very efficient, starting with risk tolerance (lagrangian multiplier) being infinite and the optimal
portfolio being 100% in the asset with the largest average return, only portfolios on the efficient
frontier will be visited. With the product of number of assets and number of simulated return less than
10 million, the time needed to construct the full efficient frontier is less than 1 minute.

Speed comparison on efficient frontier construction with other LP solvers
=========================================================================

.. image:: https://github.com/hzzyyy/pymcef/blob/master/output/performance.png

This algorithm is based on simulated returns so it is model agnostic
====================================================================

This introduce huge flexibility to the user as no assumption is made on the type of return distribution (e.g. Gaussian).

.. _`Linear Programming: Foundations and Extensions`: http://www.princeton.edu/~rvdb/LPbook/
.. _`Frontiers of Stochastically Nondominated Portfolios`: http://www.princeton.edu/~rvdb/tex/lpport/lpport8.pdf
.. _`A Quickstart tutorial`: http://nbviewer.jupyter.org/github/hzzyyy/pymcef/blob/master/Quickstart%20tutorial.ipynb
.. _`Benchmark`: http://nbviewer.jupyter.org/github/hzzyyy/pymcef/blob/master/Benchmark.ipynb
.. _`One example when mean variance model fails`: http://nbviewer.jupyter.org/github/hzzyyy/pymcef/blob/master/examples/When%20mean%20variance%20models%20fail.ipynb

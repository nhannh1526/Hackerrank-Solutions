# Task

In a single toss of 2 fair (evenly-weighted) six-sided dice, find the probability that their sum will be at most 9.

# Solution

Sample Space (S): $\binom{6}{1} * \binom{6}{1} = 36$

Event ($\tilde{A}$): $\{(6, 6), (6, 5), (6, 4), (4, 6), (5, 6), (5, 5)\}$ = 6

$P(\tilde{A})$: $\frac{|\tilde{A}|}{|S|} = \frac{6}{36} = \frac{1}{6}$

$P(A) = 1 - P(\tilde{A}) = 1 - \frac{1}{6} = \frac{5}{6}$
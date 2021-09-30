# Task
There are 3 urns labeled X, Y, and Z.
* Urn X contains 4 red balls and 3 black balls.
* Urn Y contains 5 red balls and 4 black balls.
* Urn Z contains 4 red balls and 4 black balls.

One ball is drawn from each of the 3 urns. What is the probability that, of the 3 balls drawn, 2 are red and 1 is black?

# Solution
Sample Space (S): $\binom{7}{1} * \binom{9}{1} * \binom{8}{1} = 504$  

Event (A): $\binom{4}{1} * \binom{5}{1} * \binom{4}{1} + \binom{4}{1} * \binom{4}{1} * \binom{4}{1} + \binom{3}{1} * \binom{5}{1} * \binom{4}{1} = 204$  

$P(A)$: $\frac{|A|}{|S|} = \frac{204}{504} = \frac{17}{42}$

---
title: Fermat's little theorem
css:
- ../../style.css
path: ../../

---
# Fermat's little theorem: How a gem from the past is crucial for our present.

One famous theorem in mathematics is fermat's little theorem, or the slighlty more general Euler's theorem.

One thing I really like about it is the following: At first the theorem seems inaccesible, however it's proof is really evident, once you introduce group theory,
and I mean the very basic of group theory.
It could be considered a corollary of Lagrange's theorem.

Euler's theorem is the basis of RSA encryption, which is helps to keep everything to you on the web private.
**Note**: RSA is mostly not recommended anymore, cryptographers advise ECC (Elliptic curve cryptography), however,
this also uses Euler's theorem, so another win for the old mathematicians.

It's thanks
to RSA, or more general asymetric encryption that prevents people from stealing your bank account detail or your facebook password, or
other sensible information you might want to hide.

## The theorem

So what does the theorem actually say? It states:

Given a prime **p** and any number $a$, then the remainder of dividing $a^p$ by $p$ is exactly $a$.

In mathematicians jargon we say ($a^p=a (mod p)).

I give the proof at the end of the article as usual.



## The proof

As I said before, this is little more than Lagrange theorem. Consider
the group $\mathbb{Z}_n^*$. And consider $a$ to be a non-zero element of $\mathbb{Z}_n^*$.

Then the cyclic group $<x>$ has some size exactly the order of $x$. That is:
$ord(x)=#<x>$=o$.
By Lagrange theorem, $o$ divides $n-1$, so $n-1=k*o$. So:

$$
x^(n-1)=(x^o)^k=1^k=1 (mod n)
$$

Multiplying both sides by x:
$$
x^n=x (mod n)
$$

This last equality also holds in the case $x=0$, so the proof is complete.

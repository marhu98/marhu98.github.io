---
title: A beautiful proof: Spheres are simply connected                                                        
css:
- ../../../style.css                
path: ../../../
---

# A beautiful proof: Spheres are simply connected

One professor of mine once said that one of the most humiliating 
facts for modern mathematician is that we still don't know the homotopy groups of spheres.
Sort of.

We do know techniques for calculating them, so if someone wants to calculate $\pi_50(\mathbb{S}^2)$,
then there are fancy techniques such as Postnikov tower, spectral sequence and others, that will allow
you after a tremendous amount of computation to know the solution.

However, we do not know a general formula, for example: Results on which are the possible groups,
or if there is some periodicty are rare, and highly celebrated.

It is more humiliating once we consider two things:
- The homology groups of spheres have been know for a long time.
- The homotpoy groups of a lot of spaces depend on the homotopy groups of spheres: Projective manifolds, $O(3)$ are some of these.


However, we do know a lot for $\pi_n(\mathbb{S}^n)$ if $k\leq n$. Here I present a short proof a like very much 
that shows $\pi_1(\mathbb{S}^n)=0$ for $n\geq2$.

Of course we know a stronger result: $\pi_k(\mathbb{S}^n)=0$ for $k\leq n$ ( and $\pi_n(\mathbb{S}^n)=\mathbb{Z}$).
We will take a peek on this beautiful result on another post, but more the moment we shall be content with the weaker result.
Let's begin


# Proof


We want to proof the following:

**
Let $\alpha:[0,1]\to \mathbb{S}^n$ be a continous curves, then there are homotopic,
that is, there exists $\gamma_t:[0,1]x[0,1]\to \mathbb{S}^n$ so that $\gamma_0=\alpha$ and $\gamma_1(t)=\alpha(0)$.
**

The proof is as follow take two points of $\mathbb{S}^n$, say the North and Sout Pole, which we call $N$ and $P$.


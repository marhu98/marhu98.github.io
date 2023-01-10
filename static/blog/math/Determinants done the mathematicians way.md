---
title: Determinants done the mathematicians way
css:
- ../../../style.css
path: ../../../
---

# Determinants done the mathematicians way

We all learn about determinants in high school. **Or do we?**
Take a moment and try to answer the following question: **What is a determinant?**

For most people, it's a black box, you put in some numbers and some other number comes out. This number has a lot of uses,
but why? Of course to know why someone is useful you might need to know what it is.
You might now some of it's properties, for example:
$$
det(AB)=det(A)det(B)
$$

Or if a matrix $A$ has two identical columns, then $det(A)=0$.

Determinants are very useful, but they tend to be abused. Using them before the students understands what they are
generates an innecesary layer of abstraction for early students of mathematics which causes people to see simple linear algebra
as something complex. When in truth, linear algebra is characterised for being beautifully simple.


## The abuse of determinants

Determiants are used to introduce a lot of concepts in linear algebra: Rank of matrices, eigenvalues and such.
However Sheldon Axler's [Down with determinants](https://www.maa.org/sites/default/files/pdf/awards/Axler-Ford-1996.pdf) illustrates
how most things can be done without determinats.
In my opinion one particularly good example is the following: Given a square matrix $A$, we say that a real number $\lambda$ is
an eigenvalue (eigen coming from the german for proper), if there is a vector $v$ so that: $Av=\lambda v$. And $v$ is called an eigenvector.

Simply put, the eigenvectors of a matrix are vectors on which calculation $Av$ is as simple as multiplying by a number (scalar in mathematicians jargon).

In every textbook of basic linear algebra you would find this theorem:

$$
If $A$ is a n\times n matrix. Then $A$ has at least one complex eigenvalue
$$

Then usual proof, of course, relies on determinants. The trick is not notice that $Av=\lambda v$ if and only if $(A-\lambda \mathcal{I})v=0$,
and as any person that has taken high school math knows, this is the same as saying:
$$
det(A-\lambda \mathcal{I})=0
$$

Finally, $det(A-\lambda \mathcal{I})$ is polynomial of odd degree (do an example of a $3\times 3$ matrix if you're not convinced). And every polynomial
has a complex root.


However, you don't need determinats for this: Fix any $v\neq 0$. Consider the following vectors: $v,Av,A^2v,\ldots,A^nv$.
Notice something interesting about them? Well, there are $n+1$ of them, so one more than the dimension! This means
they have to be linearly dependent: That is, it is possible to find $\b_0,\ldots,b_n$ so that:
$$
(b_0+b_1\cdot A+\ldots+b_n\cdot A^n)v=0
$$

Since the polynomial $b_0+b_1\cdot x+\ldots+b_n\cdot x^n$ can be factored into complex polynomials:
$$
b_0+b_1\cdot x+\ldots+b_n\cdot x^n=
b_n(x-x-0)\cdots (x-x_n)
$$

So we have
$$
0==(b_0+b_1\cdot A+\ldots+b_n\cdot A^n)v=
b_n(A-x_0\mathcal{I})\cdots (A-x_n\mathcal{i})v
$$

This can only happen if some $A-x_i\mathcal{I}$ sends some vector to $0$: The $x_i$ is by defintion an eigenvalue.

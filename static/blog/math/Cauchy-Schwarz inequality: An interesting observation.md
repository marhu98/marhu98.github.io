---
title: Cauchy-Schwarz inequality: An interesting observation                                                        
css:
- ../../../style.css                
path: ../../../
---

# Cauchy-Schwarz inequality: An interesting observation

The Cacuchy-Schwarz is one the most fundamental inequalities in all of mathematics, it appears in different flavours and with slightly addapted proofs.
The inequality claims the following:

- Let $u$,$v$ be two vectors of $\mathbb{R}^n$, then the dot product is at most the product of the norms:
$$
\vert <u,v>\vert = \vert\vert u\vert\vert\cdot \vert \vert v \vert \vert
$$

However, it appears in other forms, sometimes the above expresion appears expanded:

$$
\left(\sum_{i=1}^n u_iv_i\right)^2
=
\left(\sum_{i=1}^n u_i^2)\right)
\left(\sum_{i=1}^n v_i^2)\right)
$$

And it can be formulated for any scalar product as a matter of fact, so if u and v are also functions of $L^2(\Omega)$ then it holds true:

$$
\left(\int_\Omega uv\right)^2
=
\left(\int_\Omega u_2)\right)
\left(\int_\Omega v^2)\right)
$$


However, recently I came across a proof which is a one-liner: In fact a lot more can we proven in one line: 
(Disclaimer, this proof doesn't work when $<\cdot,\cdot>:E\times E\rigtharrow \mathbb{C}$).

- Given $\{b_1,\ldots,b_n\}\subset E$ where $E$ real-vector space (real subfield also works), then the Gram determinant is defined as:
$Gram(b_1,\ldots,b_n)=det_{i,j}(<i,j>)$.
Then $Gram(b_1,\ldots,b_n)>=0$.

The proof is very easy, if $P$ is the matrix that has $b_i$ as columns (that is $P=(b_1,\ldots,b_n)$) then:
$(<i,j>)_{i,j=1}^n=P^TP$. To see this, simply notice that the (i,j) position $P^TP$ is in fact $b_i^Tb_j=<b_i,b_j>$.

So  $det(<i,j>)_{i,j=1}^n=det(P^TP)=det(P^2)=(det(P))^2>=0$. And we have equality iff the $\b_i$ are linearly dependent.
This is why the Gramm determinant is sometimes also called the Gramm volume.

Now notice, when happens when we apply the above result with only two vectors? We get:

$$
\begin{matrix}
\vert\vert u\vert\vert^2 & <u,v>  \\
<u,v> & \vert\vert u\vert\vert^2 \\
\end{matrix}
=
\vert\vert u\vert\vert^2\cdot \vert \vert v \vert \vert^2+\vert <u,v>\vert^2
>=0
$$
Which is exactly Cauchy-Schwarz inequality, and we have for free that there is equality if and only if $u=\lambda v$.


Basically one line, as promised (Try to skip the explanation and it is a one-liner).


## Final note

As noted, this proof relies on the fact that if $\lambda\in\mathbb{K}$ then $\lambda^2>=0$. Which is not true in the complex field.
That is why usually a more complete proof is given, in case you are not familiar with that proof. Here is a hint (as it is an interesting exercise):
Consider the expresion:
$$
P(\alpha)<u+\alpha v.u+\alpha v>>=0
$$
Since $P(\alpha)$ is always real postive amount, even in $\mathbb{C}$, it has an extreme value. For which $\alpha$?


## Another proof of the Gram determinant being postive

The proof given above that $Gram(b_1,\ldots,b_n)>=0$ is not always the one I gave, for some reason, it more common
to study how the Gram determinant changes when we apply a basis transformation. 
Doing some high-school algebra it is easy to see that
$$
Gram(\alpha b_1+\lambda b_i,\ldots,b_n)=\alpha^2Gram(b_1,\ldots,b_n)
$$

So if we decompose $b_i$ by their coordinates in the cannonical basis:
$$
Gram(\sum b_1^i e_i,\ldots,\sum b_n^i e_i)=(b_1^1)^2\cdots(b_n^n)^2\cdot Gram(e_1,\ldot,e_n)=(b_1^1)^2\cdots(b_n^n)^2>=0
$$

Personally I like more the first proof.

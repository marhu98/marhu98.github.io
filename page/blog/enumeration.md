# How to count the infinity:  Calkin-Wilf trees.

Content
- The problem of counting

- Counting fractions

I want to talk about what
to me is one the most magical results in mathematics.
It's incredibly simple, yet it seems like I could not have guessed it in a million years.
This leads into the world of counting infinity.
And a particularly surprising solution that was
independtly discovered by a professional mathematician (Stern) and... Can you guess it?
Yes! A watchmaker! (Brocot).

## The problem of counting.

Stay with me for a second.
How to count sheep? Seems like a very easy problem, you start 1,2,3,...
Let's say you have two groups of sheeps, how do you know if they have the same size? You count them
and then you check if you counted the same on both groups. Super easy!

Okay, now let's suppose each group of sheep has infinitely many sheep (or you have insomnia).
How do you know if there are the same size? This gets very weird very soon... Let's see!

Let's say one group of sheeps are male, and the other are female, and you
organize a ball (let's assume it's male-female dance for the sake of simplicity,
picture a victorian sheep ball). 
If to every male sheep you can assign a female sheep to dance with, then there must be 
as many sheep male as female sheep.
Let's see an example below:


However, it's possible to rearange the sheep so that now there are free sheeps...
How is that possible? Seems impossible, doesn't it?


The issue get's a lot more paradoxical, in my opinion. You can use the same method
to pair the set of even numbers with the set of natural numbers. It sure
looks like the set of natural numbers should have twice the size, but of course,
what should double infinity be? If you think you know the answer, wait a bit, you're in for a shock (unless you REALLY
know the answer).

Okay, you can go further, you can pair every natural number with a pair of two natural numbers!
Or with 3, or 4. Because, again, infinity times infity sounds like it should be infinity.
In mathematics we write the set of natural numbers $\mathbb{N}$. And the set of all pairs of natural numbers
$\mathbb{N}^2$ this is the set made up of all elements that are alike to $(1,2)$ or $(9,3)$. But not $(0.1,-3)$
for example.

Realise the following: Pick your favorite natural number, let's call it $n$, then n can be expresed as a product of
an odd number and another number: That is $n=2^m\cdot k$ (k is an odd number here). If it's not clear to you how to do this do the
following: 
- Pick a random number. I picked $484$. Now, divide by $2$.
You get $484=2\cdot 242$.
- Repeat until you get an even number: $484=2^2\cdot 121$.

Note: If you're a math freshman this is an easy induction exercise that you should be able to do mentally. Try it out!

It also very easy to write a python program for doing this:

```
def decom(n):
    m = 0
    k = n
    while k%2==0:
        m=m+1
        k=k//2
    return m,k
test = 708472
result = decom(test)
assert(test==2**result[0]*result[1])
```

Although of course, true mathematicians use Haskell:

```
def decom(n):
    m = 0
    k = n
    while k%2==0:
        m=m+1
        k=k//2
    return m,k
test = 708472
result = decom(test)
assert(test==2**result[0]*result[1])
```


Can you do better? Can you think of a way to map $\mathbb{N}$ with $\mathbb{N}^3$? ($\mathbb{N}^3$ is the set of triplets of natural numbers).
Maybe with $\mathbb{N}^\infty$, this is the set of sequences of natural numbers that are eventually $0$, for example:
$(1,3,0,3,4,5,1,0,0,0,\ldots,)$ but not $(1,1,1,\ldots)$.

//For a complete showdown, here is an ocaml solution for the general case:

But.. how about the set of all pairs of infinitely many natural numbers? For example, let's consider (positive) decimal numbers,
they are composed of infinitely many digits. Can we pair the natural numbers with the decimal numbers? Let's see...


**Cantor diagonal argument**

Turns out it's impossibe! So $\infty+\infty=\infty$
and $\infty\cdot\infty=\infty$. But if you multiply 
$\infty$ by itself $\infty$ many times, you get: A new
type of infinity! What the heck!

This was Cantor's big realisation, not all infinities are created equal.
If you're anything like me you were told in school that infinity was infinty and that was
it.
Since Cantor's discovery, infinity has tormented the minds of many mathematicians. It even drove Cantor 
into an early grave at a mental insitution. Yikes!


## Counting fractions.

In summary of the previous section, there are several types of infinities. The smallest one, the one traditionally called,
$\aleph_0$ (pronounced aleph null) or countable infinity. Because... It's the size of the counting numbers. Mathematicians
are not very original with names.

What we showed in the previous sections can we summarized by the formulas:
$$
\aleph_0+\aleph_0=\aleph_0
\aleph_0\cdot\aleph_0=\aleph_0
$$
That is joining (adding) two sets of size $\aleph_0$ results in a set of equal size.
So does pairing all the elements of one with all the elements of the other. 

But $\aleph_0^{\aleph_0}>\aleph_0$. That is too much.

At this point we should come to the following realisation: 
Positive rational numbers are pairs of natural numbers. Sure there is some repetition, for example:
$\frac{1}{3}=\frac{2}{6}$. But there should be a countable number of rational numbers. Indeed there are.
Nice, but... how do we enumerate them exactly? It is not at all obvious.
We could very easily enumerate pairs of natural numbers, but it is hard to find an enumeration
of pairs of natural numbers that have greatest common divisor 1.

Turns out, there is a brilliantly simple solution. At least I think so, 
we can build a tree of rational numbers, let' see.

We start with the fraction $1/1$ and from this fraction we generate
two more fractions, two "sons": $1/2$ and $2/1$. Then we repeat,
from $1/2$ we generate $1/3$ and $2/3$ and so on. We can think of this process as the following
binary tree:


Furthermore, every fraction on the tree is reduced form. To see this
notice that if $p,q$ are coprime then so are $p+q$ and $p$ and respectively $p$ and $p+q$.

Okay, it's all very nice, but how can we sure that all fractions are on this tree? This is where the magic comes,
at least for me. Suppose there is a fraction $p/q$ which is not on the tree. Then we can choose among all of those that are not on the tree,
the one that has least denominator, let's call it $q$. And again, among those that have denominator $q$ and are not in the tree, that one that has 
smallest numerator $p$.

So $p/q$ is not in the tree by hypothesis. However that means that if $p>q$, $(p-q)/q$ was in the tree, because we choose
$p/q$ to have smallest numerator. And if $p<q$ then $p/(q-p)$ is no in tree (again, we chose it have smallest denominator.
And so, $p/q$ must be in the tree?

I don't know about you, but I find this argument very clever, it comes up a lot in mathematics. It's similar to induction, in fact,
it is usually equivalent to induction. But all we did was: Take the least counterexample, in some sense, and it must have some parent, 
and because the parent is smaller, it has to be on the tree, which contradicts the counterexample hypothesis.


## Other solution: Stern-Brocot trees.

However, suppose we wanted to calculate a fraction that was close
to $\sqrt{2}$, then Calkin-Wilf trees do not help us much.

This is particularly useful if you wanted to construct a clock that ticks on a period
which is not rational. You can only adjust the gears to have rational ratios, so you have to get as close as 
you can. That is why Brocot, a watch maker, developed a method for doing this.
Unbeknowst to him, Stern, a mathematician had gotten ahead of him by a few years.

Anyway, I find it amazing that this dark, pure, abstract branch of mathematics had a real world application.

The idea is the following, given two fractions, one smaller $p/q$ and one
greater $m/n$ we can find another fraction that lies in between simply by "adding" them in a funny way:
$(p+m)/(q+n)$.

The way this tree works is a little more complicated than the previous one.
can generate a fraction that lies in between the tw

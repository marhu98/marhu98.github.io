---                                                                                  
title: The "undefined"\ Zero to the zero
css:
- ../../../../style.css
path: ../../../../

---    

# Zero to the zero

High school teachers usually say that $0^0$ is undefined,
and most people go on believing that is true. Even some professional mathematicians,
however $0^0$ makes perfect sense and is perfectly defined.
There is no ambiguity about what it's value is. I hope the reader that the only
possible value is $0^0=1$.

Look at it this way, what is $2^3$. A number, sure, but what does it represent?
If you imagine the number two as a set with two elements, let's say $2=\{
a,b
    \}$
and 
$3=\{c,d,e\}$

Then, how many mapping are there from $\{a,b\}$ to 
$\{c,d,e\}$. If you think about it, there are $2$ choices where to send $a$,
and $2$ choices for $b$. So there are $2^3=8$ mappings.


So exponentiation just correspong to counting how many functions are between two sets.
But, what is a mapping? A mapping is an "assingment" from one set to another, 
but what does actually mean?
There are several ways in which mathematicians may define the concept of a mapping.
The most common one is to say that a mapping between two sets $f:A\to B$ is a subset of the cartesian product $A\times B$. Remember that $A\times B$ is the set of all elements of the form $(a,b)$ where $a$ is in $A$ and $b$ in $B$.


Then, if $f$ is a mapping, $(a,b)\in f$ if $f(a)=b$.
Furthermore, for a subset of $A\times B$ to we a mapping it needs to be "well defined". That means, that if $(a,b)$ and $(a,c)$ are both in $f$, then $b=c$.
Said differently, you can't assign to different values to the same number.

Okay, so what's $0^0$. Following with the previous logic, we think of $0$
as a set with zero elements, that is, the empty set. Then, whose $0\times 0$?
Well, how many pairs of the form $(a,b),a\in\emptyset,b\in\emptyset$?
Of course, there are none. So $0\times 0=0$, no big surprise here.

Now, here comes the twist. How many subsets does $0$ have? One! $0$ itself!
It is definetely true that $\emptyset\subset\emptyset$. And it turns out, this
subset follows all the properties to be a mapping.

And so, there is exactly one application between the empty set and the empty set,
the empty set itself. That is: $0^0=1$.

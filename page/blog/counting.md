# Counting is easy. Right?
On some previous post I talked about cardinals, now I want to talk about ordinals. 
Which in my opinion are a lot more fun.

One of the first experiences of little children with school is counting. The learn some numbers,
how to count up to 10, then up to 100, then how to potentially count up to any number.
One tragedy of life is that there are always as many numbers left to count as when you started.
An owe to the futility of life.

However, suppose that by some magic stroke of luck, you could actually count beyond infinity. 
The great mathematician Georg Cantor stumbled upon this problem when doing his PhD thesis. 
He realised that counting beyond infinity could make sense. I will talk about what his problem was at the end. 
(Here insert reference to Cantor part).


Supposse you can count $1,2,3,\ldots,\infty$! And then $\infty+1$ and then $\infty+2$ and so forth.
Soon you realise you could count $\infty+\infty$ and $\infty+\infty+\infty$ 
and $\infty+\infty+\infty+\infty+\ldots$.

So you get $\infty\times\infty$. And you stop to ponder how smart you are. But then you realise,
it hits you like a train, how about: $\infty\times\infty+1$.
Now we are messed up, of course, we can consider $\infty\times\infty\times\infty=\infty^3$
and then $\infty^\infty$.
And then $\infty^{\infty^
{\infty^{\cdots}}
}$.

And then your head might be blown. For simplicity, we mathematicians call this $\infty$ $\omega$
or $\omega_0$ (as we discussed there are many infinities).

Then last number, the ones with $\omega$ to the $\omega$, $\omega$- many times, we
call $\varepsilon_0$.

And all this counting "numbers", we call them ordinals.
Notice, all this ordinal have the same cardinal: $\aleph_0$. But they are
different, because they are ordered, in a very specific way. There is always one that comes after another.

Not necesarilly the other way around. Who comes before $\omega$? No-one. Who comes before $\varepsilon_0$,
no-one. But there is always that comes after. Weird!

$\varepsilon_0$ is weird for another reason, it's the first fixed point of exponentiation. What do I mean? 
Think about it for a second $\varepsilon_0^\omega=\varepsilon_0$. Another reason is, it might look
like $\varepsilon_0$ is a lot further away from $0$ that $\omega$. And you might be correct, in some sense.
However, there are as many numbers between $0$ and $\omega$ and between $0$ and $\epsilon_0$. How many? $\aleph_0$
of them. Bullocks!

## Well-ordering.

Before I mentioned that there is some ordinals are ordered in a very special way, 
but I did not say what made this ordering so special.
In mathematics jargo we say they are well ordered, but what does that actually mean?
It means the follwing: Suppose I have a question in my head, for example: What is smallest ordinal which is not
finite? Then I have an answer: $\omega_0$.

To recap, if I ask a question of the form: What is the smallest ordinal that has this property? And you can find at least one that has the property,
then you can find the smallest one.
This might seems obvious at first, but it's very special. For example, what is the smallest rational $x$, so that $x^2>2$?.
There is none. What is the smallest real number in the interval $(0,1)$? There is none. So it's not so easy to be well-ordered.

One natural question you might be asking youself is if every set can be well ordered somehow. Can we rearange the reals so that the are well ordered?
Well... We will very likely never know. The day we know, is the day mathematics will have to very reinvented. But that is a topic for another day.
It's what it's called undecidable, it can't be shown to be true and it can't be shown to be false. You can take it as an axiom, you 
can be in the religion that believes that every set can be well-ordered or you can be on the other side. Each one has it's perks.


One of my favourite line of argument goes like this: There are no boring natural numbers, for if there were, I could
ask: What is the smallest boring natural number?  Whatever number it, let's call it $n$, this number
has an interesting property: Every number below it is interesting. That must make it interesting!
So there are no boring numbers.
You can do the exact same argument for ordinals.
The savy among you (or people that already know this) might have notices there is some fihsy business. Indeed, I
did not say precisely what boring was. So I could mold it to mean whatever I wanted.
Lesson is: *When arguing always make sure that the person that you are arguing with has the same defintions as you do!*
Otherwise you might disagree on what you mean by boring (or feminism or fascists, can you thinks of a line of argumentation that
proves every natural number is fascist? Sure you can, if fascists is defined loosely enough. Of course the question is non-sensical,
numbers don't have opinions!).

At the start we mentioned $\varepsilon_0^\omega=\varepsilon_0$,
we can ask the question: What is the smallest number, that is greater than $\varepsilon_0$
that has the same property? The answer $\varepsilon_1$, and the next $\varepsilon_2$,
and then you can consider $\varepsilon_{\varepsilon_0}$ and of course: $\varepsilon_{\varepsilon_\omega}$
and so forth, you get the idea. There are as many $\varepsilon$'s as there any countable ordinals. Crazy, but
by this point it should not surprise you too much.

We can keep asking questions: What is the smallest ordinal that is not countable? The 
answer $\omega_1$. What is the cardinal of $\omega_1$? $\aleph_1$. Easy.
We can repeat this process as much as we want, until we get to $\omega_{\epsilon_0}$ or even $\omega_{\omega_1}$
and so forth.

There are so many ordinals there aren't even an infinity of them, there are more.
So many it makes no sense to ask how big they are.
Mathematics is not ready to understand that question.

## Super Geeky Math Section.
From this point on we get into math which is very interesting but a harder
for the uninitiated. Go see what you can understand! But don't we dissapointed if your head hurts.

### Cantor problem.

Ordinals might seem like they are purely abstract mathematical object with no connection to the real world.
After all, counting past infinty is impossible anyways. However, when Cantor stumbles upon them he was handling a very applied problem,
he was working with trigonometric series (one example of those would be the super famous Fourier series).

He was wondering, when two of these sequences are equal, and then realised that he had to look into the accumulation of sets.
What is the accumulation of a set? The accumulation of a set if the points of the set which are not isolated. 
Okay, what is an isolated point in a set? It's a point, that if you take a distance small enough, $\varepsilon$,
then there is no other point in the set that is $\varepsilon$-point to the original point.

Okay, examples are great for clarification. For example, finite set have an empty accumulation:
$\{x_1,\ldots,x_n\}'=\emptyset$. (We denote the accumulation of a set with a ').
Another example, is the set: 
$$
\{0\}\cup\{1/n:n\in\mathbb{N}_+\}
$$

What is it's accumulation? It's the set $\{0\}$.
We also have so-called perfect sets, sets which are their own accumulation, for example $[0,1$
or the (Cantor)[https://en.wikipedia.org/wiki/Cantor_set] set are perfect sets. 

This is what Cantor noticed, if we define $A^{(n)}$ to be the accumulation of $A$ taken $n$ times,
then we can always find a subset of the real numbers $A$, so that $A^{(n)}=\emptyset$ but $A^{(n-1)}\neq\emptyset$.
In fact, this is not difficult, as in the previous example, we took a discrete set, namely, $\{0\}$ whose
accumulation is empty and we expand it by taking fractions of the form $1/n$. Then we can repeat this procedure, we attach small enough variations
of every point to build a set whose accumulation takes one step longer to go to the empty set.

One extra challenge, we define $A^{(\omega)}=\cap_n A^{(n)}$, then we can build a set so that
$A^n\neq\emptyset$ for every $n$, but $A^{(\omega)}=\emptyset$.
Then we keep pulling the thread, we find a set $A$ so that $A^{(\omega)}\neq\emptyset$,
but $A^{(\omega+1)}=\emptyset$.

Now, out of the blue ordinals make sense, in fact you can play the previous game for every countable ordinal. Curiously, you can't do the
same for uncountable ordinales, once you get to $A^{(\omega_1)}$ it always stabilises.
So this gives a motivation for ordinal numbers.

### A quirck for topologists.

Let's consider the set $A_1=\{\alpha \text{ ordinal }: \alpha<\omega_1\}$, typically mathematicians called this set the
first uncounable ordinal set. (Again, we are not original with names).
We consider $B_1=A_1\cup \{\omega_1\}$.

As a note, the way the ordinals are constructed, $A_1=\omega_1$, that is, every ordinal is a set, the
set of all ordinals smaller than itself. For example, the number $2$ can be seen as $2=\{0,1\}$. What a coincidence that $2$
is a set with $2$ elements. If you are wondering how we define $0$. Well, what's the only set with $0$ elements?

Since $B_1$ is ordered it has a natural topology,
the order toplogy. That is the toplogy generated by the intervals:
$$
(\alpha,\beta)=\{\gamma:\alpha<\gamma<\beta\}
$$

In topology there are three "usually" equivalent notions: Compactness, sequentially compact and limit-point compactness.
It turns out compactness and sequentially compact are not related, meaning that having one doesn't imply the other.
However, finding counter examples is actually hard, in almost all spaces of interest, they are equivalent.
You can check this out at the awesome page: (Pi-base)[https://topology.pi-base.org/spaces?q=~compact%20%2B%20Sequentially%20Compact].

$B_1$ provides an example of a sequentailly compact space that is not compact.
Seen that is not compact is very easy, simply consider the open covering: 
$$
\{
(0,\beta),
\omega_1
\}_{\beta<B_1}
$$

Obviously, no finite subcovering can be found. 
Now, let's show that $B_1$ is sequentially compact. (I came with this proof, but I'm sure there are shorter ones).

First, there are two elementary facts that easily combine to give the answer:

- **Fact 1**: In a well ordered set, such as $B_1$, there is no infinite descending sequence.

- **Fact 2**: In the order topology, every bounded monotonous sequence converges to it's supremum.

Proof of this facts is traditionally left as an exercise, and so it shall be in honour of mathematical tradition.

Let's consider a sequence ${(\alpha)}_n$, we want to find a convergent subsequence.
Now simply observe that ${(\alpha)}_n$ either has constant
subsequence, or it doesn't. If it does, then pick that as a convergent subsequence, if it doesn't
given any $\alpha_n$ you can always find another $\alpha_m$ so that $\alpha_m\geq\alpha_n$, otherwise we are contradicting fact 1.
And so we can turn ${(\alpha)}_n$ into a monotonous sequence, and by fact 2 we are done.

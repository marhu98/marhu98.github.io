# Signatures: The old way and the new way.

A signature in a piece of paper is an age old proof of identity.
Even today, even though it's unreliable and easily forgeable. Yet in paper signature we trust.
There have been some mild attemps to change this. For example the spanish government made compulsory the adoption of a new form of id. An electronid id (called dnie [see here](https://www.dnielectronico.es/PortalDNIe/)).

If you are curious about the details of how digital signature works check out my post on: (here)[https://To-do]

## The problem with the old way.

The main problem with paper signatures is easy to guess: They are not really trustworthy.
For example: They are easy to duplicate. Let' say that to have a document with someone's signature on it. Take your phone, scan it and glue it any pdf you want. Voilà!

Some people remedy this by adding: Me, name surname with id bla bla...
I authorise this or another. Hopefully, I don't need to tell you why this is futile.

Since paper signature can be easily forged, your signature on a piece of paper doesn't mean anything, you can always argue somebody sign for you and it's very hard to prove otherwise.

Another problem: You sign a contract, then you find out one of the clause has been modified. But of course, you can't prove that. That's one reason we need notaries. A third party that ensures trust, that's very inefficient and can be removed with digital signatures.

On the contrary, digital signatures can't be forged, and they are attached to the content of the file they signed. Meaning that if you modified a signed file, an external verifier can check that the signature does not check out.

## Reinventing the wheel.

My grudge with dnie is that is it hard to use: You need to buy a special reader, install a proprietary software and get a new certificate every two years.

However, once you have it set up you can sign (and encrypt) documents. If your electronic signature appears on a document, it means you signed it, or someone stole your id. As of today (September, 2021) this signature is considered to be unbreakable.

**Unless**, the cryptographic algorithms used are not strong enough. And how would you know, do you ask? Well, you don't that's the problem. Because, the implementation details are hidden, and the software is closed source.

This is mildly infuriating once you consider the following two factors:
- There already existed free and open software and hardware that solved this: GnuPG.

- Because the government had to redo something that was already well done and free,
is cost the hard-working spanish tax payers a lot of money.

- You don't actually need speciallised hardware, you could store it in your computer (less safe) or on a usb (less safe but better) or you could build one for $2 
(gnuk)[https://salsa.debian.org/gnuk-team/gnuk/gnuk] (best).

- Id card should allow for password protection, which it doesn't, but GnuPG does.

- GnuPG allows the users to choose how secure they want their key to be. It has often been found that when left to the provider, they choose security that was too weak.

Of course, that was done pre 2008, aka, the good days, where no-one cared about wasting public money.

Not all are **bad things**, there is a good side: Doing this prevents so called man in the middle attack (or MITM for short). Because in this particular instance the government works as a **Certificate authority**. What this means is a guarantor that you are who you say you are.
I will give more details at the end of the post if you are curious.

## The better way.

One better way to this is one where you can choose how secure you are going to be.
First you have to choose which signing algorithm you are going to use. 
There are many algorithms to choose from. The two main options are RSA and ECC.
ECC is more modern and recomended, although RSA is still considered secure. In ECC there are several options as well, but don't worry about it now.

The first thing that you are goint to need is a key. Roughly, this is the way it works. You generate two keys (a key pair!). One is known as the public key and the private key. 

The names are very descriptive, you give your public key to whomever they ask,
and you keep your private key safe and encrypted with a passphrase. How do you think of a secure passphrase? So glad you asked, check here: (here)[https://github.com/marhu98/rdice] or (here for and external link)[https://www.eff.org/dice] 


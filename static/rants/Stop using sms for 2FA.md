---
title: Stop using sms for 2FA                                                        
css:
- ../../style.css                
path: ../../
---

# Stop using sms for 2FA---                                                                                  

So I was taking a look at the Coinbase reddit, and it's full of posts such as:
- post
- post
- post
- post

All claiming that their funds were stolen using a technique called SIM swap. If you don't know
what a SIM swap is, it's very straight forward, this is how it works:
To recover your password, coinbase wants a proof of your identity, so they send you a sms to your phone. Previously,
the hacker has called your phone company and said that you have a new sim card so maybe they could set your phone 
number to actually be linked to that new sim card.
To do this they pretend to be you, which is they can do if they happen to have same information about you, such as your id
number (or your ssn number if in the US).

After that, it's a piece of cake, they click "forgot password" and they receive their confirmation sms on their phone. And
of course, they take all of your money.

This is not the only way this might happen, in the (great) book the art of invisibility, Kevin Mitnick describes how if you're 
nearby the person that actually owns the account, when they receive their sms, you can intercept it.
This is because the cell phone towers simply broadcasts the sms, so anyone listening on it can read everyone's sms.
This should be alarming, it's equivalent to the mail officer shouting the content of your mail to your neighbours. By the way,
email didn't use to be better, but now is a lot more private.

So, if sms is so unsecure, not even encrypted, why is it that is still used everywhere? Most worrying, why is it still used by our banks?
It is extremely stupid, in my opinion that my free lichess.org account is better protected that my bank account. In general, bank security is 
backwards, but the fact that most banks force you to use sms 2FA is beyond infuriating. Not only that, I only know of a couple bank that allows
any actual secure 2FA (this being german and swiss banks, which is not surprising since these countries are among the most concerned about privacy).


Using TOTP as a second factor authentication costs nothing, and it is actually secure, yet banks will still do nothing about it.
In my opinion, this shows why by the day most people choose to stay away from the banks and choose other debanking options such as DeFi.
If the banking industry wishes to survive they should realise that unstoppable competition is brewing in the horizon, and the only way 
to stand up to it is to offer good services to their clients. Making sure that their money is actually safe should be a priority.

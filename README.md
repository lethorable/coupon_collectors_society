# coupon_collectors_society
Computational approach to coupon collectors problem. 

This is a small computational approach to coupon collectors problem https://en.wikipedia.org/wiki/Coupon_collector%27s_problem . Inspiration to this work is primarily for myself to understand and gain experience with python classes and also the widespread collector cards (in my son's case LEGO cards) handed out with purchases in a Danish nation-wide supermarket chain. 

The numerical solution to the classical problem can be easily calculated (n log(n)) as described in the wikipedia link above. Reality is a lot more complex: 

- In one pack of cards, there may be several cards that may be unique for the pack (a sample). 
- Kids tend to trade cards
- Some cards may be more rare than others
- ... 

The script is a simulation where a population of traders can interact in a simulation. Each trader has a budget and different days of the week to "shop" (gain more cards). All of the traders meet "daily" one on one to trade their cards. 

The script is a work in progress and hence I am not an expert in Python, there may be better ways to code it (please tell me :-) ). Suggestions are welcome. 

The script runs in python as installed per default on a mac OSX sierra. Probably also works out of the box on linux and win 10. 


(c) 2017 Thorbjørn Nielsen

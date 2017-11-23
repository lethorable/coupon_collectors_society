# coupon_collectors_society

Computational approach to coupon collectors problem.

This is a small computational approach to coupon collectors problem https://en.wikipedia.org/wiki/Coupon_collector%27s_problem .

This work serves primarily for myself to understand and gain experience with python classes. The script itself has no purpose but to illustrate how various factors affects the result. The starting point is the widespread collector cards - could be baseball/football or other collectors items. In my case it is LEGO cards handed out with purchases in a Danish nation-wide supermarket chain and to which my son has a huge interest.

The numerical solution to the classical problem can be easily calculated (follows n*log(n) ) as described in the wikipedia link above. Reality is a lot more complex:

- In one pack of cards, there may be several cards that may be unique for the pack (a sample).
- Kids tend to trade cards
- Some cards may be more rare than others
- If a pack is handed out as a function of a purchase of a certain amount (€10 = 1 pack). Shopping for €29,50 will "waste" €9,50
- ...

So how much will be spent by one individual? Or combined? 

The script is a simulation where a population of traders can interact in a simulation. Each trader has a budget and different days of the week to "shop" (gain more cards). All of the traders meet "daily" one on one to trade their cards. The simulation answers how much each individual will have to spend and how much the population in total has spent.

Bear in mind that this is a work in progress and hence I am not an expert in Python, there may be better ways to code it (please tell me :-) ). Suggestions are welcome.

The script runs in python as installed per default on a mac OSX sierra. Probably also works out of the box on linux and win 10.


(c) 2017 Thorbjørn Nielsen

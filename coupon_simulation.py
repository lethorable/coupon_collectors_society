import math, random, sys

# constants

cards_per_pack = 4 # How many collector cards are in one package (per purchase)
price_per_pack = 100 # Cost of one pack of cards (or purchase needed to recieve one package)
number_to_be_collected = 144 # How many cards are there all in all (to get a complete collection)
numbers_of_pupils = 35 # How many pupils are there in the society (other collectors to trade with)
max_number_of_days = 100
household_budget_low = 700 #budget is per week (7 days)
household_budget_high = 2000


class pup():
	def __init__(self, number, shopdays=[], budget=0, coll={}):
		self.money_spent = 0
		self.coll={}
		self.number = number
		self.shopdays = shopdays
		self.budget = budget
		self.cardscollected = 0
		self.active = True
		self.timetocomplete = 0
		self.traded= 0
		self.bought = 0
		for i in range(0,number_to_be_collected):
			ist = str(i)
			self.coll[ist]=0
	def gotemall(self):
		return not 0 in self.coll.values()
	def mytraders(self):
		myA = []
		for i in range(0,number_to_be_collected):
			ist=str(i)
			if int(self.coll.get(ist)) >1:
				myA.append(ist)
		return myA
	def myempties(self):
		myA = []
		for i in range(0,number_to_be_collected):
			ist=str(i)
			if int(self.coll.get(ist)) ==0:
				myA.append(ist)
		return myA
	def addcards(self,pack=[]):
		for card in pack:
			self.bought = self.bought +1
			new_count = int(self.coll[str(card)]) +1
			self.coll[str(card)]=new_count

	def addcard(self,card):
		new_count = int(self.coll[str(card)]) +1
		self.coll[str(card)]=new_count
	def removecard(self,card):
		new_count = int(self.coll[str(card)]) -1
		self.coll[str(card)]=new_count
	def shop(self,day):
		if day in self.shopdays:
			random.seed()
			self.money_spent = self.money_spent + self.budget
			numpacks = math.trunc(self.budget / price_per_pack)
			for n in range(numpacks):
				pack = random.sample(range(0,number_to_be_collected),cards_per_pack)
				self.addcards(pack)


def trade(a,b):
#	print one.mytraders()
#	print other.myempties()
	ab = list(set(a.myempties()).intersection(set(b.mytraders())))
	ba = list(set(b.myempties()).intersection(set(a.mytraders())))
	#identify trades
	amounttotrade = min(len(ab),len(ba))
	for i in range(0,amounttotrade):
		a.removecard(ba[i])
		b.addcard(ba[i])
		a.addcard(ab[i])
		b.removecard(ab[i])
		a.traded = a.traded +1
		b.traded = b.traded+1
		print "     %s traded %s for %s with %s" %(a.number, ba[i],ab[i],b.number)


#	print len(ab)
#	print len(ba)

#	print one.coll
#	print other.coll
#
#		ba = set(self.mytraders()).intersection(other.myempties)
#	print ab
#		print ba


pups = []

for i in range(0,numbers_of_pupils):
	n_shop_days = random.randint(1,5)
	print n_shop_days
	shopdays=random.sample(range(0,6),n_shop_days)
	#calculate the amount to shop per actual trip to the supermarket
	budget = math.floor(random.randint(household_budget_low,household_budget_high)/len(shopdays))
	pups.append(pup(i,shopdays,budget))

print pups


going = True
numdays = 0
dayofweek = 0
while going:
	numdays = numdays + 1
	dayofweek = dayofweek + 1
	still_in_play =[]
	for i in pups:
		if i.active:
			still_in_play.append(i.number)
	print "ooooooooooooooooooooooooooooooooooooooooooo"
	print "          DAY %s   "%numdays
	print "          Active: %s"%still_in_play
	print "ooooooooooooooooooooooooooooooooooooooooooo"


	if dayofweek == 7:
		dayofweek = 0
	for pup in pups:
		if not pup.gotemall():
			pup.shop(dayofweek)
	for i in range(0,len(pups)):
		for j in range(0,len(pups)):
			if i==j:
				continue
			trade(pups[i],pups[j])
	stopp = True
	for pup in pups:
		if pup.gotemall()==False:
			stopp=False
	for pup in pups:
		if pup.active:
			if pup.gotemall():
				pup.active=False
				pup.timetocomplete = numdays
	going = not stopp
	if numdays == max_number_of_days:
		going = False

#	print "har brugt: %s kroner " %a.money_spent
#	going = not a.gotemall()

print "days to finish: %s" %numdays

for pup in pups:
	print "--------------------"
	print "number %s " %pup.number
	print "budget %s / week" %(pup.budget*len(pup.shopdays))
	print "money spent %s" %pup.money_spent
	print "cards bought %s" %pup.bought
	print "cards traded %s" %pup.traded
	print "time to complete %s" %pup.timetocomplete
	if pup.active:
		print "DID NOT FINISH"
	print "--------------------"

#	print "cards collected"

import math, random, sys

# constants

cards_per_pack = 4 # How many collector cards are in one package (per purchase)
price_per_pack = 100 # Cost of one pack of cards (or purchase needed to recieve one package)
number_to_be_collected = 144 # How many cards are there all in all (to get a complete collection)
numbers_of_pupils = 35 # How many pupils are there in the society (other collectors to trade with)




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
		for i in range(0,144):
			ist = str(i)
			self.coll[ist]=0
	def gotemall(self):
		return not 0 in self.coll.values()
	def mytraders(self):
		myA = []
		for i in range(0,144):
			ist=str(i)
			if int(self.coll.get(ist)) >1:
				myA.append(ist)
		return myA
	def myempties(self):
		myA = []
		for i in range(0,144):
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
				pack = random.sample(range(0,144),cards_per_pack)
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
	budget = random.randint(250,1050)
	pups.append(pup(i,shopdays,budget))

print pups

#sys.exit()

blop =[
pup(1,shopdays=[1,4],budget=500),
pup(2,shopdays=[2,6],budget=400),
pup(3,shopdays=[0,3],budget=1000),
pup(4,shopdays=[1,2],budget=600),
pup(5,shopdays=[2,6],budget=900),
pup(6,shopdays=[0,2,4,6],budget=200),

pup(7,shopdays=[1,4],budget=500),
pup(8,shopdays=[2,4,6],budget=400),
pup(9,shopdays=[0,3],budget=700),
pup(10,shopdays=[1,2],budget=600),
pup(11,shopdays=[2,6],budget=900),
pup(12,shopdays=[0,2,4,6],budget=200),
pup(13,shopdays=[1,4],budget=500),
pup(14,shopdays=[2,4,6],budget=400),
pup(15,shopdays=[0,3],budget=700),
pup(16,shopdays=[1,2],budget=600),
pup(17,shopdays=[2,6],budget=900),
pup(18,shopdays=[0,2,4,6],budget=200),

pup(19,shopdays=[1,4],budget=500),
pup(20,shopdays=[2,4,6],budget=400),
pup(21,shopdays=[0,3],budget=700),
pup(22,shopdays=[1,2],budget=600),
pup(23,shopdays=[2,6],budget=900),
pup(24,shopdays=[0,2,4,6],budget=200)
]



#print a.coll
#print b.coll


#a.addcards([4,7,9,111])
#a.addcards([7,9,110,109])
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

#	print "har brugt: %s kroner " %a.money_spent
#	going = not a.gotemall()

print "days to finish: %s" %numdays

for pup in pups:
	print "--------------------"
	print "number %s " %pup.number
	print "money spent %s" %pup.money_spent
	print "cards bought %s" %pup.bought
	print "cards traded %s" %pup.traded
	print "time to complete %s" %pup.timetocomplete
	print "--------------------"

#	print "cards collected"
